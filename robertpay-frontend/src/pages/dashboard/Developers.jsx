import { useEffect, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import { getApiKeys } from "../../services/apiKeyService";

const Developers = () => {
    const [apiKeys, setApiKeys] = useState(null);

    useEffect(() => {
        loadKeys();
    }, []);

    const loadKeys = async () => {
        try {
            const data = await getApiKeys();
            setApiKeys(data);
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <DashboardLayout>
            <div className="max-w-6xl mx-auto p-8">
                <h1 className="text-3xl font-bold mb-2">
                    Developer Documentation
                </h1>

                <p className="text-gray-500 mb-8">
                    Integrate RobertPay into your application
                </p>

                <div className="space-y-8">

                    <div className="bg-white rounded-xl shadow p-6">
                        <h2 className="text-xl font-bold mb-4">
                            Base URL
                        </h2>

                        <code className="bg-gray-100 p-3 rounded block">
                            http://localhost:8000
                        </code>
                    </div>

                    <div className="bg-white rounded-xl shadow p-6">
                        <h2 className="text-xl font-bold mb-4">
                            Your API Keys
                        </h2>

                        <p className="mb-2">
                            <strong>Publishable Key</strong>
                        </p>

                        <code className="block bg-gray-100 p-3 rounded mb-4">
                            {apiKeys?.publishable_key || "Loading..."}
                        </code>

                        <p className="mb-2">
                            <strong>Secret Key</strong>
                        </p>

                        <code className="block bg-gray-100 p-3 rounded">
                            {apiKeys?.secret_key || "Loading..."}
                        </code>
                    </div>

                    <div className="bg-white rounded-xl shadow p-6">
                        <h2 className="text-xl font-bold mb-4">
                            Authentication
                        </h2>

                        <pre className="bg-gray-100 rounded p-4 overflow-x-auto">
{`Authorization: Bearer ${apiKeys?.secret_key || "Loading..."}
Content-Type: application/json`}
                        </pre>
                    </div>

                    <div className="bg-white rounded-xl shadow p-6">
                        <h2 className="text-xl font-bold mb-4">
                            Create Payment Request
                        </h2>

                        <pre className="bg-gray-100 rounded p-4 overflow-x-auto">
{`POST /payments/request

{
  "amount": 500,
  "phone": "254712345678",
  "reference": "ORDER1001",
  "description": "Payment for Shoe"
}`}
                        </pre>
                    </div>

                    <div className="bg-white rounded-xl shadow p-6">
                        <h2 className="text-xl font-bold mb-4">
                            Check Payment Status
                        </h2>

                        <pre className="bg-gray-100 rounded p-4 overflow-x-auto">
{`GET /payments/status/{transaction_id}`}
                        </pre>
                    </div>

                    <div className="bg-white rounded-xl shadow p-6">
                        <h2 className="text-xl font-bold mb-4">
                            Webhook Example
                        </h2>

                        <pre className="bg-gray-100 rounded p-4 overflow-x-auto">
{`POST https://robertpay.com/webhook

{
  "transaction_id": 25,
  "status": "SUCCESS",
  "amount": 500,
  "reference": "ORDER1001"
}`}
                        </pre>
                    </div>

                </div>
            </div>
        </DashboardLayout>
    );
};

export default Developers;