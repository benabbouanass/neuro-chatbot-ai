"""Test de connexion PostgreSQL pour vérifier la configuration"""

import streamlit as st
from database import db_manager

def test_database_connection():
    """Teste la connexion à la base de données"""
    
    st.markdown("## 🔍 Test de Connexion PostgreSQL")
    
    try:
        # Test de connexion
        conn = db_manager.get_connection()
        if conn:
            st.success("✅ Connexion PostgreSQL réussie !")
            
            # Test des tables
            cur = conn.cursor()
            
            # Vérifier table users
            cur.execute("SELECT COUNT(*) FROM users")
            user_count = cur.fetchone()[0]
            st.info(f"👥 Table users : {user_count} utilisateurs")
            
            # Vérifier table conversations
            cur.execute("SELECT COUNT(*) FROM conversations")
            conv_count = cur.fetchone()[0]
            st.info(f"💬 Table conversations : {conv_count} messages")
            
            cur.close()
            conn.close()
            
            st.success("🎯 Base de données opérationnelle !")
            
        else:
            st.error("❌ Impossible de se connecter à PostgreSQL")
            
    except Exception as e:
        st.error(f"❌ Erreur de connexion : {e}")
        st.markdown("""
        ### 🔧 Solutions possibles :
        1. Vérifier les variables d'environnement dans Streamlit Cloud
        2. S'assurer que la base PostgreSQL est accessible depuis internet
        3. Vérifier les identifiants de connexion
        4. Contrôler que les tables existent
        """)

if __name__ == "__main__":
    st.set_page_config(page_title="Test PostgreSQL", page_icon="🔍")
    test_database_connection()