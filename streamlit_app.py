"""Interface utilisateur professionnelle pour Neuro-Chatbot AI"""

import streamlit as st
from ultimate_orchestrator import orchestrator
from database import db_manager
# from enhanced_dashboard import render_dashboard  # Not needed for this version
from premium_analytics import render_premium_analytics
from enhanced_styles import get_advanced_css
import re

# Configuration de la page
st.set_page_config(
    page_title="🧠 Neuro-Chatbot AI - Professional",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_professional_css():
    """CSS professionnel ultra-moderne"""
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
    
    .pro-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="50" cy="50" r="1" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
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
    
    /* Chat interface moderne */
    .chat-container {
        background: var(--glass);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 25px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: var(--shadow-lg);
        min-height: 500px;
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
    
    /* Sidebar professionnelle */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--dark-light) 0%, var(--dark) 100%) !important;
        border-right: 1px solid var(--glass-border) !important;
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
    
    /* Boutons de défi */
    .stButton > button {
        height: auto !important;
        white-space: pre-line !important;
        text-align: center !important;
        padding: 1rem !important;
        min-height: 80px !important;
        font-size: 0.9rem !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .pro-header h1 { font-size: 2rem; }
        .message-user, .message-bot { margin-left: 5%; margin-right: 5%; }
        .pro-card { padding: 1.5rem; }
        .stButton > button { min-height: 70px !important; font-size: 0.8rem !important; }
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
    """Interface de chat professionnelle"""
    
    # Défis IA interactifs
    st.markdown('<div class="pro-card fade-in-up">', unsafe_allow_html=True)
    st.markdown("### 🎯 Défiez l'IA ! Testez sa capacité d'adaptation")
    
    challenges = [
        {"emoji": "🔥", "title": "Mode Urgence", "msg": "JE VEUX ACHETER MAINTENANT !", "desc": "Testez la réaction à l'urgence"},
        {"emoji": "😊", "title": "Mode Poli", "msg": "Bonjour, pourriez-vous m'aider s'il vous plaît ?", "desc": "Voyez l'adaptation à la politesse"},
        {"emoji": "😠", "title": "Mode Boss", "msg": "Je veux ça maintenant ! Donnez-moi le prix !", "desc": "Testez la gestion de l'autorité"},
        {"emoji": "🤔", "title": "Mode Hésitant", "msg": "Je pense que ça pourrait m'intéresser...", "desc": "Observez la patience de l'IA"},
        {"emoji": "❄️", "title": "Mode Rejet", "msg": "Non merci, pas intéressé du tout", "desc": "Défi : convaincre l'inconvaincu"}
    ]
    
    cols = st.columns(len(challenges))
    for i, challenge in enumerate(challenges):
        with cols[i]:
            if st.button(f"{challenge['emoji']} **{challenge['title']}**\n{challenge['desc']}", key=f"challenge_{i}"):
                st.session_state.test_message = challenge['msg']
                st.session_state.challenge_mode = challenge['title']
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interface de chat
    st.markdown('<div class="chat-container fade-in-up">', unsafe_allow_html=True)
    
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        
        with col1:
            default_msg = st.session_state.get("test_message", "")
            challenge_mode = st.session_state.get("challenge_mode", "")
            placeholder = f"🎯 Défi {challenge_mode} activé ! Ou tapez votre message..." if challenge_mode else "💭 Tapez votre message ou choisissez un défi..."
            
            user_input = st.text_input(
                "Message",
                value=default_msg,
                placeholder=placeholder,
                label_visibility="collapsed"
            )
            # Garder les valeurs pour l'envoi
            if "test_message" in st.session_state and not user_input:
                pass  # Garder le message jusqu'à l'envoi
        
        with col2:
            submitted = st.form_submit_button("🚀 Envoyer", use_container_width=True)
    
    if submitted and user_input.strip():
        # Nettoyer les variables de session après envoi
        if "test_message" in st.session_state:
            del st.session_state.test_message
        if "challenge_mode" in st.session_state:
            del st.session_state.challenge_mode
            
        with st.spinner("🧠 Analyse en cours..."):
            result = orchestrator.process_message(user_input)
            
            # Sauvegarde
            db_manager.save_conversation(
                user['id'], user_input, result["bot_response"],
                result["emotion_data"].get("emotion"),
                result["lead_data"].get("lead_type"),
                result["lead_data"].get("confidence"),
                result.get("style_data", {}).get("style")
            )
            
            # Affichage des messages
            st.markdown(f'<div class="message-user">👤 {user_input}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="message-bot">🤖 {result["bot_response"]}</div>', unsafe_allow_html=True)
            
            # Métriques
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="metric-pro">
                    <div class="metric-label">Émotion</div>
                    <div class="metric-value">😊</div>
                    <div style="color: var(--text-secondary);">{result["emotion_data"].get("emotion", "neutral")}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-pro">
                    <div class="metric-label">Lead Type</div>
                    <div class="metric-value">🎯</div>
                    <div style="color: var(--text-secondary);">{result["lead_data"].get("lead_type", "Unknown")}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                confidence = result["lead_data"].get("confidence", 0)
                st.markdown(f"""
                <div class="metric-pro">
                    <div class="metric-label">Confiance</div>
                    <div class="metric-value">{confidence:.0%}</div>
                    <div style="color: var(--text-secondary);">Précision</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                style = result.get("style_data", {}).get("style", "neutre")
                st.markdown(f"""
                <div class="metric-pro">
                    <div class="metric-label">Style</div>
                    <div class="metric-value">🎭</div>
                    <div style="color: var(--text-secondary);">{style}</div>
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
    else:
        st.info("Aucune conversation enregistrée")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Application principale
def main():
    # CSS professionnel
    st.markdown(get_professional_css(), unsafe_allow_html=True)
    st.markdown(get_advanced_css(), unsafe_allow_html=True)
    
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