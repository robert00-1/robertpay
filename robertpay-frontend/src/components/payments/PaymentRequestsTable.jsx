const PaymentRequestsTable = ({ requests}) => {
    const getStatusColor = (status) => {
        switch (status) {
            case "PAID":
                return "bg-green -100 text-green-700";

                case "PENDING":
                    return "bg-yellow-100 text-yellow-700";
                
                    
                case "FAILED":
                    return "bg-red-100 text-red-700";
                
                default:
                    return "bg-gray-100 text-gray-700";    
        }
    };

    return (
        <div className="bg-white rounded-xl shadow-md p-6 mt-8">
            <h2 className="text-2xl font-bold mb-6">
                Payment Requests
            </h2>

            <div className="overflow-x-auto">
                <table className="overflow-x-auto">
                    <thead>
                        <tr className="border-b">
                            <th className="text-left py-3">
                                Customer
                            </th>
                            <th className="text-left py-3">Phone</th>
                            <th className="text-left py-3">Amount</th>
                            <th className="text-left py-3">Reference</th>
                            <th className="text-left py-3">Status</th>
                            <th className="text-left py-3">Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        {requests.length === 0 ? (
                            <tr>
                                <td
                                colSpan={6}
                                className="text-center py-10 text-gray-500"
                                >
                                    No payment requests found
                                </td>
                            </tr>
                        ) : (
                            requests.map((request) => (
                                <tr 
                                key={request.id}
                                className="border-b hover:bg-gray-500"
                                >
                                    <td className="py-4">
                                        {request.customer_name}
                                    </td>
                                    <td>
                                        {request.customer_phone}
                                    </td>
                                    <td>
                                        KES {request.amount}
                                    </td>
                                    <td>
                                        {request.reference}
                                    </td>
                                    <td>

                                        <span
                                        className={`px-3 py-1 rounded-full text-sm font-medium ${getStatusColor(
                                            request.status
                                        )}`}
                                        >
                                        {request.status}
                                        </span>
                                    </td>

                                    <td>
                                        {new Date(
                                            request.create_at
                                        ).toLocaleDateString()}
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default PaymentRequestsTable;