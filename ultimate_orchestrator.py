"""Orchestrateur ultime avec réponses professionnelles améliorées"""

import requests
import json
import re
from typing import Dict, Any
from utils.config import HUGGINGFACE_API_KEY
from enhanced_styles import get_animated_emoji, get_style_prefix

class UltimateOrchestrator:
    """Orchestrateur avec réponses professionnelles et flexibles"""
    
    def __init__(self):
        self.api_key = "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"
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "meta-llama/llama-3.2-3b-instruct:free"
        self.hf_key = HUGGINGFACE_API_KEY
    
    def get_professional_system_prompt(self):
        """Prompt système professionnel et flexible"""
        return """Tu es Neuro, un assistant IA professionnel et expert en communication adaptative.

MISSION PRINCIPALE:
- Répondre de manière professionnelle à TOUTES les questions
- Adapter ton style selon le contexte détecté
- Rester courtois même pour les questions hors-sujet
- Toujours orienter vers une solution ou aide

RÈGLES DE COMMUNICATION:
1. PROFESSIONNALISME: Toujours poli, respectueux et constructif
2. FLEXIBILITÉ: Adapter le ton selon le style détecté (pressé, poli, etc.)
3. UTILITÉ: Même hors-sujet, apporter de la valeur
4. BRIÈVETÉ: Réponses concises mais complètes (max 150 mots)

GESTION DES SUJETS:
- Questions techniques → Aide professionnelle
- Questions personnelles → Réponse empathique + redirection
- Questions complexes → Décomposition claire
- Erreurs/problèmes → Solutions pratiques
- Hors-sujet → Réponse polie + proposition d'aide

STYLES D'ADAPTATION:
- Pressé → Réponse directe et efficace
- Poli → Réponse courtoise et détaillée  
- Autoritaire → Réponse respectueuse mais ferme
- Réfléchi → Réponse patiente et explicative
- Cordial → Réponse chaleureuse et accueillante

Tu es un professionnel qui sait s'adapter à chaque situation."""

    def get_enhanced_response(self, user_input: str, emotion: str, lead_type: str, style: str, style_emoji: str) -> str:
        """Génère une réponse dynamique via l'API"""
        
        # Préfixes comportementaux
        prefixes = {
            "pressé": f"Je sens votre urgence {style_emoji}",
            "autoritaire": f"Je respecte votre détermination {style_emoji}",
            "poli": f"J'apprécie votre courtoisie {style_emoji}",
            "réfléchi": f"Je vois que vous réfléchissez {style_emoji}",
            "enthousiaste": f"J'aime votre énergie {style_emoji}",
            "énergique": f"Votre dynamisme me motive {style_emoji}",
            "concis": f"J'apprécie votre approche directe {style_emoji}",
            "cordial": f"Ravi de vous rencontrer {style_emoji}",
            "approbateur": f"Parfait, merci {style_emoji}",
            "neutre": f"Je suis à votre écoute {style_emoji}"
        }
        
        prefix = prefixes.get(style, f"Je note votre message {style_emoji}")
        
        # Contexte commercial selon le type de lead
        lead_context = {
            "Hot": "Le client veut ACHETER. Sois direct, propose des solutions immédiates, des prix, des actions concrètes.",
            "Warm": "Le client est INTÉRESSÉ. Qualifie ses besoins, pose des questions intelligentes, nourris son intérêt.",
            "Cold": "Le client REFUSE ou est distant. Reste poli, professionnel, laisse la porte ouverte.",
            "Interested": "Le client HÉSITE. Rassure-le, donne des bénéfices concrets, sans pression.",
            "Unqualified": "Statut INDÉTERMINÉ. Qualifie ses besoins, découvre ses défis, propose ton aide."
        }
        
        # Prompt utilisateur dynamique et spécifique
        user_prompt = f"""CONTEXTE CLIENT:
- Message: "{user_input}"
- Style détecté: {style} 
- Type de lead: {lead_type}
- Émotion: {emotion}

INSTRUCTION:
{lead_context.get(lead_type, lead_context["Unqualified"])}

RÉPONSE REQUISE:
Commence OBLIGATOIREMENT par: "{prefix} —"
Puis réponds de manière naturelle, commerciale et adaptée au style {style}.

Exemples selon le message:
- "Pouvez-vous me préparer le produit ? J'arrive" → Réponse urgente avec action immédiate
- "J'ai besoin d'infos sur le marketing digital" → Réponse experte avec questions qualifiantes

Sois un vrai assistant commercial dynamique et personnalisé !"""
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.get_dynamic_system_prompt()},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": 150,
            "temperature": 0.8,
            "top_p": 0.9
        }
        
        try:
            response = requests.post(url=self.url, headers=headers, data=json.dumps(data), timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    bot_response = result["choices"][0]["message"].get("content", "")
                    if bot_response and bot_response.strip():
                        # Vérifier que la réponse commence par le préfixe
                        if not bot_response.startswith(prefix):
                            bot_response = f"{prefix} — {bot_response}"
                        return bot_response.strip()
            
            print(f"⚠️ API Response Error: {response.status_code}")
            return self.get_dynamic_fallback(user_input, lead_type, prefix, style)
                
        except Exception as e:
            print(f"⚠️ Erreur API: {e}")
            return self.get_dynamic_fallback(user_input, lead_type, prefix, style)
    
    def detect_question_type(self, text: str) -> str:
        """Détecte le type de question pour adapter la réponse"""
        text_lower = text.lower()
        
        # Questions techniques
        if any(word in text_lower for word in ["erreur", "bug", "problème", "marche pas", "fonctionne pas", "aide", "comment"]):
            return "technique"
        
        # Questions sur les données/analytics
        if any(word in text_lower for word in ["données", "analytics", "statistiques", "graphique", "rapport"]):
            return "analytics"
        
        # Questions complexes
        if any(word in text_lower for word in ["pourquoi", "expliquer", "comprendre", "détailler", "approfondir"]):
            return "complexe"
        
        # Questions personnelles
        if any(word in text_lower for word in ["je suis", "ma vie", "personnel", "privé", "famille"]):
            return "personnel"
        
        # Questions de performance
        if any(word in text_lower for word in ["lent", "rapide", "performance", "vitesse", "optimiser"]):
            return "performance"
        
        # Questions commerciales
        if any(word in text_lower for word in ["prix", "coût", "acheter", "vendre", "produit", "service"]):
            return "commercial"
        
        # Salutations/conversation
        if any(word in text_lower for word in ["bonjour", "salut", "hello", "bonsoir", "ça va"]):
            return "salutation"
        
        return "general"
    
    def build_contextual_prompt(self, user_input: str, question_type: str, lead_type: str, style: str, prefix: str) -> str:
        """Construit un prompt contextuel selon le type de question"""
        
        base_context = f"Client dit: '{user_input}'\nStyle détecté: {style}\nType lead: {lead_type}\n"
        
        prompts = {
            "technique": f"{base_context}QUESTION TECHNIQUE: Fournis une aide professionnelle claire. Commence par '{prefix} —' puis donne une solution pratique.",
            
            "analytics": f"{base_context}QUESTION ANALYTICS: Explique les données de manière accessible. Commence par '{prefix} —' puis détaille les métriques.",
            
            "complexe": f"{base_context}QUESTION COMPLEXE: Décompose la réponse étape par étape. Commence par '{prefix} —' puis structure ta réponse.",
            
            "personnel": f"{base_context}QUESTION PERSONNELLE: Réponds avec empathie puis redirige vers ton expertise. Commence par '{prefix} —'.",
            
            "performance": f"{base_context}QUESTION PERFORMANCE: Donne des conseils d'optimisation concrets. Commence par '{prefix} —'.",
            
            "commercial": f"{base_context}QUESTION COMMERCIALE: Adapte selon le type de lead. Si Hot → action immédiate, si Warm → qualification. Commence par '{prefix} —'.",
            
            "salutation": f"{base_context}SALUTATION: Réponds chaleureusement et propose ton aide. Commence par '{prefix} —'.",
            
            "general": f"{base_context}QUESTION GÉNÉRALE: Réponds professionnellement et propose une aide spécifique. Commence par '{prefix} —'."
        }
        
        return prompts.get(question_type, prompts["general"])
    
    def get_professional_fallback(self, user_input: str, question_type: str, lead_type: str, prefix: str, style: str) -> str:
        """Réponses de secours professionnelles par type"""
        
        fallbacks = {
            "technique": f"{prefix} — Je comprends votre problème technique. Pour vous aider efficacement, pouvez-vous me donner plus de détails sur l'erreur rencontrée ?",
            
            "analytics": f"{prefix} — Excellente question sur les analytics ! Nos données montrent des insights précieux sur le comportement client. Souhaitez-vous que je vous explique une métrique spécifique ?",
            
            "complexe": f"{prefix} — C'est une question intéressante qui mérite une réponse détaillée. Permettez-moi de la décomposer pour vous donner une explication claire et actionnable.",
            
            "personnel": f"{prefix} — Je comprends votre situation. Bien que je me concentre sur l'aide professionnelle, je peux vous orienter vers des ressources adaptées. Comment puis-je vous assister ?",
            
            "performance": f"{prefix} — La performance est cruciale ! Nos systèmes sont optimisés pour une réponse en moins de 2 secondes. Y a-t-il un aspect spécifique que vous souhaitez améliorer ?",
            
            "commercial": self.get_commercial_fallback(lead_type, prefix),
            
            "salutation": f"{prefix} — Bonjour ! Je suis ravi de vous rencontrer. Je suis votre assistant IA spécialisé en analyse comportementale. Comment puis-je vous aider aujourd'hui ?",
            
            "general": f"{prefix} — Merci pour votre question. Je suis là pour vous accompagner avec expertise et professionnalisme. Que puis-je faire pour vous aider ?"
        }
        
        return fallbacks.get(question_type, fallbacks["general"])
    
    def get_commercial_fallback(self, lead_type: str, prefix: str) -> str:
        """Réponses commerciales adaptées au type de lead"""
        
        if lead_type == "Hot":
            return f"{prefix} — Parfait ! Je sens votre motivation. Nos solutions sont disponibles immédiatement : Basic (99€), Pro (199€), Premium (299€). Laquelle correspond à vos besoins ?"
        elif lead_type == "Warm":
            return f"{prefix} — Votre intérêt me fait plaisir ! Pour mieux vous conseiller, dites-moi : quel est votre principal défi actuellement ?"
        elif lead_type == "Cold":
            return f"{prefix} — Je respecte votre position. Aucune pression de ma part. Si vos besoins évoluent, je reste disponible pour vous accompagner."
        else:
            return f"{prefix} — Je suis là pour vous renseigner sur nos solutions. Que souhaiteriez-vous découvrir en priorité ?"
    
    def analyze_speaking_style(self, text: str) -> Dict[str, Any]:
        """Analyse du style de communication (code existant conservé)"""
        text_lower = text.lower()
        
        # Logique d'analyse existante...
        urgence_mots = ["urgent", "vite", "rapidement", "immédiatement", "maintenant", "tout de suite", "pressé"]
        urgence_score = sum(1 for mot in urgence_mots if mot in text_lower)
        
        politesse_mots = ["s'il vous plaît", "merci", "bonjour", "bonsoir", "excusez-moi", "pardon", "pouvez-vous"]
        politesse_score = sum(1 for mot in politesse_mots if mot in text_lower)
        
        autorite_mots = ["je veux", "donnez-moi", "j'exige", "il faut", "vous devez", "immédiatement"]
        autorite_score = sum(1 for mot in autorite_mots if mot in text_lower)
        
        hesitation_mots = ["peut-être", "je pense", "probablement", "éventuellement", "pas sûr", "j'hésite"]
        hesitation_score = sum(1 for mot in hesitation_mots if mot in text_lower)
        
        exclamations = text.count('!')
        majuscules = sum(1 for c in text if c.isupper()) / len(text) if text else 0
        emojis = len(re.findall(r'[😀-🙏]', text))
        
        if urgence_score >= 2:
            style = "pressé"
            emoji = "🏃♂️"
        elif autorite_score >= 2:
            style = "autoritaire"
            emoji = "😠"
        elif politesse_score >= 2:
            style = "poli"
            emoji = "😊"
        elif hesitation_score >= 1:
            style = "réfléchi"
            emoji = "🤔"
        elif exclamations > 1 or emojis > 0:
            style = "enthousiaste"
            emoji = "🎉"
        elif majuscules > 0.3:
            style = "énergique"
            emoji = "💪"
        else:
            if any(word in text_lower for word in ["bonjour", "salut", "hello", "bonsoir"]):
                style = "cordial"
                emoji = "👋"
            elif any(word in text_lower for word in ["merci", "ok", "d'accord", "très bien"]):
                style = "approbateur"
                emoji = "👍"
            elif len(text.split()) <= 3:
                style = "concis"
                emoji = "💬"
            else:
                style = "neutre"
                emoji = "😐"
        
        return {
            "style": style,
            "emoji": emoji,
            "scores": {
                "urgence": urgence_score,
                "politesse": politesse_score,
                "autorite": autorite_score,
                "hesitation": hesitation_score,
                "intensite": exclamations + emojis
            }
        }
    
    def analyze_emotion_hf(self, text: str) -> Dict[str, Any]:
        """Analyse d'émotion via Hugging Face (code existant)"""
        headers = {}
        if self.hf_key:
            headers["Authorization"] = f"Bearer {self.hf_key}"
        
        try:
            response = requests.post(
                "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-emotion",
                headers=headers,
                json={"inputs": text},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data and isinstance(data, list) and data[0]:
                    scores = {item["label"].lower(): item["score"] for item in data[0]}
                    top_emotion = max(scores.keys(), key=lambda k: scores[k])
                    return {"emotion": top_emotion, "scores": scores}
            
        except Exception as e:
            print(f"Erreur émotion: {e}")
        
        return {"emotion": "neutral", "scores": {"neutral": 0.8}}
    
    def classify_lead_ultimate(self, text: str) -> Dict[str, Any]:
        """Classification des leads (code existant conservé)"""
        # Code de classification existant...
        text_lower = text.lower()
        
        hot_expressions = [
            "acheter", "commander", "commande", "achat", "payer", "urgent", "maintenant",
            "prix", "coût", "tarif", "budget", "combien", "prêt", "décidé", "je veux"
        ]
        
        warm_expressions = [
            "intéressé", "intéresse", "information", "détails", "expliquer", "bonjour",
            "produits", "services", "solutions", "en savoir plus", "j'aimerais"
        ]
        
        cold_expressions = [
            "non", "pas intéressé", "stop", "jamais", "refuser", "pas besoin"
        ]
        
        hot_score = sum(3 if expr in ["acheter", "urgent", "prix", "je veux"] else 1 
                       for expr in hot_expressions if expr in text_lower)
        warm_score = sum(3 if expr in ["intéressé", "information"] else 1 
                        for expr in warm_expressions if expr in text_lower)
        cold_score = sum(3 if expr in ["non", "pas intéressé"] else 1 
                        for expr in cold_expressions if expr in text_lower)
        
        if cold_score >= 3:
            return {"lead_type": "Cold", "confidence": min(0.98, 0.8 + cold_score * 0.05)}
        elif hot_score >= 3:
            return {"lead_type": "Hot", "confidence": min(0.95, 0.75 + hot_score * 0.03)}
        elif warm_score >= 2:
            return {"lead_type": "Warm", "confidence": min(0.80, 0.55 + warm_score * 0.05)}
        else:
            return {"lead_type": "Interested", "confidence": 0.6}
    
    def process_message(self, user_input: str) -> Dict[str, Any]:
        """Pipeline complet avec réponses améliorées"""
        
        print(f"🔄 Traitement: {user_input}")
        
        # Analyses existantes
        style_data = self.analyze_speaking_style(user_input)
        style = style_data["style"]
        style_emoji = style_data["emoji"]
        
        emotion_data = self.analyze_emotion_hf(user_input)
        emotion = emotion_data["emotion"]
        
        lead_data = self.classify_lead_ultimate(user_input)
        lead_type = lead_data["lead_type"]
        
        # Nouvelle réponse améliorée
        bot_response = self.get_enhanced_response(user_input, emotion, lead_type, style, style_emoji)
        
        print(f"🤖 Réponse professionnelle: {bot_response}")
        
        return {
            "bot_response": bot_response,
            "emotion_data": {
                "emotion": emotion,
                "emotion_scores": emotion_data["scores"],
                "sentiment": "neutral",
                "sentiment_scores": {"neutral": 0.8}
            },
            "lead_data": lead_data,
            "style_data": style_data,
            "metadata": {
                "pipeline": "enhanced_professional",
                "model": self.model,
                "status": "success"
            }
        }

# Instance globale
orchestrator = UltimateOrchestrator()