"""Styles et emojis animés professionnels pour le Neuro-Chatbot"""

def get_animated_emoji(style: str) -> str:
    """Retourne l'emoji animé selon le style détecté"""
    
    animated_emojis = {
        "pressé": '<i class="fas fa-bolt animated-bolt" style="color: #f59e0b;"></i>',
        "autoritaire": '<i class="fas fa-user-tie animated-shake" style="color: #ef4444;"></i>',
        "poli": '<i class="fas fa-smile animated-pulse" style="color: #10b981;"></i>',
        "réfléchi": '<i class="fas fa-brain animated-think" style="color: #8b5cf6;"></i>',
        "enthousiaste": '<i class="fas fa-star animated-sparkle" style="color: #f59e0b;"></i>',
        "énergique": '<i class="fas fa-fire animated-flame" style="color: #ef4444;"></i>',
        "concis": '<i class="fas fa-comment animated-fade" style="color: #06b6d4;"></i>',
        "cordial": '<i class="fas fa-hand-wave animated-wave" style="color: #10b981;"></i>',
        "approbateur": '<i class="fas fa-thumbs-up animated-bounce" style="color: #10b981;"></i>',
        "neutre": '<i class="fas fa-cog animated-rotate" style="color: #6b7280;"></i>'
    }
    
    return animated_emojis.get(style, '<i class="fas fa-robot" style="color: #6b7280;"></i>')

def get_style_prefix(style: str, emoji: str) -> str:
    """Retourne le préfixe stylé avec animations"""
    
    prefixes = {
        "pressé": f"<span class='style-indicator urgent'>Vous semblez pressé {emoji}</span>",
        "autoritaire": f"<span class='style-indicator authority'>Je sens votre détermination {emoji}</span>",
        "poli": f"<span class='style-indicator polite'>J'apprécie votre courtoisie {emoji}</span>",
        "réfléchi": f"<span class='style-indicator thoughtful'>Je vois que vous réfléchissez {emoji}</span>",
        "enthousiaste": f"<span class='style-indicator enthusiastic'>Votre enthousiasme me plaît {emoji}</span>",
        "énergique": f"<span class='style-indicator energetic'>J'aime votre énergie {emoji}</span>",
        "concis": f"<span class='style-indicator concise'>Je note votre approche directe {emoji}</span>",
        "cordial": f"<span class='style-indicator cordial'>Ravi de vous rencontrer {emoji}</span>",
        "approbateur": f"<span class='style-indicator approving'>Parfait, je vous remercie {emoji}</span>",
        "neutre": f"<span class='style-indicator neutral'>Je suis à votre écoute {emoji}</span>"
    }
    
    return prefixes.get(style, f"<span class='style-indicator'>Message reçu {emoji}</span>")

def get_advanced_css() -> str:
    """CSS avancé avec animations et glassmorphism"""
    
    return """
    <style>
    /* FontAwesome CDN */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
    
    /* Variables CSS modernes */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --success-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        --warning-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --danger-gradient: linear-gradient(135deg, #fc466b 0%, #3f5efb 100%);
        --glass-bg: rgba(255, 255, 255, 0.1);
        --glass-border: rgba(255, 255, 255, 0.2);
        --neon-glow: 0 0 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Animations FontAwesome */
    .animated-bolt {
        animation: bolt-flash 1.5s infinite;
        filter: drop-shadow(0 0 8px #f59e0b);
    }
    
    .animated-shake {
        animation: authority-shake 2s infinite;
        filter: drop-shadow(0 0 8px #ef4444);
    }
    
    .animated-pulse {
        animation: gentle-pulse 2s infinite;
        filter: drop-shadow(0 0 8px #10b981);
    }
    
    .animated-think {
        animation: brain-think 3s infinite;
        filter: drop-shadow(0 0 8px #8b5cf6);
    }
    
    .animated-sparkle {
        animation: sparkle-rotate 2s infinite;
        filter: drop-shadow(0 0 8px #f59e0b);
    }
    
    .animated-flame {
        animation: flame-flicker 1s infinite;
        filter: drop-shadow(0 0 8px #ef4444);
    }
    
    .animated-fade {
        animation: fade-pulse 2s infinite;
        filter: drop-shadow(0 0 8px #06b6d4);
    }
    
    .animated-wave {
        animation: hand-wave 2s infinite;
        filter: drop-shadow(0 0 8px #10b981);
    }
    
    .animated-bounce {
        animation: thumb-bounce 1.5s infinite;
        filter: drop-shadow(0 0 8px #10b981);
    }
    
    .animated-rotate {
        animation: cog-rotate 3s linear infinite;
        filter: drop-shadow(0 0 8px #6b7280);
    }
    
    /* Keyframes pour animations */
    @keyframes bolt-flash {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.2); }
    }
    
    @keyframes authority-shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-2px); }
        75% { transform: translateX(2px); }
    }
    
    @keyframes gentle-pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    
    @keyframes brain-think {
        0%, 100% { transform: scale(1) rotate(0deg); }
        33% { transform: scale(1.05) rotate(-5deg); }
        66% { transform: scale(1.05) rotate(5deg); }
    }
    
    @keyframes sparkle-rotate {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.2); }
        100% { transform: rotate(360deg) scale(1); }
    }
    
    @keyframes flame-flicker {
        0%, 100% { transform: scale(1) rotate(-2deg); }
        50% { transform: scale(1.1) rotate(2deg); }
    }
    
    @keyframes fade-pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }
    
    @keyframes hand-wave {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(20deg); }
        75% { transform: rotate(-10deg); }
    }
    
    @keyframes thumb-bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    @keyframes cog-rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* Style indicators avec glassmorphism */
    .style-indicator {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        font-weight: 600;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        margin: 4px 0;
    }
    
    .style-indicator.urgent {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(239, 68, 68, 0.2));
        color: #fbbf24;
        box-shadow: var(--neon-glow);
    }
    
    .style-indicator.authority {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(127, 29, 29, 0.2));
        color: #f87171;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.4);
    }
    
    .style-indicator.polite {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(5, 150, 105, 0.2));
        color: #34d399;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }
    
    .style-indicator.thoughtful {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(109, 40, 217, 0.2));
        color: #a78bfa;
        box-shadow: 0 0 20px rgba(139, 92, 246, 0.4);
    }
    
    .style-indicator.enthusiastic {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(251, 191, 36, 0.2));
        color: #fbbf24;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.4);
    }
    
    .style-indicator.energetic {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(220, 38, 127, 0.2));
        color: #f87171;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.4);
    }
    
    .style-indicator.concise {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.2), rgba(14, 165, 233, 0.2));
        color: #22d3ee;
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
    }
    
    .style-indicator.cordial {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(52, 211, 153, 0.2));
        color: #34d399;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }
    
    .style-indicator.approving {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(34, 197, 94, 0.2));
        color: #4ade80;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    }
    
    .style-indicator.neutral {
        background: linear-gradient(135deg, rgba(107, 114, 128, 0.2), rgba(75, 85, 99, 0.2));
        color: #9ca3af;
        box-shadow: 0 0 20px rgba(107, 114, 128, 0.3);
    }
    
    /* Hover effects */
    .style-indicator:hover {
        transform: translateY(-2px) scale(1.05);
        filter: brightness(1.2);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .style-indicator {
            padding: 6px 12px;
            font-size: 0.9rem;
        }
    }
    </style>
    """