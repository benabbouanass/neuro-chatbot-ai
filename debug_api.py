import streamlit as st
import os
import requests
import json

st.title("🔍 Debug API Keys")

# Test Streamlit secrets
st.subheader("1. Streamlit Secrets")
try:
    openrouter_key = st.secrets.get("OPENROUTER_API_KEY")
    groq_key = st.secrets.get("GROQ_API_KEY")
    
    st.write(f"OpenRouter Key: {'✅ Found' if openrouter_key else '❌ Missing'}")
    st.write(f"Groq Key: {'✅ Found' if groq_key else '❌ Missing'}")
    
    if openrouter_key:
        st.write(f"OpenRouter starts with: {openrouter_key[:10]}...")
    if groq_key:
        st.write(f"Groq starts with: {groq_key[:10]}...")
        
except Exception as e:
    st.error(f"Secrets error: {e}")

# Test environment variables
st.subheader("2. Environment Variables")
env_openrouter = os.getenv("OPENROUTER_API_KEY")
env_groq = os.getenv("GROQ_API_KEY")

st.write(f"ENV OpenRouter: {'✅ Found' if env_openrouter else '❌ Missing'}")
st.write(f"ENV Groq: {'✅ Found' if env_groq else '❌ Missing'}")

# Test API calls
st.subheader("3. API Tests")

if st.button("Test OpenRouter API"):
    key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
    if key:
        try:
            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "meta-llama/llama-3.2-3b-instruct:free",
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 50
            }
            
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            st.write(f"Status: {response.status_code}")
            st.json(response.json())
            
        except Exception as e:
            st.error(f"OpenRouter error: {e}")
    else:
        st.error("No OpenRouter key found")

if st.button("Test Groq API"):
    key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if key:
        try:
            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": "Hello"}],
                "max_tokens": 50
            }
            
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            st.write(f"Status: {response.status_code}")
            st.json(response.json())
            
        except Exception as e:
            st.error(f"Groq error: {e}")
    else:
        st.error("No Groq key found")