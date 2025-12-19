import { useState, useEffect } from 'react';
import { useAuth } from './AuthContext';
import api from '../services/api';

const Profile = () => {
  const { logout } = useAuth();
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await api.get('/api/profile');
        setProfile(response.data);
      } catch (err) {
        if (err.response?.status === 401) {
          logout(); // Token expired, logout
        } else {
          setError(err.response?.data?.error || 'Failed to fetch profile');
        }
      }
    };
    fetchProfile();
  }, [logout]);

  if (error) {
    return <div className="text-red-500 text-center mt-8">{error}</div>;
  }

  if (!profile) {
    return <div className="text-center mt-8">Loading...</div>;
  }

  return (
    <div className="max-w-md mx-auto mt-8 bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Profile</h2>
      <div className="space-y-2">
        <p><strong>Name:</strong> {profile.name}</p>
        <p><strong>Email:</strong> {profile.email}</p>
        <p><strong>Aadhaar:</strong> {profile.aadhaar}</p>
      </div>
    </div>
  );
};

export default Profile;