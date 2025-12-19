import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000', // Configurable base URL
  withCredentials: true, // Send cookies with requests
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