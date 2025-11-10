"""Interface SaaS professionnelle pour Neuro-Chatbot AI"""

import streamlit as st
from ultimate_orchestrator import orchestrator
from database import db_manager
from premium_analytics import render_premium_analytics
from enhanced_styles import get_advanced_css
from saas_styles import get_saas_chat_css
import re
import uuid
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="🧠 Neuro-Chatbot AI - Professional SaaS",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_professional_css():
    """CSS professionnel ultra-moderne pour interface SaaS"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
    
    /* Variables globales */
    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --secondary: #8b5cf6;
        --accent: #06b6d4;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --dark: #0f172a;
        --dark-light: #1e293b;
        --glass: rgba(255, 255, 255, 0.1);
        --glass-border: rgba(255, 255, 255, 0.2);
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        --shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    }
    
    /* Reset et base */
    * { font-family: 'Inter', sans-serif; }
    
    .stApp {
        background: linear-gradient(135deg, var(--dark) 0%, var(--dark-light) 100%);
        color: var(--text-primary);
    }
    
    /* Header professionnel */
    .pro-header {
        background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: var(--shadow-xl);
        position: relative;
        overflow: hidden;
    }
    
    .pro-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(45deg, #fff, #e2e8f0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
        z-index: 1;
    }
    
    .pro-header p {
        font-size: 1.2rem;
        margin: 1rem 0 0 0;
        opacity: 0.9;
        position: relative;
        z-index: 1;
    }
    
    /* Cards professionnelles */
    .pro-card {
        background: var(--glass);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .pro-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
    }
    
    .pro-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-xl);
        border-color: var(--primary);
    }
    
    /* Chat container moderne */
    .chat-container {
        background: var(--glass);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 25px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-lg);
        min-height: 600px;
        max-height: 800px;
        overflow-y: auto;
    }
    
    /* Messages de conversation */
    .conversation-history {
        max-height: 400px;
        overflow-y: auto;
        margin-bottom: 2rem;
        padding: 1rem;
        background: rgba(0, 0, 0, 0.1);
        border-radius: 15px;
        border: 1px solid var(--glass-border);
    }
    
    .message-user {
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 25px 25px 8px 25px;
        margin: 1rem 0 1rem 20%;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        animation: slideInRight 0.3s ease;
        position: relative;
    }
    
    .message-bot {
        background: var(--glass);
        backdrop-filter: blur(10px);
        border: 1px solid var(--glass-border);
        color: var(--text-primary);
        padding: 1rem 1.5rem;
        border-radius: 25px 25px 25px 8px;
        margin: 1rem 20% 1rem 0;
        box-shadow: var(--shadow-lg);
        animation: slideInLeft 0.3s ease;
        position: relative;
    }
    
    .message-timestamp {
        font-size: 0.8rem;
        color: var(--text-secondary);
        margin-top: 0.5rem;
        opacity: 0.7;
    }
    
    /* Métriques modernes */
    .metric-pro {
        background: var(--glass);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-pro::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--primary);
    }
    
    .metric-pro:hover {
        transform: scale(1.05);
        box-shadow: var(--shadow-xl);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Formulaires modernes */
    .stTextInput > div > div > input {
        background: var(--glass) !important;
        backdrop-filter: blur(10px);
        border: 2px solid var(--glass-border) !important;
        border-radius: 15px !important;
        color: var(--text-primary) !important;
        padding: 1rem 1.5rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* Boutons professionnels */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), var(--primary-dark)) !important;
        border: none !important;
        border-radius: 15px !important;
        color: white !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4) !important;
    }
    
    /* Status indicators */
    .status-online {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: var(--success);
        border-radius: 50%;
        margin-right: 0.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
        100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
    
    /* Animations */
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeInUp {
        from { transform: translateY(30px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .pro-header h1 { font-size: 2rem; }
        .message-user, .message-bot { margin-left: 5%; margin-right: 5%; }
        .pro-card { padding: 1.5rem; }
    }
    </style>
    """

