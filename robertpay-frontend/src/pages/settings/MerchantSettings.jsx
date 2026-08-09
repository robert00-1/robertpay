import { useEffect, useState } from "react";
import DashboardLayout from "../../layouts/DashboardLayout";

import {
    getMerchantSettings,
    updateMerchantSettings,

} from "../../services/settingsService";

const MerchantSettings = () => {
    const [loading, setLoading] = useState(true);

    const [saving, setSaving] = useState(false);

    const [formData, setFormData] = useState({
        business_name: "",
        payment_type: "PAYBILL",
        paybill_number: "",
        account_number: "",
        callback_url: "",
        environment: "SANDBOX",
        is_active: true,
    });

    useEffect(() => {
        loadSetting();

    }, []);

    const loadSetting = async () => {
        try {
            const data = await getMerchantSettings();

            setFormData(data);
        } catch (error) {
            console.error(error);
            alert("Failed to load merchant settings.");
        } finally {
            setLoading(false);
        }
    };

    const handleChange = (e) => {
        const {name, value, type, checked} = e.target;

        setFormData((prev) => ({
            ...prev,
            [name]:
            type === "checkbox"
                  ? checked
                  : value, 
        }));
    };
    const handleSubmit = async (e) => {
        e.preventDefault();

        setSaving(true);

        try {
            await updateMerchantSettings(formData);

            alert("Settings updated sucessfully.");
        } catch (error) {
            console.error(error);

            alert("Failed to save settings.");
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return <h2 className="p-8">Loading...</h2>;
    }

    return (
        <DashboardLayout>
            <div className="max-w-4xl mx-auto p-8">
                <h1 className="text-3xl font-bold mb-8">
                    Merchant Settings
                </h1>

                <form
                onSubmit={handleSubmit}
                className="bg-white rounded-xl shadow p-8 space-y-6"
                >

                    <div>
                        <label>Business Name</label>
                        <input name="business_name"
                        value={formData.business_name}
                        onChange={handleChange}
                        className="w-full border rounded p-3 mt-2"
                        
                        />
                    </div>

                    <div>
                        <label>Payment Type</label>

                        <select
                        name="payment_type"
                        value={formData.payment_type}
                        onChange={handleChange}
                        className="w-full border rounded p-3 mt-2"
                        >
                            <option value="PAYBILL">
                                PAYBILL
                            </option>
                            <option value="BUY_GOODS">
                                BUY GOODS
                            </option>
                        </select>
                    </div>
                    <div>
                        <label>Paybill Number</label>

                        <input 
                        name="paybill_number"
                        value={formData.paybill_number || ""}
                        onChange={handleChange}
                        className="w-full border rounded p-3 mt-2"
                        />
                        <div>
                            <label>Account Number</label>

                            <input 
                            name="account_number"
                            value={formData.account_number}
                            onChange={handleChange}
                            className="w-full border rounder p-3 mt-2"
                            />


                        </div>
                        <div>
                            <label>Callback URL</label>

                            <input 
                            name="callback_url"
                            value={formData.callback_url || ""}
                            onChange={handleChange}
                            className="w-full border rounder p-3 mt-2"
                            />
                        </div>

                        <div>
                            <label>Enviroment</label>
                            <select name="environment" 
                            value={formData.environment}
                            onChange={handleChange}
                            className="w-full border rounded p-3 mt-2"
                            >

                                <option value="SANDBOX">
                                    SANDBOX
                                </option>
                                <option value="LIVE">
                                    LIVE
                                </option>
                            </select>

                            <div className="flex items-center gap-3">
                                <input type="checkbox"
                                name="is_active"
                                checked={formData.is_active}
                                onChange={handleChange}
                                />
                                <span>Merchant Active</span>
                            </div>
                            
                            <button 
                            type="submit"
                            disabled={saving}
                            className="bg-green-600 hover:bg-green-700 text-white px-8 rounded"
                            >
                                {
                                    saving
                                    ? "Saving..."
                                    : "Save Settings"
                                }
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </DashboardLayout>
    );
};
export default MerchantSettings;