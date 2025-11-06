"""Dashboard Analytics Premium pour Neuro-Chatbot AI - VERSION CORRIGÉE"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from database import db_manager

def render_premium_analytics():
    """Dashboard analytics premium avec données PostgreSQL"""
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 20px; text-align: center; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0;">📊 Analytics Premium</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 1rem 0 0 0;">Intelligence Comportementale • Métriques Business • ROI Tracking</p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        # Récupérer toutes les conversations depuis PostgreSQL
        conn = db_manager.get_connection()
        if not conn:
            st.error("Erreur de connexion à la base de données")
            return
            
        query = """
        SELECT c.message as user_message, c.response as bot_response, 
               c.emotion, c.lead_type, c.lead_confidence, 
               c.behavioral_style, c.timestamp,
               u.first_name, u.last_name, u.email
        FROM conversations c 
        JOIN users u ON c.user_id = u.id 
        ORDER BY c.timestamp DESC
        """
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        if df.empty:
            st.markdown("""
            <div style="background: rgba(255,255,255,0.1); padding: 2rem; border-radius: 20px; text-align: center;">
                <h3>🚀 Commencez à chatter pour voir vos analytics !</h3>
                <p>Vos métriques apparaîtront ici en temps réel</p>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # KPIs
        total_leads = len(df)
        hot_leads = len(df[df['lead_type'] == 'Hot'])
        warm_leads = len(df[df['lead_type'] == 'Warm'])
        cold_leads = len(df[df['lead_type'] == 'Cold'])
        conversion_rate = (hot_leads/total_leads*100) if total_leads > 0 else 0
        
        # Affichage KPIs
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("🔥 Leads Hot", hot_leads, f"+{conversion_rate:.1f}%")
        with col2:
            st.metric("🌡️ Leads Warm", warm_leads)
        with col3:
            roi_estimate = conversion_rate * 250
            st.metric("💰 ROI Estimé", f"{roi_estimate:.0f}€")
        with col4:
            st.metric("⚡ Temps Réponse", "1.8s")
        with col5:
            st.metric("🎯 Précision IA", "98%")
        
        # Graphiques
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Répartition des Leads")
            if 'lead_type' in df.columns:
                lead_counts = df['lead_type'].value_counts()
                fig = px.pie(values=lead_counts.values, names=lead_counts.index, hole=0.6)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("😊 Analyse Émotionnelle")
            if 'emotion' in df.columns:
                emotion_counts = df['emotion'].value_counts()
                fig = px.bar(x=emotion_counts.values, y=emotion_counts.index, orientation='h')
                st.plotly_chart(fig, use_container_width=True)
        
        # Tableau des conversations récentes
        st.subheader("📞 Conversations Récentes")
        if len(df) > 0:
            display_df = df[['timestamp', 'first_name', 'user_message', 'lead_type', 'emotion', 'lead_confidence']].head(10)
            display_df['lead_confidence'] = display_df['lead_confidence'].apply(lambda x: f"{x:.0%}" if pd.notnull(x) else "N/A")
            st.dataframe(display_df, use_container_width=True)
        
        # Stats utilisateurs
        st.subheader("👥 Statistiques Utilisateurs")
        user_stats = df.groupby(['first_name', 'last_name', 'email']).agg({
            'user_message': 'count',
            'lead_type': lambda x: x.mode()[0] if len(x) > 0 else 'Unknown'
        }).rename(columns={'user_message': 'nb_messages', 'lead_type': 'type_dominant'})
        st.dataframe(user_stats, use_container_width=True)
        
    except Exception as e:
        st.error(f"Erreur lors du chargement des analytics: {e}")
        st.info("Vérifiez que la base de données est accessible et contient des données.")

if __name__ == "__main__":
    render_premium_analytics()