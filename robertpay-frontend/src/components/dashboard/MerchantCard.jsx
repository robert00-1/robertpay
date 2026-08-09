import React from "react";

const MerchantCard = ({
    businessName,
    paybillNumber,
    accountNumber,
    currency,
    isVerified,
}) => {
    return (
        <div className="bg-white rounded-xl shadow p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">
                Merchant Information
            </h2>

            <div className="space-y-3">

                <div className="flex-justify-between">
                    <span className="text-gray-500">Business</span>
                    <span className="font-medium">
                        {businessName}
                    </span>
                </div>

                <div className="flex justify-between">
                    <span className="text-gray-500">Paybill</span>
                    <span className="font-medium">
                        {paybillNumber || "."}
                    </span>
                </div>
                <div className="flex justify-between">
                    <span className="text-gray-500">Currency</span>
                    <span className="font-medium">
                        {currency}
                    </span>
                </div>
                <div className="flex justify-between">
                    <span className="text-gray-500">Status</span>

                    <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                        isVerified
                        ? "bg-green-100 text-green-700"
                        : "bg-red-100 text-red-700"
                    }`}>
                        {isVerified ? "Verified" : "Not Verified"}
                    </span>
                </div>
            </div>
        </div>
    );
};

export default MerchantCard;