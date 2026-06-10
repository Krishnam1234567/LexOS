import { Sparkles, Send, X, Trash2, Mic, MicOff, Zap } from 'lucide-react';
import { useState, useRef, useEffect, useCallback } from 'react';

const QUICK_PROMPTS = [
  'Summarize top legal risks',
  'What contracts expire soon?',
  'GDPR compliance status?',
  'Litigation cost forecast?',
];

/* ── Avatar Keyframe Styles ──────────────────────────────── */

const avatarStyles = `
@keyframes lexa-orbit {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
@keyframes lexa-glow {
  0%, 100% {
    box-shadow: 0 0 12px rgba(99,102,241,0.4),
                0 0 24px rgba(124,58,237,0.15),
                inset 0 0 8px rgba(99,102,241,0.1);
  }
  50% {
    box-shadow: 0 0 20px rgba(99,102,241,0.7),
                0 0 40px rgba(124,58,237,0.3),
                inset 0 0 12px rgba(99,102,241,0.2);
  }
}
@keyframes lexa-shimmer {
  0%   { left: -40%; }
  100% { left: 140%; }
}
@keyframes lexa-breathe {
  0%, 100% { transform: scale(1); opacity: 0.45; }
  50%      { transform: scale(1.8); opacity: 0; }
}
@keyframes lexa-float {
  0%, 100% { transform: translateY(0px); }
  50%      { transform: translateY(-2px); }
}
@keyframes user-ring-spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
@keyframes mic-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(239,68,68,0.5); }
  50%      { box-shadow: 0 0 0 8px rgba(239,68,68,0); }
}
@keyframes bubble-pop-in {
  0%   { opacity: 0; transform: translateY(8px) scale(0.9); }
  60%  { opacity: 1; transform: translateY(-2px) scale(1.02); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes bubble-dot {
  0%, 80%, 100% { opacity: 0.3; }
  40% { opacity: 1; }
}
@keyframes icon-ring-ping {
  0%   { transform: scale(1); opacity: 0.6; }
  100% { transform: scale(1.8); opacity: 0; }
}
`;

/* ── LexA Bot Avatar ─────────────────────────────────────── */

function LexAAvatar({ size = 'sm' }) {
  const isLg  = size === 'lg';
  const outer = isLg ? 44 : 32;
  const inner = isLg ? 36 : 26;
  const fontSize = isLg ? '15px' : '11px';

  return (
    <div
      className="relative flex-shrink-0"
      style={{
        width: outer, height: outer,
        animation: 'lexa-float 4s ease-in-out infinite',
      }}
    >
      {/* Breathing ripple (lg only) */}
      {isLg && (
        <div
          className="absolute rounded-full"
          style={{
            inset: -4,
            background: 'radial-gradient(circle, rgba(99,102,241,0.25) 0%, transparent 70%)',
            animation: 'lexa-breathe 3s ease-in-out infinite',
          }}
        />
      )}

      {/* Rotating orbital ring */}
      <div
        className="absolute inset-0 rounded-full"
        style={{
          background: 'conic-gradient(from 0deg, #6366F1, #8B5CF6, #D946EF, #EC4899, #6366F1)',
          animation: 'lexa-orbit 3.5s linear infinite',
        }}
      />

      {/* Inner avatar face */}
      <div
        className="absolute rounded-full flex items-center justify-center overflow-hidden"
        style={{
          top: (outer - inner) / 2,
          left: (outer - inner) / 2,
          width: inner,
          height: inner,
          background: 'linear-gradient(145deg, #1e1b4b 0%, #312e81 40%, #4f46e5 100%)',
          animation: 'lexa-glow 3s ease-in-out infinite',
        }}
      >
        {/* "L" Logo — custom styled letter */}
        <span
          style={{
            fontSize,
            fontWeight: 800,
            fontFamily: "'Inter', sans-serif",
            background: 'linear-gradient(135deg, #c7d2fe, #e9d5ff, #fce7f3)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            letterSpacing: '-0.5px',
            position: 'relative',
            zIndex: 2,
            filter: 'drop-shadow(0 0 4px rgba(199,210,254,0.5))',
          }}
        >
          L
        </span>

        {/* Shimmer streak */}
        <div
          className="absolute top-0 h-full"
          style={{
            width: '35%',
            background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent)',
            transform: 'skewX(-15deg)',
            animation: 'lexa-shimmer 2.8s ease-in-out infinite',
          }}
        />
      </div>
    </div>
  );
}

/* ── User Avatar ─────────────────────────────────────────── */

