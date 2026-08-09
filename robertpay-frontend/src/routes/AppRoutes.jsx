import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";
import Dashboard from "../pages/dashboard/Dashboard";
import PaymentRequests from "../pages/payments/PaymentRequests";
import Transactions from "../pages/transactions/Transactions";
import MerchantSettings from "../pages/settings/MerchantSettings";
import ApiKeys from "../pages/dashboard/ApiKeys";

import ProtectedRoute from "../components/layout/ProtectedRoute";
import Developers from "../pages/dashboard/Developers";
export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/register" element={<Register />} />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        <Route
          path="/payment-requests"
          element={
            <ProtectedRoute>
              <PaymentRequests />
            </ProtectedRoute>
          }
        />

        <Route
          path="/transactions"
          element={
            <ProtectedRoute>
              <Transactions />
            </ProtectedRoute>
          }
        />

        <Route
          path="/settings"
          element={
            <ProtectedRoute>
              <MerchantSettings />
            </ProtectedRoute>
          }
        />

        <Route
          path="/dashboard/api-keys"
          element={
            <ProtectedRoute>
              <ApiKeys />
            </ProtectedRoute>
          }
        />
        <Route
    path="/dashboard/developers"
    element={
        <ProtectedRoute>
            <Developers />
        </ProtectedRoute>
    }
/>

      </Routes>
    </BrowserRouter>
  );
}