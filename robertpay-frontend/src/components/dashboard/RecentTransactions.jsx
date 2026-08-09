import React from "react";

const RecentTransactions = ({ transactions }) => {
    return (
        <div className="bg-white rounded-xl shadow p-6">
            <h2 className="text-xl font-semibold mb-5">
                Recent Transactions
            </h2>
            {transactions.length === 0 ? (
                <p className="text-gray-500">
                    No transaction found.
                </p>
            ) :(
                <table className="w-full">
                    <thead>
                        <tr className="border-b">
                            <th className="text-left py-3">
                                Reference
                            </th>
                            <th className="text-left py-3">
                                Amount
                            </th>

                            <th className="text-left py-3">
                                Type
                            </th>
                            <th className="text-left py-3">
                                Status
                            </th>
                            <th className="text-left py-3">
                                Date
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {transactions.map((transaction) => (
                            <tr
                            key={transaction.id}
                            className="border-b hover:bg-gray-50"
                            >
                                <td
                                className="py-4"
                                >
                                    {transaction.reference}
                                </td>
                                <td
                                className="py-4"
                                >
                                    KES (Number(transaction.amount).toLocalString())
                                </td>

                                <td className="py-4">
                                    {transaction.type}
                                </td>
                                <td className="py-4">
                                    <span
                                    className={`px-2 py-1 rounded-full text-sm ${
                                    transaction.status === "SUCCESS"
                                    ? "bg-green-100 text-green-700"
                                    : transaction.status === "FAILED"
                                    ? "bg-red-100 text-red-700"
                                    : "bg-yellow-100 text-yellow-700" }`}
                                    >
                                        {transaction.status}
                                    </span>
                                </td>

                                <td className="py-4">
                                    {new Date(
                                        transaction.created_at
                                    ).toLocaleDateString()}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default RecentTransactions;