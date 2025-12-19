import { Navigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

const ProtectedRoute = ({ children }) => {
  const { isAuth, authChecked } = useAuth();

  if (!authChecked) {
    return <div>Loading...</div>; // Show loading while checking auth
  }

  return isAuth ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;