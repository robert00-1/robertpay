import api from "../api/axios";

export const getPaymentRequests = async () => {
    const response = await api.get("/payment-requests");
    return response.data;
};

export const createPaymentRequest = async (data) => {
    const response = await api.post(
        "/payment-requests",
        data
    );
    return response.data;
};