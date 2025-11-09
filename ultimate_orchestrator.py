"""Orchestrateur ultime avec analyse complète de la manière de parler"""

import requests
import json
import re
import random
import os
from typing import Dict, Any
from utils.config import HUGGINGFACE_API_KEY
from enhanced_styles import get_animated_emoji, get_style_prefix

class UltimateOrchestrator:
    """Orchestrateur avec analyse complète : tonalité, urgence, politesse, confiance"""
    
    def __init__(self):
        # Essayer Streamlit secrets d'abord, puis variables d'environnement
        try:
            import streamlit as st
            self.api_key = st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY")
            self.groq_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
        except:
            self.api_key = os.getenv("OPENROUTER_API_KEY")
            self.groq_key = os.getenv("GROQ_API_KEY")
        
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "meta-llama/llama-3.2-3b-instruct:free"
        self.groq_model = "llama3-8b-8192"
        self.hf_key = HUGGINGFACE_API_KEY
        self.conversation_context = []  # Historique conversationnel
    
    def analyze_speaking_style(self, text: str) -> Dict[str, Any]:
        """Analyse complète de la manière de parler"""
        
        text_lower = text.lower()
        
        # 1. URGENCE
        urgence_mots = ["urgent", "vite", "rapidement", "immédiatement", "maintenant", "tout de suite", "pressé"]
        urgence_score = sum(1 for mot in urgence_mots if mot in text_lower)
        
        # 2. POLITESSE
        politesse_mots = ["s'il vous plaît", "merci", "bonjour", "bonsoir", "excusez-moi", "pardon", "pouvez-vous"]
        politesse_score = sum(1 for mot in politesse_mots if mot in text_lower)
        
        # 3. CONFIANCE/AUTORITÉ
        autorite_mots = ["je veux", "donnez-moi", "j'exige", "il faut", "vous devez", "immédiatement"]
        autorite_score = sum(1 for mot in autorite_mots if mot in text_lower)
        
        # 4. HÉSITATION
        hesitation_mots = ["peut-être", "je pense", "probablement", "éventuellement", "pas sûr", "j'hésite"]
        hesitation_score = sum(1 for mot in hesitation_mots if mot in text_lower)
        
        # 5. INTENSITÉ ÉMOTIONNELLE
        exclamations = text.count('!')
        majuscules = sum(1 for c in text if c.isupper()) / len(text) if text else 0
        emojis = len(re.findall(r'[😀-🙏]', text))
        
        # 6. DÉTERMINATION DU STYLE DOMINANT
        if urgence_score >= 2:
            style = "pressé"
            emoji = "🏃‍♂️"
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
            # Style neutre plus adaptatif selon le contexte
            if len(text.split()) <= 3:
                style = "concis"
                emoji = ""
            elif any(word in text_lower for word in ["bonjour", "salut", "hello", "bonsoir"]):
                style = "cordial"
                emoji = "👋"
            elif any(word in text_lower for word in ["merci", "ok", "d'accord", "très bien"]):
                style = "approbateur"
                emoji = "👍"
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
        """Analyse d'émotion via Hugging Face"""
        
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
        """Classification ultra-robuste avec 300+ mots-clés"""
        
        text_lower = text.lower()
        
        # HOT - Intention d'achat immédiate (80+ expressions)
        hot_expressions = [
            # Achat direct
            "acheter", "commander", "commande", "achat", "payer", "payement", "facture", "livrer",
            "prendre", "réserver", "souscrire", "s'abonner", "finaliser", "conclure", "acquérir",
            # Urgence commerciale
            "urgent", "maintenant", "immédiatement", "rapidement", "aujourd'hui", "tout de suite",
            "vite", "pressé", "asap", "en urgence", "sans délai", "direct", "express",
            # Prix/Budget confirmé
            "prix", "coût", "tarif", "budget", "combien", "devis", "facture", "paiement", 
            "€", "$", "euros", "dollars", "financement", "crédit", "acompte", "règlement",
            # Décision ferme
            "prêt", "décidé", "sûr", "certain", "convaincu", "ok", "d'accord", "go",
            "validé", "approuvé", "confirmé", "signé", "accepté", "banco", "marché conclu",
            # Actions concrètes
            "envoyer", "installer", "commencer", "démarrer", "signer", "contrat",
            "livraison", "expédition", "mise en service", "activation", "déploiement",
            # Expressions d'intention
            "je veux", "j'ai besoin", "il me faut", "prenez ma commande", "je prends",
            "c'est parti", "allons-y", "on y va", "foncez", "let's go"
        ]
        
        # WARM - Intérêt marqué (100+ expressions)
        warm_expressions = [
            # Intérêt marqué
            "intéressé", "intéresse", "intéressant", "attiré", "séduit", "curieux",
            "motivé", "tenté", "enthousiasmé", "impressionné", "conquis", "captivé",
            # Demande d'information
            "information", "détails", "expliquer", "présenter", "montrer", "voir", "découvrir",
            "renseigner", "documenter", "clarifier", "préciser", "développer", "approfondir",
            # Questions d'exploration
            "comment", "pourquoi", "quand", "où", "quoi", "quel", "quelle",
            "combien de temps", "à partir de quand", "jusqu'à quand", "dans quelles conditions",
            # Produits/Services
            "produits", "services", "solutions", "offres", "catalogue", "gamme",
            "options", "formules", "packages", "versions", "modèles", "références",
            # Engagement positif
            "bonjour", "salut", "bonsoir", "hello", "merci", "parfait", "excellent",
            "génial", "super", "formidable", "impressionnant", "remarquable",
            # Exploration active
            "explorer", "étudier", "examiner", "regarder", "tester", "essayer",
            "comparer", "analyser", "évaluer", "considérer", "inspecter", "vérifier",
            # Expressions d'intérêt
            "en savoir plus", "je veux savoir", "dites-moi", "parlez-moi",
            "j'aimerais", "ça m'intéresse", "pourriez-vous", "serait-il possible",
            "pouvez-vous me dire", "j'ai entendu parler", "on m'a dit que"
        ]
        
        # INTERESTED - Curiosité/Hésitation positive (40+ expressions)
        interested_expressions = [
            # Hésitation positive
            "peut-être", "possiblement", "éventuellement", "réfléchir", "penser",
            "probablement", "sans doute", "pourquoi pas", "à voir", "on verra",
            # Considération
            "considérer", "envisager", "voir", "regarder", "étudier", "comparer",
            "peser le pour et le contre", "y réfléchir", "prendre le temps",
            # Curiosité
            "intéressant", "sympa", "bon concept", "je suis curieux", "je veux tester",
            "ça m'intrigue", "original", "innovant", "pas mal", "cool", "surprenant",
            # Conditionnels
            "si", "dans le cas où", "à condition que", "selon", "en fonction de",
            "ça dépend", "suivant", "sous réserve", "si jamais", "au cas où"
        ]
        
        # COLD - Rejet/Désintérêt (50+ expressions)
        cold_expressions = [
            # Rejet direct
            "non", "pas", "jamais", "aucun", "stop", "arrêter", "cesser",
            "négatif", "refus", "impossible", "hors de question", "absolument pas",
            # Désintérêt
            "pas intéressé", "pas besoin", "inutile", "refuser", "rejeter",
            "décliner", "passer mon tour", "ça ne m'intéresse pas", "sans intérêt",
            # Demandes d'arrêt
            "annuler", "supprimer", "enlever", "retirer", "supprime-moi",
            "désabonner", "ne plus me contacter", "blacklister", "rayer de la liste",
            # Expressions négatives
            "aucun intérêt", "pas pour moi", "ne me contactez plus",
            "laissez-moi tranquille", "fichez-moi la paix", "pas maintenant",
            "plus tard", "jamais de la vie", "n'insistez pas", "c'est mort"
        ]
        
        # OBJECTIONS - Objections communes (30+ expressions)
        objection_expressions = [
            # Prix
            "trop cher", "cher", "coûteux", "budget serré", "pas les moyens",
            "hors budget", "prix élevé", "tarif prohibitif", "inabordable",
            # Timing
            "pas le bon moment", "trop tôt", "trop tard", "pas maintenant",
            "reporter", "décaler", "attendre", "plus tard dans l'année",
            # Concurrence
            "concurrent", "moins cher ailleurs", "meilleure offre",
            "comparer", "voir ailleurs", "d'autres options", "alternative",
            # Décision
            "consulter", "équipe", "patron", "direction", "comité", "validation"
        ]
        
        # UNQUALIFIED - Indéterminé
        unqualified_expressions = [
            "salut", "coucou", "ça va", "quoi de neuf", "test", "hello", "hey", "yo"
        ]
        
        # Calcul des scores avec pondération intelligente avancée
        hot_score = 0
        for expr in hot_expressions:
            if expr in text_lower:
                # Mots critiques : x3 points
                if expr in ["acheter", "commander", "urgent", "prix", "je veux", "maintenant"]:
                    hot_score += 3
                # Mots importants : x2 points
                elif expr in ["payer", "devis", "prêt", "décidé", "budget"]:
                    hot_score += 2
                # Mots standard : x1 point
                else:
                    hot_score += 1
        
        warm_score = 0
        for expr in warm_expressions:
            if expr in text_lower:
                # Mots critiques : x3 points
                if expr in ["intéressé", "information", "en savoir plus"]:
                    warm_score += 3
                # Mots importants : x2 points
                elif expr in ["produits", "services", "détails", "expliquer"]:
                    warm_score += 2
                # Mots standard : x1 point
                else:
                    warm_score += 1
        
        interested_score = 0
        for expr in interested_expressions:
            if expr in text_lower:
                if expr in ["peut-être", "réfléchir", "considérer"]:
                    interested_score += 2
                else:
                    interested_score += 1
        
        cold_score = 0
        for expr in cold_expressions:
            if expr in text_lower:
                # Mots critiques de rejet : x3 points
                if expr in ["non", "pas intéressé", "stop", "jamais"]:
                    cold_score += 3
                else:
                    cold_score += 1
        
        objection_score = sum(1 for expr in objection_expressions if expr in text_lower)
        unqualified_score = sum(1 for expr in unqualified_expressions if expr in text_lower)
        
        # Bonus pour combinaisons (+50%)
        if hot_score >= 2:
            hot_score = int(hot_score * 1.5)
        if warm_score >= 2:
            warm_score = int(warm_score * 1.5)
        
        # Classification avec logique améliorée et gestion des objections
        if cold_score >= 3:
            return {"lead_type": "Cold", "confidence": min(0.98, 0.8 + cold_score * 0.05)}
        elif objection_score >= 2:
            return {"lead_type": "Interested", "confidence": min(0.75, 0.5 + objection_score * 0.1)}
        elif hot_score >= 5:
            return {"lead_type": "Hot", "confidence": min(0.99, 0.85 + hot_score * 0.02)}
        elif hot_score >= 3:
            return {"lead_type": "Hot", "confidence": min(0.95, 0.75 + hot_score * 0.03)}
        elif warm_score >= 4:
            return {"lead_type": "Warm", "confidence": min(0.90, 0.65 + warm_score * 0.04)}
        elif warm_score >= 2:
            return {"lead_type": "Warm", "confidence": min(0.80, 0.55 + warm_score * 0.05)}
        elif interested_score >= 2:
            return {"lead_type": "Interested", "confidence": min(0.80, 0.6 + interested_score * 0.08)}
        elif interested_score >= 1:
            return {"lead_type": "Interested", "confidence": min(0.70, 0.5 + interested_score * 0.1)}
        elif unqualified_score >= 1:
            return {"lead_type": "Unqualified", "confidence": 0.4}
        else:
            # Détection des questions ouvertes pour éviter les réponses génériques
            if any(word in text_lower for word in ["quoi", "comment", "pourquoi", "quelle", "qu'est-ce que", "faire"]):
                return {"lead_type": "Interested", "confidence": 0.65}
            return {"lead_type": "Unqualified", "confidence": 0.3}
    
    def get_ultimate_response(self, user_input: str, emotion: str, lead_type: str, style: str, style_emoji: str) -> str:
        """Génère une réponse dynamique et conversationnelle avec l'API"""
        
        # Prompt système ultra-optimisé pour un ton commercial naturel
        system_prompt = """Tu es Neuro, un assistant commercial IA expert en marketing digital.

Ton rôle : Conseiller commercial empathique et professionnel qui aide les entreprises à développer leur marketing digital (influence, contenu, réseaux sociaux, croissance).

Ton style de communication :
✅ Naturel et conversationnel (jamais robotique)
✅ Empathique et à l'écoute des besoins
✅ Proactif avec des questions pertinentes
✅ Commercial subtil (valorisation douce)
✅ Adapté au style du client

Tu proposes des solutions concrètes en :
• Marketing d'influence
• Marketing de contenu
• Marketing sur réseaux sociaux
• Stratégies de croissance digitale
• Automatisation marketing

Tu dois TOUJOURS :
1. Reformuler/résumer ce que dit le client
2. Poser une question qualifiante
3. Proposer une valeur ajoutée
4. Garder un ton humain et chaleureux"""
        
        # Prompt utilisateur contextualisé et dynamique avec historique
        context_info = self._get_context_info(user_input, lead_type, style, emotion)
        context_summary = self.get_context_summary()
        
        user_prompt = f"""CLIENT: "{user_input}"

{context_summary}

CONTEXTE ACTUEL:
- Style: {style} ({emotion})
- Intention: {lead_type}
- Besoin probable: {context_info}

Réponds de manière naturelle et conversationnelle. Sois un vrai conseiller commercial qui comprend ses besoins en marketing digital.

Si c'est une suite de conversation, réfère-toi au contexte précédent.

NE commence PAS par des formules comme "Je suis à votre écoute" ou "Je note votre approche".

Commence directement par une réponse pertinente et engageante."""
        
        # Essai OpenRouter
        if self.api_key:
            try:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "max_tokens": 200,
                    "temperature": 0.7,
                    "top_p": 0.9
                }
                
                response = requests.post(url=self.url, headers=headers, data=json.dumps(data), timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    if "choices" in result and len(result["choices"]) > 0:
                        bot_response = result["choices"][0]["message"].get("content", "")
                        if bot_response and bot_response.strip():
                            print("[SUCCESS] OpenRouter API")
                            return bot_response.strip()
                            
            except Exception as e:
                print(f"[WARNING] OpenRouter Error: {e}")
        
        # Fallback Groq
        if self.groq_key:
            try:
                headers = {
                    "Authorization": f"Bearer {self.groq_key}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": self.groq_model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "max_tokens": 200,
                    "temperature": 0.7
                }
                
                response = requests.post(url=self.groq_url, headers=headers, data=json.dumps(data), timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    if "choices" in result and len(result["choices"]) > 0:
                        bot_response = result["choices"][0]["message"].get("content", "")
                        if bot_response and bot_response.strip():
                            print("[SUCCESS] Groq API")
                            return bot_response.strip()
                            
            except Exception as e:
                print(f"[WARNING] Groq Error: {e}")
        
        # Fallback local
        print("[FALLBACK] Using local responses")
        return self._get_dynamic_fallback(user_input, lead_type, style, context_info)
    
    def _get_context_info(self, user_input: str, lead_type: str, style: str, emotion: str) -> str:
        """Détermine le contexte probable du besoin client"""
        text_lower = user_input.lower()
        
        if any(word in text_lower for word in ["marketing", "digital", "influence", "contenu", "réseaux", "croissance"]):
            return "Stratégie marketing digital"
        elif any(word in text_lower for word in ["produit", "service", "solution", "offre"]):
            return "Découverte produit/service"
        elif any(word in text_lower for word in ["prix", "tarif", "coût", "budget"]):
            return "Information tarifaire"
        elif any(word in text_lower for word in ["aide", "conseil", "accompagnement"]):
            return "Besoin d'accompagnement"
        else:
            return "Qualification des besoins"
    
    def _detect_message_category(self, text: str) -> str:
        """Détecte la catégorie du message pour un fallback ciblé"""
        text_lower = text.lower()
        
        # Catégorie COMMANDE/ACHAT
        if any(word in text_lower for word in ["commande", "acheter", "devis", "passer commande", "commander", "prendre", "souscrire"]):
            return "commande"
        
        # Catégorie INFOS ENTREPRISE
        elif any(word in text_lower for word in ["faites quoi", "proposez", "services", "qu'est-ce que", "votre entreprise", "activité"]):
            return "infos"
        
        # Catégorie FONCTIONNEMENT
        elif any(word in text_lower for word in ["comment ça marche", "fonctionnement", "process", "étapes", "déroulement"]):
            return "fonctionnement"
        
        # Catégorie TARIFS
        elif any(word in text_lower for word in ["prix", "tarif", "coût", "combien", "budget", "facture"]):
            return "tarifs"
        
        # Catégorie RÉSEAUX SOCIAUX
        elif any(word in text_lower for word in ["instagram", "facebook", "linkedin", "tiktok", "réseaux sociaux", "visibilité"]):
            return "reseaux"
        
        # Catégorie URGENCE
        elif any(word in text_lower for word in ["urgent", "vite", "rapidement", "pressé", "immédiatement"]):
            return "urgence"
        
        # Catégorie COMPARAISON
        elif any(word in text_lower for word in ["compare", "concurrence", "différence", "mieux", "avantage"]):
            return "comparaison"
        
        # Catégorie SALUTATIONS
        elif any(word in text_lower for word in ["bonjour", "salut", "hello", "bonsoir", "hey"]):
            return "salutation"
        
        # Catégorie E-COMMERCE
        elif any(word in text_lower for word in ["e-commerce", "boutique en ligne", "vente en ligne", "site web"]):
            return "ecommerce"
        
        # Catégorie AIDE GÉNÉRALE
        elif any(word in text_lower for word in ["aide", "aider", "conseil", "accompagnement", "support"]):
            return "aide"
        
        return "unknown"
    
    def _get_dynamic_fallback(self, user_input: str, lead_type: str, style: str, context_info: str) -> str:
        """Système de fallback renforcé avec catégorisation intelligente"""
        
        category = self._detect_message_category(user_input)
        
        # Réponses catégorisées avec variations
        categorized_responses = {
            "commande": [
                "Parfait ! Voyons ensemble vos besoins : augmenter vos ventes, votre visibilité ou votre audience ?",
                "Excellent ! Nous avons des créneaux disponibles cette semaine. Pouvez-vous préciser votre secteur d'activité ?",
                "Super ! Pour préparer votre offre personnalisée, dites-moi quel est votre objectif principal ?"
            ],
            "infos": [
                "Nous aidons les entreprises à développer leur marketing digital via le contenu, les réseaux sociaux et l'influence. Quel domaine vous intéresse le plus ?",
                "Nos solutions couvrent marketing digital, réseaux sociaux et stratégies de croissance. Quel est votre objectif principal ?",
                "Nous sommes spécialisés dans le marketing digital : influence, contenu, réseaux sociaux. Sur quoi souhaitez-vous vous concentrer ?"
            ],
            "fonctionnement": [
                "Excellente question ! Nous proposons des stratégies personnalisées selon vos besoins. Sur quel domaine souhaitez-vous vous développer ?",
                "Tout dépend de vos objectifs : augmenter votre audience, vos ventes ou votre visibilité ? Que préférez-vous ?",
                "Notre approche s'adapte à chaque entreprise. Pouvez-vous me parler de vos défis actuels ?"
            ],
            "tarifs": [
                "Bien sûr ! Pour vous proposer un devis précis, pouvez-vous me donner quelques détails sur votre projet ?",
                "Nos tarifs s'adaptent à vos besoins. Quel type de marketing digital vous intéresse : contenu, réseaux sociaux ou influence ?",
                "Je peux vous établir un devis personnalisé. Parlez-moi de votre entreprise et de vos objectifs ?"
            ],
            "reseaux": [
                "Nous avons des stratégies adaptées à chaque réseau ! Sur quel objectif voulez-vous vous concentrer : audience ou ventes ?",
                "Très bonne question ! Préférez-vous un accompagnement global ou ciblé sur un réseau en particulier ?",
                "Les réseaux sociaux sont notre spécialité ! Quel est votre défi principal : contenu, engagement ou croissance ?"
            ],
            "urgence": [
                "Parfait ! Voyons ensemble vos besoins rapidement : visibilité, audience ou ventes ?",
                "Excellent timing ! Nous pouvons accélérer le processus. Quel est votre objectif principal ?",
                "Compris ! Pour agir vite et bien, dites-moi quel est votre besoin le plus urgent ?"
            ],
            "comparaison": [
                "Je comprends votre démarche de comparaison. Pour mieux vous conseiller, pouvez-vous me parler de vos attentes principales ?",
                "Chaque entreprise est unique ! Pouvez-vous préciser vos objectifs pour que je vous propose la meilleure solution ?",
                "Excellente approche ! Dites-moi quels sont vos critères les plus importants ?"
            ],
            "salutation": [
                "Bonjour ! Ravi de vous rencontrer. Je suis Neuro, votre assistant marketing digital. Comment puis-je vous aider ?",
                "Salut ! Enchanté de faire votre connaissance. Parlez-moi de vos besoins en marketing digital !",
                "Hello ! Bienvenue ! Je suis là pour vous accompagner dans votre développement digital. Que puis-je faire pour vous ?"
            ],
            "ecommerce": [
                "Parfait ! L'e-commerce est notre domaine d'expertise. Votre priorité : augmenter le trafic, les conversions ou la fidélisation ?",
                "Excellent ! Pour les boutiques en ligne, nous proposons des stratégies complètes. Quel est votre principal défi actuellement ?",
                "Super ! Le marketing digital est essentiel pour l'e-commerce. Souhaitez-vous travailler sur l'acquisition ou la rétention ?"
            ],
            "aide": [
                "Je suis là pour vous accompagner ! Que souhaitez-vous développer : votre présence sur les réseaux sociaux, votre stratégie de contenu, ou votre marketing d'influence ?",
                "Avec plaisir ! Dites-moi quel aspect du marketing digital vous pose le plus de difficultés ?",
                "Bien sûr ! Pour mieux vous orienter, pouvez-vous me préciser vos objectifs marketing ?"
            ]
        }
        
        # Réponses par type de lead (si catégorie inconnue)
        lead_responses = {
            "Hot": [
                "Parfait ! Je vois que vous êtes motivé. Nos solutions sont disponibles immédiatement. Quel est votre objectif : ventes, visibilité ou audience ?",
                "Excellent ! Nous pouvons démarrer rapidement. Pour vous proposer la meilleure solution, parlez-moi de votre secteur ?"
            ],
            "Warm": [
                "Je comprends votre intérêt ! Le marketing digital est effectivement un levier puissant. Quel est votre plus grand défi : leads, fidélisation ou notoriété ?",
                "Très bonne approche ! Pour vous orienter au mieux, pouvez-vous me parler de votre entreprise ?"
            ],
            "Cold": [
                "Je respecte votre position. Aucune pression ! Si vos besoins évoluent, je reste disponible.",
                "Pas de souci, je comprends. Gardez mes coordonnées si vos priorités changent."
            ],
            "Interested": [
                "C'est normal de prendre son temps ! Avez-vous des questions spécifiques pour vous aider dans votre réflexion ?",
                "Je comprends votre hésitation. Puis-je vous poser quelques questions pour mieux cerner vos attentes ?"
            ]
        }
        
        # Sélection de la réponse
        import random
        
        if category != "unknown":
            return random.choice(categorized_responses[category])
        else:
            # Fallback par type de lead
            responses = lead_responses.get(lead_type, [
                "Merci pour votre message ! Pour mieux vous conseiller, pouvez-vous préciser vos besoins ?",
                "Intéressant ! Dites-moi sur quel aspect du marketing digital vous souhaitez vous concentrer ?",
                "Je suis là pour vous aider ! Quel est votre objectif principal en marketing digital ?"
            ])
            return random.choice(responses)
    
    def add_to_context(self, user_input: str, bot_response: str):
        """Ajoute l'échange au contexte conversationnel"""
        self.conversation_context.append({
            "user": user_input,
            "bot": bot_response
        })
        # Garde seulement les 3 derniers échanges pour éviter la surcharge
        if len(self.conversation_context) > 3:
            self.conversation_context.pop(0)
    
    def get_context_summary(self) -> str:
        """Résumé du contexte conversationnel"""
        if not self.conversation_context:
            return "Première interaction"
        
        context_str = "Contexte précédent:\n"
        for exchange in self.conversation_context[-2:]:  # 2 derniers échanges
            context_str += f"Client: {exchange['user']}\nNeuro: {exchange['bot']}\n"
        return context_str
    
    def process_message(self, user_input: str) -> Dict[str, Any]:
        """Pipeline ultime complet avec contexte conversationnel"""
        
        print(f"[PROCESSING] {user_input}")
        
        # 1. Analyse du style de parole
        style_data = self.analyze_speaking_style(user_input)
        style = style_data["style"]
        style_emoji = style_data["emoji"]
        print(f"[STYLE] {style}")
        
        # 2. Analyse émotionnelle
        emotion_data = self.analyze_emotion_hf(user_input)
        emotion = emotion_data["emotion"]
        print(f"[EMOTION] {emotion}")
        
        # 3. Classification lead ultime
        lead_data = self.classify_lead_ultimate(user_input)
        lead_type = lead_data["lead_type"]
        print(f"[LEAD] {lead_type} (conf: {lead_data['confidence']:.2f})")
        
        # 4. Réponse avec contexte conversationnel
        bot_response = self.get_ultimate_response(user_input, emotion, lead_type, style, style_emoji)
        print(f"[RESPONSE] Generated successfully")
        
        # 5. Ajout au contexte pour les prochaines interactions
        self.add_to_context(user_input, bot_response)
        
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
                "pipeline": "ultimate",
                "model": self.model,
                "status": "success",
                "context_length": len(self.conversation_context)
            }
        }

# Instance globale
orchestrator = UltimateOrchestrator()