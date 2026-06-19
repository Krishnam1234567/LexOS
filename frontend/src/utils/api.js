const API_BASE = import.meta.env.VITE_API_URL || '/api';

// Intercept global fetch to inject Authorization header for all API calls
const originalFetch = window.fetch;
window.fetch = async (...args) => {
  let [resource, config] = args;
  
  // Convert URL object to string if necessary
  const urlString = typeof resource === 'string' ? resource : (resource instanceof Request ? resource.url : String(resource));
  
  // Only inject for API calls
  if (urlString.includes('/api') || urlString.startsWith(API_BASE)) {
    config = config || {};
    config.headers = config.headers || {};
    
    const stored = localStorage.getItem('lexos_session');
    if (stored) {
      try {
        const session = JSON.parse(stored);
        if (session && session.token) {
          if (config.headers instanceof Headers) {
            if (!config.headers.has('Authorization')) {
               config.headers.append('Authorization', `Bearer ${session.token}`);
            }
          } else {
            if (!config.headers['Authorization']) {
               config.headers['Authorization'] = `Bearer ${session.token}`;
            }
          }
        }
      } catch (e) {}
    }
    args[1] = config;
  }
  return originalFetch(...args);
};

export const fetchFromAPI = async (endpoint, options = {}) => {
  try {
    const url = endpoint.startsWith('/api') ? endpoint : `${API_BASE}${endpoint}`;
    const response = await fetch(url, options);
    
    if (!response.ok) {
      if (response.status === 401) {
        console.warn('Unauthorized request, token may be invalid or missing.');
      }
      throw new Error(`API error: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`Error fetching ${endpoint}:`, error);
    throw error;
  }
};
