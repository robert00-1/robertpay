
import base64
from datetime import datetime

import requests


def get_access_token(merchant_settings):
    """Generate a Safaricom OAuth access token."""

    consumer_key = merchant_settings.consumer_key
    consumer_secret = merchant_settings.consumer_secret

    credentials = f"{consumer_key}:{consumer_secret}"
    encoded_credentials = base64.b64encode(
        credentials.encode()
    ).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
    }

    if merchant_settings.environment.lower() == "production":
        url = (
            "https://api.safaricom.co.ke/"
            "oauth/v1/generate?grant_type=client_credentials"
        )
    else:
        url = (
            "https://sandbox.safaricom.co.ke/"
            "oauth/v1/generate?grant_type=client_credentials"
        )

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=30,
        )

        print("\n========== OAUTH RESPONSE ==========")
        print("HTTP Status:", response.status_code)
        print("Response:", response.text)
        print("====================================\n")

        response.raise_for_status()

        access_token = response.json().get("access_token")

        if not access_token:
            raise ValueError(
                "Safaricom response did not contain an access token."
            )

        return access_token

    except requests.exceptions.RequestException as exc:
        print("\n========== OAUTH ERROR ==========")
        print("Error type:", type(exc).__name__)
        print("Error:", str(exc))
        print("=================================\n")
        raise


def generate_timestamp():
    """Generate the timestamp required by Safaricom."""

    return datetime.now().strftime("%Y%m%d%H%M%S")


def generate_password(
    shortcode: str,
    passkey: str,
    timestamp: str,
):
    """Generate the Base64-encoded STK Push password."""

    password = shortcode + passkey + timestamp

    return base64.b64encode(
        password.encode()
    ).decode()


def stk_push(
    merchant_settings,
    phone_number: str,
    amount: int,
    account_reference: str,
    transaction_desc: str,
):
    """Initiate an M-Pesa STK Push."""

    access_token = get_access_token(merchant_settings)

    timestamp = generate_timestamp()

    password = generate_password(
        merchant_settings.paybill_number,
        merchant_settings.passkey,
        timestamp,
    )

    if merchant_settings.environment.lower() == "production":
        url = (
            "https://api.safaricom.co.ke/"
            "mpesa/stkpush/v1/processrequest"
        )
    else:
        url = (
            "https://sandbox.safaricom.co.ke/"
            "mpesa/stkpush/v1/processrequest"
        )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    payload = {
        "BusinessShortCode": merchant_settings.paybill_number,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": merchant_settings.paybill_number,
        "PhoneNumber": phone_number,
        "CallBackURL": merchant_settings.callback_url,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc,
    }

    print("\n========== STK PUSH DEBUG ==========")
    print("Environment:", merchant_settings.environment)
    print("Safaricom endpoint:", url)
    print("Callback URL:", merchant_settings.callback_url)
    print("Business shortcode:", merchant_settings.paybill_number)
    print("Amount:", amount)
    print("Account reference:", account_reference)
    print("====================================\n")

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30,
        )

        print("\n========== STK PUSH RESPONSE ==========")
        print("HTTP Status:", response.status_code)
        print("Response:", response.text)
        print("=======================================\n")

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as exc:
        print("\n========== STK PUSH ERROR ==========")
        print("Error type:", type(exc).__name__)
        print("Error:", str(exc))
        print("====================================\n")
        raise
