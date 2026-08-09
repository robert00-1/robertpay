import { useEffect, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";

import {
    getApiKeys,
    regenerateApiKeys,
} from "../../services/apiKeyService";


const ApiKeys = () => {
    const [loading, setLoading] = useState(true);
    const [regenerating, setRegenerating] = useState(false);
    const [showSecret, setShowSecret] = useState(false);

    const [ApiKeys, setApiKeys] = useState({
        publishable_key: "",
        secret_key: "",
        status: "",
        created_at: "",
    });

    useEffect(() => {
        loadkeys();

    }, []);

    const loadkeys = async () => {
        try {
            const data = await getApiKeys();
            setApiKeys(data);
        } catch (err) {
            console.error(err);
            alert("Failed to load API keys.");
        } finally {
            setLoading(false);
        }
    };

    const copyText = (text) => {
        navigator.clipboard.writeText(text);
        alert("Copied!");
    };

    const regenerate = async () => {
        const ok = window.confirm(
            "Regenerate your API keys?\n\nYour old keys will stop working."
        );
        if (!ok) return;

        setRegenerating(true);

        try {
            const data = await regenerateApiKeys();
            setApiKeys(data);
            alert("API Keys regenerated successfully.");
        } catch (err) {
            console.error(err);
            alert("Failed to regenerate keys.");
        } finally {
            setRegenerating(false);
        }
    };

    if (loading) {
        return (
            <DashboardLayout>
                <div className="p-8">Loading...</div>
            </DashboardLayout>
        );
    }
    return (
        <DashboardLayout>
            <div className="max-w-4xl mx-auto p-8">
                <h1 className="text-3xl font-bold mb-8">
                    API Keys
                </h1>
                <div className="bg-white rounded-xl shadow p-8 space-y-8">
                    <div>
                        <label className="font-semibold block mb-2">
                            Publishable Key
                        </label>
                        <div className="flex gap-3">
                            <input 
                            readOnly
                            value={ApiKeys.publishable_key}
                            className="flex-1 border rounded p-3 bg-gray-100"
                            />
                            <button
                            onClick={() => 
                                copyText(ApiKeys.publishable_key)
                            }
                            className="bg-blue-600 text-white px-4 rounded"
                            >
                                Copy
                            </button>
                        </div>
                    </div>
                    <div>
                        <label className="font-semibold block mb-2">
                            Secret Key
                        </label>
                        <div className="flex gap-3">
                            <input 
                            readOnly
                            type={showSecret ? "text" : "password"}
                            value={ApiKeys.secret_key}
                            className="flex-1 border rounded p-3 bg-gray-100"
                            />
                            <button
                            onClick={() =>

                                setShowSecret(!showSecret)
                            }
                            className="bg-gray-700 text-white px-4 rounded"
                            >
                                {showSecret ? "Hide" : "Show"}
                            </button>
                            <button 
                            onClick={() => 
                                copyText(ApiKeys.secret_key)
                            }
                            className="bg-blue-600 text-white px-4 rounded"
                            >Copy</button>
                        </div>
                    </div>
                    <div className="grid grid-cols-2 gap-8">
                        <div>
                            <h3 className="font-semibold">
                                Status
                            </h3>
                            <p className="text-green-600 font-bold">
                                {ApiKeys.status}
                            </p>
                        </div>
                        <div>
                            <h3 className="font-semibold">
                                Created
                            </h3>
                            <p>
                                {new Date(
                                    ApiKeys.created_at

                                ).toLocaleString()}

                                

                            </p>
                        </div>
                    </div>
                    <button
                    onClick={regenerate}
                    disabled={regenerating}
                    className="bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded"
                    >
                        {
                            regenerating
                            ? "Regenerating..."
                            : "Regenerate API Keys"
                        }
                    </button>
                </div>
            </div>
        </DashboardLayout>
    )
}

export default ApiKeys;