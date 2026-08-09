import base64
from datetime import datetime

import requests


def get_access_token(merchant_settings):
    consumer_key = merchant_settings.consumer_key
    consumer_secret = merchant_settings.consumer_secret

    credentials = f"{consumer_key}:{consumer_secret}"
    encoded_credentials = base64.b64encode(
        credentials.encode()
    ).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}"
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

    response = requests.get(
        url,
        headers=headers,
        timeout=30,
    )

    if response.status_code != 200:
        raise Exception(
            f"Failed to get access token: {response.text}"
        )

    return response.json()["access_token"]


def generate_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def generate_password(
    shortcode: str,
    passkey: str,
    timestamp: str,
):
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
    access_token = get_access_token(
        merchant_settings,
    )

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

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30,
    )

    print("\n========== STK PUSH RESPONSE ==========")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    print("=======================================\n")

    return response.json()