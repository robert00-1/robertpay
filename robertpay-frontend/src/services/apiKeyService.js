import api from "../api/axios";

export const getApiKeys = async () => {
    const response = await api.get("/api-keys");
    return response.data;
};

export const regenerateApiKeys = async () => {
    const response = await api.post("/api-keys/regenerate");
    return response.data;
};