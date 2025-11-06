"""Gestionnaire de base de données PostgreSQL pour le Neuro-Chatbot"""

import psycopg2
import uuid
from datetime import datetime
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.connection_params = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'database': os.getenv('DB_NAME', 'neuro_chatbot'),
            'user': os.getenv('DB_USER', 'postgres'),
            'password': os.getenv('DB_PASSWORD', '12345'),
            'port': os.getenv('DB_PORT', '5432')
        }
    
    def get_connection(self):
        """Établit une connexion à la base de données"""
        try:
            return psycopg2.connect(**self.connection_params)
        except Exception as e:
            st.error(f"Erreur de connexion à la base de données: {e}")
            return None
    
    def create_tables(self):
        """Crée les tables nécessaires"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cur = conn.cursor()
            
            # Table users
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20),
                    email VARCHAR(255) UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Table conversations
            cur.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id UUID REFERENCES users(id),
                    message TEXT NOT NULL,
                    response TEXT NOT NULL,
                    emotion VARCHAR(50),
                    lead_type VARCHAR(20),
                    lead_confidence FLOAT,
                    behavioral_style VARCHAR(50),
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
            cur.close()
            conn.close()
            return True
        except Exception as e:
            st.error(f"Erreur lors de la création des tables: {e}")
            return False
    
    def save_user(self, first_name, last_name, phone, email):
        """Sauvegarde un nouvel utilisateur"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cur = conn.cursor()
            user_id = str(uuid.uuid4())
            
            cur.execute("""
                INSERT INTO users (id, first_name, last_name, phone, email, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (user_id, first_name, last_name, phone, email, datetime.now()))
            
            result = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()
            return result
        except psycopg2.IntegrityError:
            return "EMAIL_EXISTS"
        except Exception as e:
            st.error(f"Erreur lors de la sauvegarde utilisateur: {e}")
            return None
    
    def get_user_by_email(self, email):
        """Récupère un utilisateur par email"""
        conn = self.get_connection()
        if not conn:
            return None
        
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, first_name, last_name, phone, email FROM users WHERE email = %s", (email,))
            result = cur.fetchone()
            cur.close()
            conn.close()
            
            if result:
                return {
                    'id': result[0],
                    'first_name': result[1],
                    'last_name': result[2],
                    'phone': result[3],
                    'email': result[4]
                }
            return None
        except Exception as e:
            st.error(f"Erreur lors de la récupération utilisateur: {e}")
            return None
    
    def save_conversation(self, user_id, message, response, emotion=None, lead_type=None, lead_confidence=None, behavioral_style=None):
        """Sauvegarde une conversation"""
        conn = self.get_connection()
        if not conn:
            return False
        
        try:
            cur = conn.cursor()
            conversation_id = str(uuid.uuid4())
            
            cur.execute("""
                INSERT INTO conversations (id, user_id, message, response, emotion, lead_type, lead_confidence, behavioral_style, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (conversation_id, user_id, message, response, emotion, lead_type, lead_confidence, behavioral_style, datetime.now()))
            
            conn.commit()
            cur.close()
            conn.close()
            return True
        except Exception as e:
            st.error(f"Erreur lors de la sauvegarde conversation: {e}")
            return False
    
    def get_user_conversations(self, user_id, limit=50):
        """Récupère les conversations d'un utilisateur"""
        conn = self.get_connection()
        if not conn:
            return []
        
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT message, response, emotion, lead_type, lead_confidence, behavioral_style, timestamp
                FROM conversations 
                WHERE user_id = %s 
                ORDER BY timestamp DESC 
                LIMIT %s
            """, (user_id, limit))
            
            results = cur.fetchall()
            cur.close()
            conn.close()
            
            conversations = []
            for row in results:
                conversations.append({
                    'message': row[0],
                    'response': row[1],
                    'emotion': row[2],
                    'lead_type': row[3],
                    'lead_confidence': row[4],
                    'behavioral_style': row[5],
                    'timestamp': row[6]
                })
            
            return conversations
        except Exception as e:
            st.error(f"Erreur lors de la récupération des conversations: {e}")
            return []

# Instance globale
db_manager = DatabaseManager()