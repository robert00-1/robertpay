
import api from "../api/axios";

export const getMerchantSettings = async () => {
  const response = await api.get("/merchant-settings");
  return response.data;
};

export const createMerchantSettings = async (data) => {
  const response = await api.post("/merchant-settings", data);
  return response.data;
};

export const updateMerchantSettings = async (data) => {
  const response = await api.put("/merchant-settings", data);
  return response.data;
};
