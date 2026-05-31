// Replace the URL below with your actual Render web service link
const API_BASE = import.meta.env.VITE_API_URL || 'https://your-backend-app.onrender.com';

export const fetchFromAPI = async (endpoint) => {
  try {
    const response = await fetch(`${API_BASE}${endpoint}`);
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`Error fetching ${endpoint}:`, error);
    throw error;
  }
};
