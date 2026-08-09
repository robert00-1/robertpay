const TransactionTable = ({ transactions }) => {
    const getStatusColor = (status) => {
        switch (status) {
            case "SUCCESS":
                return "bg-green-100 text-green-700";

            case "PENDING":
                return "bg-yellow-100 text-yellow-700";
            
            case "FAILED":
                return "bg-red-100 text-red-700";
            
           default:
            return "bg-gray-100 text-gray-700";     
        }
    };

    return (
        <div className="bg-white rounded-xl shadow-md p-6">
            <h2 className="text-2xl font-bold mb-6">
                Transaction History
            </h2>

            <div className="overflow-x-auto">
                <table className="w-full">
                    <thead>
                        <tr className="border-b text-left">
                            <th className="py-3">Date</th>
                            <th className="py-3">Type</th>
                            <th className="py-3">Amount</th>
                            <th className="py-3">Reference</th>
                            <th className="py-3">Description</th>
                            <th className="py-3">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {transactions.map((transaction) => (
                            <tr
                            key={transaction.id}
                            className="border-b hover:bg-gray-50"
                            >
                                <td className="py-4">
                                    {new Date(
                                        transaction.created_at
                                    ).toLocaleString()}
                                </td>
                                <td>
                                    <span 
                                    className={`font-semibold ${
                                        transaction.type == "CREDIT"
                                        ? "text-green-600"
                                        : "text-red-600"
                                    }`}
                                    >
                                        {transaction.type === "CREDIT"
                                        ? " ⬇ Credit"
                                        : "⬇ Debit "}
                                    </span>
                                </td>
                                <td>
                                    KES {transaction.amount}
                                </td>
                                <td>
                                    {transaction.reference}
                                </td>
                                <td>
                                    {transaction.description}
                                </td>

                                <td>
                                    <span
                                    className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(
                                        transaction.status
                                    )}`}
                                    >
                                        {transaction.status}
                                    </span>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};
export default TransactionTable;