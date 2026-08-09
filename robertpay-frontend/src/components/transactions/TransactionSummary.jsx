const Card = ({ title, value, color}) => (
    <div className= {`rounded-xl shadow-md p-6} ${color}`}>
        <h3 className="text-sm font-medium">
            {title}
        </h3>

        <p className="text-3xl font-bold mt-2">
            {value}
        </p>
    </div>
);
    const TransactionSummary = ({
        walletBalance,
        totalCredits,
        totalDebits,
        transactionCount,
        currency,

    }) => {
        return (
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mb-8">
                <Card
                title="Wallet Balance"
                value={`${currency} ${walletBalance}`}
                color="bg-white"
                />
                <Card
                title="Total Credits"
                value={`${currency} ${totalCredits}`}
                color="bg-green-100 text-green-700"
                />
                <Card
                title="Total Debits"
                value={` ${currency} ${totalDebits}`}
                color="bg-red-100 text-red-700"
                />
                <Card
                title="Transactions"
                value={transactionCount}
                color="bg-blue-100 text-blue-700"
                />
            </div>
        );
    };

    export default TransactionSummary;