def validate_email(email):
    """Valide le format email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def auth_section():
    """Section d'authentification moderne"""
    st.markdown("""
    <div class="pro-header fade-in-up">
        <h1><i class="fas fa-brain"></i> Neuro-Chatbot AI</h1>
        <p><span class="status-online"></span>Intelligence Émotionnelle • Analyse Comportementale • Classification Leads</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="pro-card fade-in-up">', unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔐 Connexion", "📝 Inscription"])
        
        with tab1:
            with st.form("login_form"):
                st.markdown("### Connexion")
                email = st.text_input("📧 Email", placeholder="votre@email.com")
                submitted = st.form_submit_button("🚀 Se connecter", use_container_width=True)
                
                if submitted and email:
                    if validate_email(email):
                        user = db_manager.get_user_by_email(email)
                        if user:
                            st.session_state.user = user
                            st.session_state.conversation_history = []
                            st.success(f"Bienvenue {user['first_name']} ! 👋")
                            st.rerun()
                        else:
                            st.error("Email non trouvé. Veuillez vous inscrire.")
                    else:
                        st.error("Format email invalide")
        
        with tab2:
            with st.form("register_form"):
                st.markdown("### Inscription")
                col1, col2 = st.columns(2)
                with col1:
                    first_name = st.text_input("👤 Prénom", placeholder="Jean")
                with col2:
                    last_name = st.text_input("👤 Nom", placeholder="Dupont")
                
                email = st.text_input("📧 Email", placeholder="jean.dupont@email.com")
                phone = st.text_input("📞 Téléphone", placeholder="+33 6 12 34 56 78")
                
                submitted = st.form_submit_button("✨ Créer mon compte", use_container_width=True)
                
                if submitted and first_name and last_name and email:
                    if validate_email(email):
                        result = db_manager.save_user(first_name, last_name, phone, email)
                        if result and result != "EMAIL_EXISTS":
                            user = {
                                'id': result,
                                'first_name': first_name,
                                'last_name': last_name,
                                'phone': phone,
                                'email': email
                            }
                            st.session_state.user = user
                            st.session_state.conversation_history = []
                            st.success(f"Compte créé ! Bienvenue {first_name} ! 🎉")
                            st.rerun()
                        else:
                            st.error("Email déjà utilisé")
                    else:
                        st.error("Email invalide")
        
        st.markdown('</div>', unsafe_allow_html=True)

def main_app():
    """Application principale professionnelle"""
    user = st.session_state.user
    
    # Header utilisateur
    st.markdown(f"""
    <div class="pro-header fade-in-up">
        <h1>👋 Bienvenue {user['first_name']} {user['last_name']}</h1>
        <p><span class="status-online"></span>Votre assistant IA personnel est opérationnel</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar moderne
    with st.sidebar:
        st.markdown(f"""
        <div class="pro-card">
            <h4 style="color: var(--primary);"><i class="fas fa-user-circle"></i> Profil</h4>
            <p><strong>Nom:</strong> {user['first_name']} {user['last_name']}</p>
            <p><strong>Email:</strong> {user['email']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Déconnexion", use_container_width=True):
            del st.session_state.user
            if 'conversation_history' in st.session_state:
                del st.session_state.conversation_history
            st.rerun()
        
        st.markdown("---")
        
        page = st.radio(
            "Navigation",
            ["💬 Chat Intelligence", "📊 Analytics", "📈 Mes Stats"],
            label_visibility="collapsed"
        )
    
    if page == "💬 Chat Intelligence":
        chat_interface(user)
    elif page == "📊 Analytics":
        render_premium_analytics()
    else:
        user_stats(user)

def chat_interface(user):
    """Interface de chat professionnelle avec historique de conversation"""
    
    # Initialiser l'historique de conversation
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    

    
    # Interface de chat professionnelle
    st.markdown("""
    <div class="saas-chat-interface">
        <div class="chat-header">
            <div class="chat-title">
                <i class="fas fa-robot"></i>
                <span>Neuro Assistant</span>
                <div class="status-indicator online"></div>
            </div>
            <div class="chat-subtitle">Intelligence Émotionnelle & Analyse Comportementale</div>
        </div>
        <div class="chat-messages">
    """, unsafe_allow_html=True)
    
    # Affichage de l'historique de conversation
    if st.session_state.conversation_history:
        for msg in st.session_state.conversation_history:
            timestamp = msg.get('timestamp', '')
            st.markdown(f"""
            <div class="message-bubble user-message">
                <div class="message-content">{msg["user_message"]}</div>
                <div class="message-time">{timestamp}</div>
            </div>
            <div class="message-bubble bot-message">
                <div class="message-content">{msg["bot_response"]}</div>
                <div class="message-meta">
                    <span class="lead-badge {msg.get("lead_type", "unknown").lower()}">{msg.get("lead_type", "Unknown")}</span>
                    <span class="style-badge">{msg.get("style", "neutre")}</span>
                    <span class="message-time">{timestamp}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Bouton pour effacer l'historique
        if st.button("🗑️ Nouvelle conversation", key="clear_history"):
            st.session_state.conversation_history = []
            st.rerun()
    else:
        st.markdown("""
        <div class="welcome-message">
            <div class="welcome-icon">👋</div>
            <h3>Bienvenue ! Comment puis-je vous aider ?</h3>
            <p>Je suis votre assistant IA spécialisé en marketing digital. Posez-moi vos questions !</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Formulaire de chat professionnel
    st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([6, 1])
        
        with col1:
            user_input = st.text_input(
                "Message",
                placeholder="💬 Tapez votre message ici...",
                label_visibility="collapsed",
                key="chat_input"
            )
        
        with col2:
            submitted = st.form_submit_button("🚀", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if submitted and user_input.strip():
            
        with st.spinner("🧠 Analyse en cours..."):
            result = orchestrator.process_message(user_input)
            
            # Ajouter à l'historique de conversation
            conversation_entry = {
                'id': str(uuid.uuid4()),
                'user_message': user_input,
                'bot_response': result["bot_response"],
                'emotion': result["emotion_data"].get("emotion"),
                'lead_type': result["lead_data"].get("lead_type"),
                'confidence': result["lead_data"].get("confidence"),
                'style': result.get("style_data", {}).get("style"),
                'timestamp': datetime.now().strftime("%H:%M:%S")
            }
            
            st.session_state.conversation_history.append(conversation_entry)
            
            # Limiter l'historique à 10 messages
            if len(st.session_state.conversation_history) > 10:
                st.session_state.conversation_history = st.session_state.conversation_history[-10:]
            
            # Sauvegarde en base de données
            db_manager.save_conversation(
                user['id'], user_input, result["bot_response"],
                result["emotion_data"].get("emotion"),
                result["lead_data"].get("lead_type"),
                result["lead_data"].get("confidence"),
                result.get("style_data", {}).get("style")
            )
            
            # Affichage du nouveau message
            st.markdown(f"""
            <div class="message-bubble user-message new-message">
                <div class="message-content">{user_input}</div>
                <div class="message-time">{conversation_entry["timestamp"]}</div>
            </div>
            <div class="message-bubble bot-message new-message">
                <div class="message-content">{result["bot_response"]}</div>
                <div class="message-meta">
                    <span class="lead-badge {result["lead_data"].get("lead_type", "unknown").lower()}">{result["lead_data"].get("lead_type")}</span>
                    <span class="style-badge">{result.get("style_data", {}).get("style")}</span>
                    <span class="message-time">{conversation_entry["timestamp"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Métriques discrètes
            confidence = result["lead_data"].get("confidence", 0)
            st.markdown(f"""
            <div class="analysis-summary">
                <div class="analysis-item">
                    <span class="analysis-label">Émotion:</span>
                    <span class="analysis-value">{result["emotion_data"].get("emotion", "neutral")}</span>
                </div>
                <div class="analysis-item">
                    <span class="analysis-label">Confiance:</span>
                    <span class="analysis-value">{confidence:.0%}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def user_stats(user):
    """Statistiques utilisateur"""
    st.markdown('<div class="pro-card fade-in-up">', unsafe_allow_html=True)
    st.markdown("### 📈 Vos Statistiques")
    
    conversations = db_manager.get_user_conversations(user['id'], 100)
    
    if conversations:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-pro">
                <div class="metric-label">Conversations</div>
                <div class="metric-value">{len(conversations)}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            hot_leads = len([c for c in conversations if c.get('lead_type') == 'Hot'])
            st.markdown(f"""
            <div class="metric-pro">
                <div class="metric-label">Leads Hot</div>
                <div class="metric-value">{hot_leads}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            warm_leads = len([c for c in conversations if c.get('lead_type') == 'Warm'])
            st.markdown(f"""
            <div class="metric-pro">
                <div class="metric-label">Leads Warm</div>
                <div class="metric-value">{warm_leads}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            avg_confidence = sum([c.get('confidence', 0) for c in conversations]) / len(conversations) if conversations else 0
            st.markdown(f"""
            <div class="metric-pro">
                <div class="metric-label">Confiance Moy.</div>
                <div class="metric-value">{avg_confidence:.0%}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Aucune conversation enregistrée")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Application principale
def main():
    # CSS professionnel
    st.markdown(get_professional_css(), unsafe_allow_html=True)
    st.markdown(get_advanced_css(), unsafe_allow_html=True)
    st.markdown(get_saas_chat_css(), unsafe_allow_html=True)
    
    # Initialisation DB
    if 'db_initialized' not in st.session_state:
        if db_manager.create_tables():
            st.session_state.db_initialized = True
        else:
            st.error("Erreur base de données")
            st.stop()
    
    # Logique d'authentification
    if "user" not in st.session_state:
        auth_section()
    else:
        main_app()

if __name__ == "__main__":
    main()