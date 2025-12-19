import api from './api';

export const register = async (userData) => {
  const response = await api.post('/api/auth/register', userData);
  return response.data;
};

export const login = async (credentials) => {
  const response = await api.post('/api/auth/login', credentials);
  return response.data;
};

export const logout = () => {
  // No need to remove token, as it's in cookies; just redirect
};

export const isAuthenticated = () => {
  // Since token is in cookies, we can't easily check here; rely on API calls
  return true; // Assume authenticated until 401
};