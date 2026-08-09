import { useEffect,useState } from "react";

import DashboardLayout from "../../layouts/DashboardLayout";

import CreatePaymentRequestForm from "../../components/payments/CreatePaymentRequestForm";
import PaymentRequestsTable from "../../components/payments/PaymentRequestsTable";

import {
    getPaymentRequests,
    createPaymentRequest,
} from "../../services/paymentRequestService";
import { toast } from "react-toastify";
const PaymentRequests = () => {
    const [requests, setRequests] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        loadRequests();
        
        const interval = setInterval(() => {
            loadRequests();
        }, 5000);

        return () => clearInterval(interval);
    }, []);

    const loadRequests = async () => {
        try {
            const data = await getPaymentRequests();
            setRequests(data);
        } catch (error) {
            console.error(error);
            toast.error("Failed to load payment requests.");
        }
    };

    const handleCreate = async (FormData) => {
        setLoading(true);

        try {
            const response = await createPaymentRequest(FormData)

            if (
                response.stk_response?.ResponseCode === "0"
            ) {
                toast.success("STK Push sent successfully.");
            } else {
                toast.success("Payment request created.");
            }
            await loadRequests();
        } catch (error) {
            console.error(error);

            toast.error(
                error.response?.data?.detail ||
                "Failed to initiate STK Push."
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <DashboardLayout>
            <div className="max-w-7-xl mx-auto p-8">
                <h1 className="text-3xl font-bold mb-8">
                    Payment Requests
                </h1>
                <CreatePaymentRequestForm
               onSubmit={handleCreate}
               loading={loading} 
                />
                <PaymentRequestsTable
                requests={requests}
                />
            </div>
        </DashboardLayout>
    );
};

export default PaymentRequests;