function UserAvatar({ initials, size = 'sm' }) {
  const isLg  = size === 'lg';
  const outer = isLg ? 44 : 32;
  const inner = isLg ? 36 : 26;
  const text  = isLg ? 'text-xs' : 'text-[10px]';

  return (
    <div
      className="relative flex-shrink-0 transition-transform duration-200 hover:scale-110 cursor-default"
      style={{ width: outer, height: outer }}
    >
      {/* Rotating gradient border */}
      <div
        className="absolute inset-0 rounded-full"
        style={{
          background: 'conic-gradient(from 0deg, #06b6d4, #3b82f6, #8b5cf6, #06b6d4)',
          animation: 'user-ring-spin 5s linear infinite',
        }}
      />

      {/* Inner circle */}
      <div
        className="absolute rounded-full flex items-center justify-center"
        style={{
          top: (outer - inner) / 2,
          left: (outer - inner) / 2,
          width: inner,
          height: inner,
          background: 'linear-gradient(145deg, #0f172a, #1e293b)',
          boxShadow: 'inset 0 1px 3px rgba(255,255,255,0.08), 0 0 8px rgba(59,130,246,0.25)',
        }}
      >
        <span className={`${text} font-bold text-white leading-none`}
              style={{ textShadow: '0 0 6px rgba(147,197,253,0.5)' }}>
          {initials}
        </span>
      </div>
    </div>
  );
}

/* ── Speech-to-Text Hook ─────────────────────────────────── */

function useSpeechToText() {
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState('');
  const recognitionRef = useRef(null);

  const isSupported = typeof window !== 'undefined' &&
    ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window);

  const startListening = useCallback(() => {
    if (!isSupported) return;

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = 'en-US';

    recognition.onresult = (event) => {
      let finalText = '';
      let interimText = '';
      for (let i = 0; i < event.results.length; i++) {
        if (event.results[i].isFinal) {
          finalText += event.results[i][0].transcript;
        } else {
          interimText += event.results[i][0].transcript;
        }
      }
      setTranscript(finalText || interimText);
    };

    recognition.onerror = () => {
      setIsListening(false);
    };

    recognition.onend = () => {
      setIsListening(false);
    };

    recognitionRef.current = recognition;
    recognition.start();
    setIsListening(true);
    setTranscript('');
  }, [isSupported]);

  const stopListening = useCallback(() => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }
    setIsListening(false);
  }, []);

  return { isListening, transcript, startListening, stopListening, isSupported };
}

/* ── Main Component ──────────────────────────────────────── */

