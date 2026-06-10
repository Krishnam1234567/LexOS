import { Sparkles, Send, X, Bot, User } from 'lucide-react';
import { useState } from 'react';

export function AICopilot() {
  const [isOpen, setIsOpen] = useState(true);
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: 'Hello! I\'m your Legal AI Assistant. I can help you analyze contracts, check compliance, predict litigation risk, and navigate your legal operations.'
    }
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim()) return;

    setMessages([...messages, { role: 'user', content: input }]);
    setInput('');

    setTimeout(() => {
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: 'I understand your query. Based on your legal digital twin, I recommend reviewing the contract clauses related to jurisdiction and ensuring compliance with the new GDPR amendments.'
      }]);
    }, 1000);
  };

  if (!isOpen) {
    return (
      <button
        onClick={() => setIsOpen(true)}
        className="fixed bottom-6 right-6 p-4 bg-primary text-primary-foreground rounded-full shadow-lg hover:shadow-xl transition-shadow"
      >
        <Sparkles className="w-6 h-6" />
      </button>
    );
  }

  return (
    <div className="w-96 h-full bg-card border-l border-border flex flex-col">
      <div className="p-4 border-b border-border flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="relative">
            <div className="w-8 h-8 rounded-full bg-gradient-to-br from-primary to-chart-5 flex items-center justify-center shadow-md"
                 style={{ boxShadow: '0 0 12px rgba(37, 99, 235, 0.4)' }}>
              <Bot className="w-4 h-4 text-white" />
            </div>
            <span className="absolute bottom-0 right-0 w-2.5 h-2.5 bg-accent rounded-full border-2 border-card"></span>
          </div>
          <div>
            <h3 className="font-semibold text-foreground text-sm leading-tight">AI Legal Copilot</h3>
            <span className="text-xs text-accent font-medium">Online</span>
          </div>
        </div>
        <button
          onClick={() => setIsOpen(false)}
          className="p-1 hover:bg-accent/10 rounded transition-colors"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`flex items-end gap-2 ${msg.role === 'user' ? 'flex-row-reverse' : 'flex-row'}`}
          >
            {/* Avatar */}
            <div className="flex-shrink-0">
              {msg.role === 'assistant' ? (
                <div className="w-7 h-7 rounded-full bg-gradient-to-br from-primary to-chart-5 flex items-center justify-center shadow-sm"
                     style={{ boxShadow: '0 0 8px rgba(37, 99, 235, 0.3)' }}>
                  <Bot className="w-3.5 h-3.5 text-white" />
                </div>
              ) : (
                <div className="w-7 h-7 rounded-full bg-gradient-to-br from-secondary to-muted-foreground flex items-center justify-center shadow-sm">
                  <User className="w-3.5 h-3.5 text-white" />
                </div>
              )}
            </div>
            {/* Message bubble */}
            <div
              className={`max-w-[75%] rounded-2xl p-3 text-sm ${
                msg.role === 'user'
                  ? 'bg-primary text-primary-foreground rounded-br-sm'
                  : 'bg-muted text-foreground rounded-bl-sm'
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
      </div>

      <div className="p-4 border-t border-border">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            placeholder="Ask about contracts, compliance..."
            className="flex-1 px-3 py-2 bg-input-background border border-input rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-ring"
          />
          <button
            onClick={handleSend}
            className="p-2 bg-primary text-primary-foreground rounded-lg hover:opacity-90 transition-opacity"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
