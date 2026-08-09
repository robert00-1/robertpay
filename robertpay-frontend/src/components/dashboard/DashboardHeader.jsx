import React from "react";

const DashboardHeader = ({ businessName}) => {
    return (
        <div className="mb-8">
            <h1 className="text-3xl font-bold text-gray-800">
                Welcome back 👋
            </h1>

            <p className="text-gray-500 mt-2">
                {businessName}
            </p>
        </div>
    );
};

export default DashboardHeader;