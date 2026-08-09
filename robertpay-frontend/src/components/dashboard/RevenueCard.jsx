import React from "react";

const RevenueCard = ({ title, amount}) => {
    return (
        <div className="bg-green-600 text-white rounded-xl p-6 shadow">
            <p className="text-green-100">
                {title}
            </p>

            <h2 className="text-3xl font-bold mt-2">
                KES {Number(amount).toLocaleString()}
            </h2>
        </div>
    );
};

export default RevenueCard;