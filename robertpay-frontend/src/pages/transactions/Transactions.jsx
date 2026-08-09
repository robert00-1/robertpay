import { useEffect, useState } from "react";

import DashboardLayout from "../../layouts/DashboardLayout";

import TransactionSummary from "../../components/transactions/TransactionSummary";
import TransactionTable from "../../components/transactions/TransactionTable";

import { getTransactions } from "../../services/transactionService";

const Transactions = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    loadTransactions();
  }, []);

  const loadTransactions = async () => {
    try {
      const response = await getTransactions();
      setData(response);
    } catch (error) {
      console.error(error);
    }
  };

  if (!data) {
    return (
      <div className="flex items-center justify-center h-screen">
        Loading transactions...
      </div>
    );
  }

  return (
    <DashboardLayout>

      <div className="max-w-7xl mx-auto p-8">

        <h1 className="text-3xl font-bold mb-8">
          Transactions
        </h1>

        <TransactionSummary
          walletBalance={data.wallet_balance}
          totalCredits={data.total_credits}
          totalDebits={data.total_debits}
          transactionCount={data.transaction_count}
          currency={data.currency}
        />

        <TransactionTable
          transactions={data.transactions}
        />

      </div>

    </DashboardLayout>
  );
};

export default Transactions;