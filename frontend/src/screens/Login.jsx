import { useState } from 'react';
import { Eye, EyeOff, Scale, Loader2, Shield, Zap, GitBranch } from 'lucide-react';
import { GoogleLogin } from '@react-oauth/google';
import { jwtDecode } from 'jwt-decode';

const DEMO_USERS = [
  { email: 'sarah.chen@demo.lexos.app',    password: 'demo', name: 'Sarah Chen',     role: 'General Counsel',      avatar: 'SC' },
  { email: 'marcus.okafor@demo.lexos.app', password: 'demo', name: 'Marcus Okafor',  role: 'Senior Legal Counsel', avatar: 'MO' },
  { email: 'admin@demo.lexos.app',         password: 'demo', name: 'Admin',           role: 'System Administrator', avatar: 'AD' },
];

const FEATURES = [
  { icon: Zap,       text: 'AI-powered legal intelligence with Gemini' },
  { icon: Shield,    text: '14 compliance frameworks monitored' },
  { icon: GitBranch, text: 'Interactive legal knowledge graph' },
  { icon: Scale,     text: 'Real-time litigation risk assessment' },
];

export function Login({ onLogin }) {
  const [email, setEmail]     = useState('');
  const [password, setPass]   = useState('');
  const [showPass, setShow]   = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState('');

  const handleGoogleSuccess = async (credentialResponse) => {
    setError('');
    setLoading(true);
    try {
      const decoded = jwtDecode(credentialResponse.credential);
      const session = {
        email: decoded.email,
        name: decoded.name,
        picture: decoded.picture,
        token: credentialResponse.credential, // Save the token for API calls
        role: 'Authenticated User',
        avatar: decoded.name ? decoded.name.substring(0, 2).toUpperCase() : 'U',
        loginAt: Date.now()
      };
      localStorage.setItem('lexos_session', JSON.stringify(session));
      onLogin(session);
    } catch (err) {
      setError('Failed to parse Google login response.');
    }
    setLoading(false);
  };

  const handleGoogleError = () => {
    setError('Google Sign-In failed. Please try again.');
  };

  return (
    <div className="min-h-screen bg-background flex">
      {/* Left Panel */}
      <div className="hidden lg:flex lg:w-1/2 bg-card border-r border-border flex-col justify-between p-12 relative overflow-hidden">
        {/* Background glow */}
        <div className="absolute top-0 left-0 w-full h-full pointer-events-none">
          <div className="absolute -top-40 -left-40 w-96 h-96 bg-primary/10 rounded-full blur-3xl" />
          <div className="absolute -bottom-40 -right-20 w-80 h-80 bg-accent/10 rounded-full blur-3xl" />
        </div>

        <div className="relative z-10">
          <div className="flex items-center gap-3 mb-16">
            <div className="w-10 h-10 bg-primary rounded-xl flex items-center justify-center">
              <Scale className="w-5 h-5 text-white" />
            </div>
            <div>
              <p className="text-lg font-bold text-foreground tracking-tight">LexOS</p>
              <p className="text-xs text-muted-foreground">Legal Operating System</p>
            </div>
          </div>

          <h1 className="text-4xl font-bold text-foreground leading-tight mb-6">
            The AI-powered<br />
            <span className="text-primary">legal intelligence</span><br />
            platform for enterprises.
          </h1>
          <p className="text-base text-muted-foreground leading-relaxed mb-12">
            Manage contracts, litigation, compliance, and global expansion — all powered by Gemini AI and real-time legal intelligence.
          </p>

          <div className="space-y-4">
            {FEATURES.map(({ icon: Icon, text }) => (
              <div key={text} className="flex items-center gap-3">
                <div className="w-8 h-8 bg-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                  <Icon className="w-4 h-4 text-primary" />
                </div>
                <span className="text-sm text-muted-foreground">{text}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="relative z-10">
          <div className="flex items-center gap-2 p-3 bg-accent/5 border border-accent/20 rounded-xl">
            <Shield className="w-4 h-4 text-accent flex-shrink-0" />
            <p className="text-xs text-muted-foreground">SOC 2 Type II certified · GDPR compliant · 256-bit encryption</p>
          </div>
        </div>
      </div>

      {/* Right Panel */}
      <div className="flex-1 flex items-center justify-center p-8">
        <div className="w-full max-w-md">
          {/* Mobile logo */}
          <div className="flex items-center gap-2 mb-8 lg:hidden">
            <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
              <Scale className="w-4 h-4 text-white" />
            </div>
            <p className="text-lg font-bold text-foreground">LexOS</p>
          </div>

          <div className="mb-8">
            <h2 className="text-2xl font-bold text-foreground mb-2">Welcome back</h2>
            <p className="text-sm text-muted-foreground">Sign in to your LexOS workspace</p>
          </div>

          <div className="flex flex-col items-center gap-4">
            <div className="w-full flex justify-center">
              <GoogleLogin
                onSuccess={handleGoogleSuccess}
                onError={handleGoogleError}
                useOneTap
                theme="outline"
                size="large"
              />
            </div>
            
            {error && (
              <div className="w-full p-3 bg-destructive/10 border border-destructive/20 rounded-lg">
                <p className="text-xs text-destructive text-center">{error}</p>
              </div>
            )}
            
            <div className="w-full mt-6 border-t border-border pt-6">
              <p className="text-xs text-muted-foreground mb-3 font-medium uppercase tracking-wider text-center">Or continue with demo account</p>
              <div className="flex gap-2">
                {DEMO_USERS.map(u => (
                  <button key={u.email} onClick={() => {
                    const session = { ...u, token: 'mock_token', loginAt: Date.now() };
                    localStorage.setItem('lexos_session', JSON.stringify(session));
                    onLogin(session);
                  }}
                    className="flex-1 flex flex-col items-center gap-1 p-2 bg-card border border-border rounded-lg hover:border-primary/50 hover:bg-primary/5 transition-all text-center">
                    <div className="w-7 h-7 bg-primary/20 text-primary rounded-full flex items-center justify-center text-xs font-bold">{u.avatar}</div>
                    <span className="text-xs text-muted-foreground leading-tight">{u.role.split(' ')[0]}<br/>{u.role.split(' ').slice(1).join(' ')}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