export function AICopilot({ session }) {
  const [isOpen, setIsOpen] = useState(true);
  const [showBubble, setShowBubble] = useState(false);
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: "Hi! I'm LexA 👋\nYour AI-powered legal assistant. I can help you analyze contracts, check compliance, predict risks, and navigate your legal ops. How can I help you today?",
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const bottomRef = useRef(null);

  // Speech-to-text
  const { isListening, transcript, startListening, stopListening, isSupported } = useSpeechToText();

  // Auto-show speech bubble when panel is closed
  useEffect(() => {
    if (!isOpen) {
      const timer = setTimeout(() => setShowBubble(true), 1500);
      return () => clearTimeout(timer);
    } else {
      setShowBubble(false);
    }
  }, [isOpen]);

  // When speech transcript updates, put it in the input
  useEffect(() => {
    if (transcript) {
      setInput(transcript);
    }
  }, [transcript]);

  // When speech stops and we have text, auto-send
  useEffect(() => {
    if (!isListening && transcript.trim()) {
      // Small delay so user sees the text before it sends
      const timer = setTimeout(() => {
        handleSend(transcript.trim());
      }, 400);
      return () => clearTimeout(timer);
    }
  }, [isListening]);

  // User initials
  const userInitials =
    session?.avatar ||
    session?.name?.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2) ||
    'U';

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  const buildHistory = (msgs) =>
    msgs.slice(0, -0).map(m => ({ role: m.role === 'user' ? 'user' : 'assistant', content: m.content }));

  const handleSend = async (messageOverride) => {
    const userMessage = (messageOverride || input).trim();
    if (!userMessage) return;

    const updated = [...messages, { role: 'user', content: userMessage }];
    setMessages(updated);
    setInput('');
    setIsLoading(true);

    try {
      const apiBase = import.meta.env.VITE_API_URL || '/api';
      const response = await fetch(`${apiBase}/agents/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMessage,
          history: buildHistory(updated.slice(0, -1)),
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || `HTTP error ${response.status}`);
      }

      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (error) {
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: `⚠️ Backend not connected. Start the backend server to enable AI responses.\n\n${error.message}`,
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) {
    return (
      <div className="fixed bottom-6 right-6 z-50" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 10 }}>
        <style>{avatarStyles}</style>

        {/* Speech Bubble */}
        {showBubble && (
          <div
            style={{
              animation: 'bubble-pop-in 0.4s ease-out forwards',
              position: 'relative',
              maxWidth: 240,
            }}
          >
            <div
              style={{
                background: 'linear-gradient(145deg, #1e1b4b, #312e81)',
                border: '1px solid rgba(99,102,241,0.3)',
                borderRadius: 16,
                padding: '14px 16px',
                boxShadow: '0 8px 32px rgba(0,0,0,0.3), 0 0 16px rgba(99,102,241,0.2)',
              }}
            >
              {/* Close bubble */}
              <button
                onClick={(e) => { e.stopPropagation(); setShowBubble(false); }}
                className="absolute top-2 right-2 p-0.5 rounded-full hover:bg-white/10 transition-colors"
                style={{ lineHeight: 1 }}
              >
                <X className="w-3 h-3 text-white/50" />
              </button>

              <div className="flex items-start gap-2.5">
                {/* Mini LexA icon */}
                <div
                  className="flex-shrink-0 rounded-full flex items-center justify-center"
                  style={{
                    width: 28, height: 28,
                    background: 'linear-gradient(145deg, #4f46e5, #7c3aed)',
                    boxShadow: '0 0 8px rgba(99,102,241,0.4)',
                  }}
                >
                  <span style={{
                    fontSize: '12px', fontWeight: 800, fontFamily: "'Inter', sans-serif",
                    background: 'linear-gradient(135deg, #c7d2fe, #e9d5ff)',
                    WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
                  }}>L</span>
                </div>

                <div style={{ flex: 1 }}>
                  <p style={{ color: '#e0e7ff', fontSize: 13, fontWeight: 600, lineHeight: 1.3, margin: 0 }}>
                    Hi! I'm LexA 👋
                  </p>
                  <p style={{ color: '#a5b4fc', fontSize: 11.5, lineHeight: 1.4, marginTop: 3 }}>
                    Your AI legal assistant. Click to chat!
                  </p>
                </div>
              </div>
            </div>

            {/* Bubble tail / pointer */}
            <div style={{
              position: 'absolute',
              bottom: -6,
              right: 22,
              width: 12, height: 12,
              background: '#312e81',
              border: '1px solid rgba(99,102,241,0.3)',
              borderTop: 'none', borderLeft: 'none',
              transform: 'rotate(45deg)',
              borderRadius: '0 0 3px 0',
            }} />
          </div>
        )}

        {/* Floating Icon Button */}
        <button
          onClick={() => setIsOpen(true)}
          className="rounded-full shadow-lg hover:shadow-xl transition-all hover:scale-110 relative"
          style={{
            width: 56, height: 56,
            background: 'linear-gradient(145deg, #4f46e5, #7c3aed)',
            boxShadow: '0 4px 24px rgba(99,102,241,0.5)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
          }}
        >
          {/* Ping ring */}
          <div
            className="absolute inset-0 rounded-full"
            style={{
              border: '2px solid rgba(99,102,241,0.5)',
              animation: 'icon-ring-ping 2s ease-out infinite',
            }}
          />
          <span style={{
            fontSize: '22px', fontWeight: 800, fontFamily: "'Inter', sans-serif",
            background: 'linear-gradient(135deg, #c7d2fe, #e9d5ff)',
            WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent',
            position: 'relative', zIndex: 2,
          }}>L</span>
        </button>
      </div>
    );
  }

  return (
    <div className="w-96 h-full bg-card border-l border-border flex flex-col">
      <style>{avatarStyles}</style>

      {/* ── Header ───────────────────────────────────────── */}
      <div className="p-4 border-b border-border flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="relative">
            <LexAAvatar size="lg" />
            {/* Online dot */}
            <span
              className="absolute rounded-full border-2 border-card"
              style={{
                bottom: 1, right: 1,
                width: 10, height: 10,
                background: '#10B981',
                boxShadow: '0 0 8px rgba(16,185,129,0.7)',
                zIndex: 10,
              }}
            />
          </div>
          <div>
            <h3 className="font-semibold text-foreground text-sm leading-tight">
              LexA
              <span className="ml-1.5 text-[10px] font-medium px-1.5 py-0.5 rounded-full"
                    style={{
                      background: 'linear-gradient(135deg, rgba(99,102,241,0.15), rgba(139,92,246,0.15))',
                      color: '#8B5CF6',
                    }}>
                AI
              </span>
            </h3>
            <div className="flex items-center gap-1.5">
              <Zap className="w-3 h-3 text-accent" />
              <p className="text-xs text-muted-foreground">Powered by Gemini</p>
            </div>
          </div>
        </div>
        <div className="flex items-center gap-1">
          <button onClick={() => setMessages(messages.slice(0, 1))}
            className="p-1.5 hover:bg-muted/50 rounded transition-colors" title="Clear chat">
            <Trash2 className="w-3.5 h-3.5 text-muted-foreground" />
          </button>
          <button onClick={() => setIsOpen(false)} className="p-1.5 hover:bg-muted/50 rounded transition-colors">
            <X className="w-4 h-4 text-muted-foreground" />
          </button>
        </div>
      </div>

      {/* ── Messages ─────────────────────────────────────── */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, idx) => {
          const isUser = msg.role === 'user';
          return (
            <div
              key={idx}
              className={`flex items-start gap-2.5 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}
            >
              {isUser
                ? <UserAvatar initials={userInitials} />
                : <LexAAvatar />
              }
              <div
                className={`max-w-[76%] rounded-2xl px-3.5 py-2.5 text-sm leading-relaxed whitespace-pre-line ${
                  isUser
                    ? 'bg-primary text-primary-foreground rounded-tr-sm'
                    : 'bg-muted text-foreground rounded-tl-sm'
                }`}
                style={isUser ? { boxShadow: '0 2px 12px rgba(37,99,235,0.2)' } : {}}
              >
                {msg.content}
              </div>
            </div>
          );
        })}

        {/* Loading */}
        {isLoading && (
          <div className="flex items-start gap-2.5">
            <LexAAvatar />
            <div className="bg-muted rounded-2xl rounded-tl-sm px-4 py-3 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 bg-primary/60 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
              <span className="w-1.5 h-1.5 bg-primary/60 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
              <span className="w-1.5 h-1.5 bg-primary/60 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* ── Quick prompts ────────────────────────────────── */}
      {messages.length <= 1 && (
        <div className="px-4 pb-2">
          <p className="text-xs text-muted-foreground mb-2">Quick actions</p>
          <div className="grid grid-cols-2 gap-1.5">
            {QUICK_PROMPTS.map(p => (
              <button key={p} onClick={() => handleSend(p)}
                className="text-left text-xs px-2.5 py-2 bg-muted/50 hover:bg-muted rounded-lg text-muted-foreground hover:text-foreground transition-colors leading-tight">
                {p}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* ── Input ────────────────────────────────────────── */}
      <div className="p-4 border-t border-border">
        {/* Listening indicator */}
        {isListening && (
          <div className="flex items-center gap-2 mb-2 px-2">
            <div className="w-2 h-2 bg-destructive rounded-full" style={{ animation: 'mic-pulse 1.2s infinite' }} />
            <span className="text-xs text-destructive font-medium">Listening...</span>
            {transcript && <span className="text-xs text-muted-foreground truncate flex-1">{transcript}</span>}
          </div>
        )}
        <div className="flex gap-2 items-center">
          <UserAvatar initials={userInitials} />
          <input
            type="text"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyPress={e => e.key === 'Enter' && !isLoading && handleSend()}
            placeholder={isListening ? 'Speak now...' : 'Ask LexA anything...'}
            className="flex-1 px-3 py-2 bg-input-background border border-input rounded-lg text-sm focus:outline-none focus:ring-1 focus:ring-ring"
          />
          {/* Mic button */}
          {isSupported && (
            <button
              onClick={isListening ? stopListening : startListening}
              disabled={isLoading}
              className={`p-2 rounded-lg transition-all disabled:opacity-50 ${
                isListening
                  ? 'bg-destructive text-destructive-foreground'
                  : 'bg-muted hover:bg-muted/80 text-muted-foreground hover:text-foreground'
              }`}
              style={isListening ? { animation: 'mic-pulse 1.2s infinite' } : {}}
              title={isListening ? 'Stop recording' : 'Voice input'}
            >
              {isListening ? <MicOff className="w-4 h-4" /> : <Mic className="w-4 h-4" />}
            </button>
          )}
          <button onClick={() => handleSend()} disabled={isLoading || !input.trim()}
            className="p-2 bg-primary text-primary-foreground rounded-lg hover:opacity-90 transition-opacity disabled:opacity-50">
            <Send className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
}
