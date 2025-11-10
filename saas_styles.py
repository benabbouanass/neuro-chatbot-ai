"""Styles CSS professionnels pour interface SaaS moderne"""

def get_saas_chat_css():
    """CSS pour interface de chat SaaS professionnelle"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    
    /* Variables SaaS */
    :root {
        --primary: #6366f1;
        --primary-light: #818cf8;
        --secondary: #f1f5f9;
        --accent: #10b981;
        --danger: #ef4444;
        --warning: #f59e0b;
        --dark: #0f172a;
        --dark-light: #1e293b;
        --gray-50: #f8fafc;
        --gray-100: #f1f5f9;
        --gray-200: #e2e8f0;
        --gray-300: #cbd5e1;
        --gray-400: #94a3b8;
        --gray-500: #64748b;
        --gray-600: #475569;
        --gray-700: #334155;
        --gray-800: #1e293b;
        --gray-900: #0f172a;
        --white: #ffffff;
        --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    
    /* Interface de chat SaaS */
    .saas-chat-interface {
        background: var(--white);
        border-radius: 16px;
        box-shadow: var(--shadow-xl);
        overflow: hidden;
        margin: 2rem 0;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        border: 1px solid var(--gray-200);
    }
    
    /* Header du chat */
    .chat-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
        padding: 1.5rem 2rem;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .chat-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.1;
    }
    
    .chat-title {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 1.25rem;
        font-weight: 600;
        position: relative;
        z-index: 1;
    }
    
    .chat-title i {
        font-size: 1.5rem;
    }
    
    .status-indicator {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-left: auto;
    }
    
    .status-indicator.online {
        background: var(--accent);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
        100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
    
    .chat-subtitle {
        font-size: 0.875rem;
        opacity: 0.9;
        margin-top: 0.25rem;
        position: relative;
        z-index: 1;
    }
    
    /* Messages */
    .chat-messages {
        padding: 1.5rem;
        min-height: 400px;
        max-height: 600px;
        overflow-y: auto;
        background: var(--gray-50);
    }
    
    .message-bubble {
        margin-bottom: 1rem;
        animation: slideIn 0.3s ease-out;
    }
    
    .message-bubble.new-message {
        animation: slideInBounce 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideInBounce {
        0% { opacity: 0; transform: translateY(20px) scale(0.95); }
        60% { opacity: 1; transform: translateY(-2px) scale(1.02); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }
    
    .user-message {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        margin-left: 20%;
    }
    
    .user-message .message-content {
        background: var(--primary);
        color: white;
        padding: 0.875rem 1.25rem;
        border-radius: 18px 18px 4px 18px;
        max-width: 100%;
        word-wrap: break-word;
        font-size: 0.95rem;
        line-height: 1.4;
        box-shadow: var(--shadow);
    }
    
    .bot-message {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-right: 20%;
    }
    
    .bot-message .message-content {
        background: var(--white);
        color: var(--gray-800);
        padding: 0.875rem 1.25rem;
        border-radius: 18px 18px 18px 4px;
        max-width: 100%;
        word-wrap: break-word;
        font-size: 0.95rem;
        line-height: 1.4;
        box-shadow: var(--shadow);
        border: 1px solid var(--gray-200);
    }
    
    .message-time {
        font-size: 0.75rem;
        color: var(--gray-400);
        margin-top: 0.25rem;
        padding: 0 0.5rem;
    }
    
    .message-meta {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-top: 0.5rem;
        padding: 0 0.5rem;
    }
    
    .lead-badge, .style-badge {
        font-size: 0.7rem;
        padding: 0.2rem 0.5rem;
        border-radius: 12px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.025em;
    }
    
    .lead-badge.hot { background: #fef2f2; color: #dc2626; }
    .lead-badge.warm { background: #fef3c7; color: #d97706; }
    .lead-badge.interested { background: #eff6ff; color: #2563eb; }
    .lead-badge.cold { background: #f3f4f6; color: #6b7280; }
    
    .style-badge {
        background: var(--gray-100);
        color: var(--gray-600);
    }
    
    /* Message de bienvenue */
    .welcome-message {
        text-align: center;
        padding: 3rem 2rem;
        color: var(--gray-600);
    }
    
    .welcome-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .welcome-message h3 {
        color: var(--gray-800);
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .welcome-message p {
        color: var(--gray-500);
        font-size: 0.95rem;
    }
    
    /* Input de chat */
    .chat-input-container {
        padding: 1.5rem;
        background: var(--white);
        border-top: 1px solid var(--gray-200);
    }
    
    .stTextInput > div > div > input {
        background: var(--gray-50) !important;
        border: 2px solid var(--gray-200) !important;
        border-radius: 24px !important;
        padding: 0.875rem 1.25rem !important;
        font-size: 0.95rem !important;
        color: var(--gray-800) !important;
        transition: all 0.2s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
        background: var(--white) !important;
    }
    
    .stButton > button {
        background: var(--primary) !important;
        border: none !important;
        border-radius: 20px !important;
        color: white !important;
        padding: 0.875rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.2s ease !important;
        box-shadow: var(--shadow) !important;
        height: 48px !important;
    }
    
    .stButton > button:hover {
        background: var(--primary-light) !important;
        transform: translateY(-1px) !important;
        box-shadow: var(--shadow-md) !important;
    }
    
    /* Analyse discrète */
    .analysis-summary {
        display: flex;
        gap: 1rem;
        margin-top: 0.5rem;
        padding: 0 0.5rem;
        font-size: 0.8rem;
    }
    
    .analysis-item {
        display: flex;
        gap: 0.25rem;
    }
    
    .analysis-label {
        color: var(--gray-400);
        font-weight: 500;
    }
    
    .analysis-value {
        color: var(--gray-600);
        font-weight: 600;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .saas-chat-interface {
            margin: 1rem;
            border-radius: 12px;
        }
        
        .user-message, .bot-message {
            margin-left: 5%;
            margin-right: 5%;
        }
        
        .chat-header {
            padding: 1rem 1.5rem;
        }
        
        .chat-messages {
            padding: 1rem;
        }
        
        .chat-input-container {
            padding: 1rem;
        }
    }
    </style>
    """