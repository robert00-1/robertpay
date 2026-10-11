
import { useEffect, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";
import {
    getMerchantSettings,
    createMerchantSettings,
    updateMerchantSettings,
} from "../../services/settingsService";

const initialFormData = {
    business_name: "",
    payment_type: "PAYBILL",
    paybill_number: "",
    account_number: "",
    consumer_key: "",
    consumer_secret: "",
    passkey: "",
    callback_url: "",
    environment: "SANDBOX",
    is_active: true,
};

const MerchantSettings = () => {
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [settingsExist, setSettingsExist] = useState(false);
    const [formData, setFormData] = useState(initialFormData);

    useEffect(() => {
        loadSetting();
    }, []);

    const loadSetting = async () => {
        try {
            const data = await getMerchantSettings();

            setFormData({
                ...initialFormData,
                ...data,
                consumer_key: "",
                consumer_secret: "",
                passkey: "",
            });

            setSettingsExist(true);
        } catch (error) {
            if (error.response?.status === 404) {
                // No settings exist yet; allow the user to create them.
                setSettingsExist(false);
            } else {
                console.error("Failed to load merchant settings:", error);
                alert("Could not load settings. Please check your connection and try again.");
            }
        } finally {
            setLoading(false);
        }
    };

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;

        setFormData((prev) => ({
            ...prev,
            [name]: type === "checkbox" ? checked : value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setSaving(true);

        try {
            if (settingsExist) {
                const updateData = { ...formData };

                // Do not overwrite stored credentials with blank fields.
                if (!updateData.consumer_key) delete updateData.consumer_key;
                if (!updateData.consumer_secret) delete updateData.consumer_secret;
                if (!updateData.passkey) delete updateData.passkey;

                await updateMerchantSettings(updateData);
            } else {
                if (
                    !formData.consumer_key.trim() ||
                    !formData.consumer_secret.trim() ||
                    !formData.passkey.trim()
                ) {
                    alert("Enter your Daraja Consumer Key, Consumer Secret, and Passkey to create settings.");
                    return;
                }

                await createMerchantSettings(formData);
                setSettingsExist(true);
            }

            alert("Merchant settings saved successfully.");
        } catch (error) {
            console.error("Failed to save merchant settings:", error);

            const detail = error.response?.data?.detail;
            alert(
                typeof detail === "string"
                    ? detail
                    : "Failed to save settings. Check the backend response and try again."
            );
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return (
            <DashboardLayout>
                <h2 className="p-8">Loading merchant settings...</h2>
            </DashboardLayout>
        );
    }

    return (
        <DashboardLayout>
            <div className="max-w-4xl mx-auto p-8">
                <h1 className="text-3xl font-bold mb-3">
                    Merchant Settings
                </h1>

                <p className="text-gray-600 mb-8">
                    Configure your business details and Daraja sandbox credentials.
                </p>

                <form
                    onSubmit={handleSubmit}
                    className="bg-white rounded-xl shadow p-8 space-y-6"
                >
                    <div>
                        <label className="block font-medium">
                            Business Name
                        </label>
                        <input
                            type="text"
                            name="business_name"
                            value={formData.business_name}
                            onChange={handleChange}
                            required
                            className="w-full border rounded p-3 mt-2"
                        />
                    </div>

                    <div>
                        <label className="block font-medium">
                            Payment Type
                        </label>
                        <select
                            name="payment_type"
                            value={formData.payment_type}
                            onChange={handleChange}
                            className="w-full border rounded p-3 mt-2"
                        >
                            <option value="PAYBILL">Paybill</option>
                            <option value="BUY_GOODS">Buy Goods / Till</option>
                        </select>
                    </div>

                    <div>
                        <label className="block font-medium">
                            Paybill Number
                        </label>
                        <input
                            type="text"
                            name="paybill_number"
                            value={formData.paybill_number || ""}
                            onChange={handleChange}
                            className="w-full border rounded p-3 mt-2"
                        />
                    </div>

                    <div>
                        <label className="block font-medium">
                            Account Number
                        </label>
                        <input
                            type="text"
                            name="account_number"
                            value={formData.account_number || ""}
                            onChange={handleChange}
                            className="w-full border rounded p-3 mt-2"
                        />
                    </div>

                    <div className="border-t pt-6">
                        <h2 className="text-xl font-semibold mb-4">
                            Safaricom Daraja Credentials
                        </h2>

                        <p className="text-sm text-gray-600 mb-4">
                            Use your Daraja sandbox credentials for testing.
                            Leave credential fields blank when updating if you
                            do not want to replace the stored values.
                        </p>

                        <div className="space-y-4">
                            <div>
                                <label className="block font-medium">
                                    Consumer Key
                                </label>
                                <input
                                    type="text"
                                    name="consumer_key"
                                    value={formData.consumer_key}
                                    onChange={handleChange}
                                    autoComplete="off"
                                    required={!settingsExist}
                                    className="w-full border rounded p-3 mt-2"
                                />
                            </div>

                            <div>
                                <label className="block font-medium">
                                    Consumer Secret
                                </label>
                                <input
                                    type="password"
                                    name="consumer_secret"
                                    value={formData.consumer_secret}
                                    onChange={handleChange}
                                    autoComplete="new-password"
                                    required={!settingsExist}
                                    className="w-full border rounded p-3 mt-2"
                                />
                            </div>

                            <div>
                                <label className="block font-medium">
                                    Passkey
                                </label>
                                <input
                                    type="password"
                                    name="passkey"
                                    value={formData.passkey}
                                    onChange={handleChange}
                                    autoComplete="new-password"
                                    required={!settingsExist}
                                    className="w-full border rounded p-3 mt-2"
                                />
                            </div>
                        </div>
                    </div>

                    <div>
                        <label className="block font-medium">
                            Callback URL
                        </label>
                        <input
                            type="url"
                            name="callback_url"
                            value={formData.callback_url || ""}
                            onChange={handleChange}
                            placeholder="https://your-api.onrender.com/..."
                            className="w-full border rounded p-3 mt-2"
                        />
                    </div>

                    <div>
                        <label className="block font-medium">
                            Environment
                        </label>
                        <select
                            name="environment"
                            value={formData.environment}
                            onChange={handleChange}
                            className="w-full border rounded p-3 mt-2"
                        >
                            <option value="SANDBOX">Sandbox</option>
                            <option value="LIVE">Live</option>
                        </select>
                    </div>

                    <div className="flex items-center gap-3">
                        <input
                            id="is_active"
                            type="checkbox"
                            name="is_active"
                            checked={Boolean(formData.is_active)}
                            onChange={handleChange}
                            className="h-4 w-4"
                        />
                        <label htmlFor="is_active">
                            Merchant Active
                        </label>
                    </div>

                    <button
                        type="submit"
                        disabled={saving}
                        className="bg-green-600 hover:bg-green-700 disabled:opacity-50 text-white px-8 py-3 rounded"
                    >
                        {saving
                            ? "Saving..."
                            : settingsExist
                                ? "Update Settings"
                                : "Create Settings"}
                    </button>
                </form>
            </div>
        </DashboardLayout>
    );
};

export default MerchantSettings;