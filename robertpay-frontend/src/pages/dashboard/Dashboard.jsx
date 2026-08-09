import { useEffect, useState } from "react";

import DashboardLayout from "../../layouts/DashboardLayout";

import DashboardHeader from "../../components/dashboard/DashboardHeader";
import RevenueCard from "../../components/dashboard/RevenueCard";
import StatCard from "../../components/dashboard/StatCard";
import MerchantCard from "../../components/dashboard/MerchantCard";
import RecentTransactions from "../../components/dashboard/RecentTransactions";

import { getDashboard } from "../../services/dashboardService";


const Dashboard = () => {
  const [dashboard, setDashboard] = useState(null);
  const [loading, setLoading] = useState(true);
  const [apiKeys, setApiKeys] = useState(null);

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {
    try {
      const data = await getDashboard();
      setDashboard(data);
    } catch (error) {
      console.error("Failed to load dashboard:", error);
    } finally {
      setLoading(false);
    }
  };
  

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen bg-gray-100">
        <h2 className="text-2xl font-semibold text-gray-700">
          Loading Dashboard...
        </h2>
      </div>
    );
  }

  if (!dashboard) {
    return (
      <div className="flex items-center justify-center h-screen bg-gray-100">
        <h2 className="text-2xl font-semibold text-red-600">
          Failed to load dashboard.
        </h2>
      </div>
    );
  }

  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto">

        <DashboardHeader
          businessName={dashboard.business_name}
        />

        {/* Revenue Cards */}

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mt-8">

          <RevenueCard
            title="Wallet Balance"
            amount={dashboard.wallet_balance}
          />

          <RevenueCard
            title="Today's Revenue"
            amount={dashboard.today_revenue}
          />

          <RevenueCard
            title="Week Revenue"
            amount={dashboard.week_revenue}
          />

          <RevenueCard
            title="Month Revenue"
            amount={dashboard.month_revenue}
          />

        </div>

        {/* Statistics */}

        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6 mt-8">

          <StatCard
            title="Transactions"
            value={dashboard.transaction_count}
          />

          <StatCard
            title="Successful"
            value={dashboard.successful_transactions}
          />

          <StatCard
            title="Pending"
            value={dashboard.pending_transactions}
          />

          <StatCard
            title="Failed"
            value={dashboard.failed_transactions}
          />

        </div>

        {/* Merchant Information + Recent Transactions */}

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mt-8">

          <div className="lg:col-span-2">

            <RecentTransactions
              transactions={dashboard.recent_transactions}
            />

          </div>

          <MerchantCard
            businessName={dashboard.business_name}
            paybillNumber={dashboard.paybill_number}
            tillNumber={dashboard.till_number}
            currency={dashboard.currency}
            isVerified={dashboard.is_verified}
          />

        </div>

      </div>
    </DashboardLayout>
  );
};

export default Dashboard;