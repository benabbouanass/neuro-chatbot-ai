#!/usr/bin/env python3
"""Debug pour Streamlit Cloud"""

import streamlit as st
import os
import requests
import json

def debug_api_config():
    """Debug de la configuration API sur Streamlit Cloud"""
    
    st.title("🔧 Debug API Configuration")
    
    # Vérification des variables d'environnement
    st.subheader("📋 Variables d'environnement")
    
    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    groq_key = os.getenv("GROQ_API_KEY")
    
    st.write(f"**OpenRouter Key:** {'✅ Configurée' if openrouter_key else '❌ Manquante'}")
    if openrouter_key:
        st.write(f"Longueur: {len(openrouter_key)} caractères")
        st.write(f"Préfixe: {openrouter_key[:10]}...")
    
    st.write(f"**Groq Key:** {'✅ Configurée' if groq_key else '❌ Manquante'}")
    if groq_key:
        st.write(f"Longueur: {len(groq_key)} caractères")
        st.write(f"Préfixe: {groq_key[:10]}...")
    
    # Test des APIs
    st.subheader("🧪 Test des APIs")
    
    if st.button("Tester OpenRouter"):
        if openrouter_key:
            test_openrouter(openrouter_key)
        else:
            st.error("Clé OpenRouter manquante")
    
    if st.button("Tester Groq"):
        if groq_key:
            test_groq(groq_key)
        else:
            st.error("Clé Groq manquante")
    
    if st.button("Tester Orchestrateur"):
        test_orchestrator()

def test_openrouter(api_key):
    """Test OpenRouter API"""
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "messages": [{"role": "user", "content": "Hello test"}],
        "max_tokens": 50
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=10
        )
        
        st.write(f"**Status Code:** {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            if "choices" in result:
                st.success("✅ OpenRouter fonctionne!")
                st.write(f"**Réponse:** {result['choices'][0]['message']['content']}")
            else:
                st.error("❌ Pas de réponse dans choices")
        else:
            st.error(f"❌ Erreur: {response.text}")
            
    except Exception as e:
        st.error(f"❌ Exception: {e}")

def test_groq(api_key):
    """Test Groq API"""
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": "Hello test"}],
        "max_tokens": 50
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=10
        )
        
        st.write(f"**Status Code:** {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            if "choices" in result:
                st.success("✅ Groq fonctionne!")
                st.write(f"**Réponse:** {result['choices'][0]['message']['content']}")
            else:
                st.error("❌ Pas de réponse dans choices")
        else:
            st.error(f"❌ Erreur: {response.text}")
            
    except Exception as e:
        st.error(f"❌ Exception: {e}")

def test_orchestrator():
    """Test de l'orchestrateur"""
    
    try:
        from ultimate_orchestrator import orchestrator
        
        st.write("**Configuration Orchestrateur:**")
        st.write(f"OpenRouter Key: {'✅' if orchestrator.openrouter_key else '❌'}")
        st.write(f"Groq Key: {'✅' if orchestrator.groq_key else '❌'}")
        
        # Test d'un message
        result = orchestrator.process_message("Hello test")
        
        st.success("✅ Orchestrateur fonctionne!")
        st.write(f"**Réponse:** {result['bot_response']}")
        st.write(f"**Lead:** {result['lead_data']['lead_type']}")
        st.write(f"**Style:** {result['style_data']['style']}")
        
    except Exception as e:
        st.error(f"❌ Erreur Orchestrateur: {e}")

if __name__ == "__main__":
    debug_api_config()