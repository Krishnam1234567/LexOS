import {
  LayoutDashboard,
  Network,
  FileText,
  Shield,
  Scale,
  Globe,
  Users,
  Bot,
  GitBranch,
  BarChart3,
  Plug,
  Lock,
  Settings
} from 'lucide-react';

export function Sidebar({ activeScreen, onNavigate, role = 'Authenticated User' }) {
  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'digital-twin', label: 'Legal Digital Twin', icon: Network },
    { id: 'contracts', label: 'Contracts', icon: FileText },
    { id: 'compliance', label: 'Compliance', icon: Shield },
    { id: 'litigation', label: 'Litigation', icon: Scale },
    { id: 'expansion', label: 'Global Expansion', icon: Globe },
    { id: 'governance', label: 'Governance', icon: Users },
    { id: 'agents', label: 'AI Agents', icon: Bot },
    { id: 'knowledge', label: 'Knowledge Graph', icon: GitBranch },
    { id: 'analytics', label: 'Analytics', icon: BarChart3 },
    { id: 'integrations', label: 'Integrations', icon: Plug },
    { id: 'security', label: 'Security', icon: Lock },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  const getVisibleItems = () => {
    if (role === 'System Administrator') {
      return navItems; // Sees everything
    }
    if (role === 'General Counsel') {
      const allowed = ['dashboard', 'digital-twin', 'contracts', 'compliance', 'litigation', 'expansion', 'governance', 'analytics', 'agents', 'knowledge'];
      return navItems.filter(item => allowed.includes(item.id));
    }
    if (role === 'Senior Legal Counsel') {
      const allowed = ['dashboard', 'contracts', 'litigation', 'compliance', 'agents', 'knowledge'];
      return navItems.filter(item => allowed.includes(item.id));
    }
    // Default fallback for generic Google Auth users
    const allowed = ['dashboard', 'contracts', 'compliance', 'agents', 'knowledge'];
    return navItems.filter(item => allowed.includes(item.id));
  };

  const visibleNavItems = getVisibleItems();

  return (
    <div className="w-64 h-full bg-sidebar border-r border-sidebar-border flex flex-col">
      <div className="p-6 border-b border-sidebar-border">
        <h1 className="text-xl font-semibold text-sidebar-foreground">LexOS</h1>
        <p className="text-xs text-sidebar-foreground/60 mt-1">Legal Operating System</p>
      </div>

      <nav className="flex-1 overflow-y-auto p-3">
        {visibleNavItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeScreen === item.id;

          return (
            <button
              key={item.id}
              onClick={() => onNavigate(item.id)}
              className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition-colors mb-1 ${
                isActive
                  ? 'bg-sidebar-primary text-sidebar-primary-foreground'
                  : 'text-sidebar-foreground/80 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground'
              }`}
            >
              <Icon className="w-4 h-4" />
              <span>{item.label}</span>
            </button>
          );
        })}
      </nav>
    </div>
  );
}
