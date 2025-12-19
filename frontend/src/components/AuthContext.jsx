import { createContext, useContext, useState, useEffect } from 'react';
import api from '../services/api';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [authChecked, setAuthChecked] = useState(false);
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    const checkAuth = async () => {
      try {
        await api.get('/api/auth/verify');
        setIsAuth(true);
      } catch {
        setIsAuth(false);
      } finally {
        setAuthChecked(true);
      }
    };
    checkAuth();
  }, []);

  const handleLogout = () => {
    setIsAuth(false);
    window.location.href = '/login';
  };

  return (
    <AuthContext.Provider value={{ isAuth, authChecked, logout: handleLogout }}>
      {children}
    </AuthContext.Provider>
  );
};