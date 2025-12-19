import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000', // Direct backend URL
  withCredentials: true, // Send cookies with requests
});

// Request interceptor to add token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor to handle token expiry
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Do not redirect here to avoid full page reloads; let components handle 401
    return Promise.reject(error);
  }
);

export default api;