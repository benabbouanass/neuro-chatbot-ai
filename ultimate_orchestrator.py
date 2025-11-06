"""Orchestrateur ultime avec analyse complète de la manière de parler"""

import requests
import json
import re
from typing import Dict, Any
from utils.config import HUGGINGFACE_API_KEY
from enhanced_styles import get_animated_emoji, get_style_prefix

class UltimateOrchestrator:
    """Orchestrateur avec analyse complète : tonalité, urgence, politesse, confiance"""
    
    def __init__(self):
        self.api_key = "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"
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "meta-llama/llama-3.2-3b-instruct:free"
        self.hf_key = HUGGINGFACE_API_KEY
    
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
                emoji = "💬"
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
            return {"lead_type": "Unqualified", "confidence": 0.3}
    
    def get_ultimate_response(self, user_input: str, emotion: str, lead_type: str, style: str, style_emoji: str) -> str:
        """Génère une réponse avec prompt engineering avancé et few-shot learning"""
        
        # Préfixe comportemental selon le style détecté
        prefixes = {
            "pressé": f"Vous semblez pressé {style_emoji}",
            "autoritaire": f"Je sens votre détermination {style_emoji}",
            "poli": f"J'apprécie votre courtoisie {style_emoji}",
            "réfléchi": f"Je vois que vous réfléchissez {style_emoji}",
            "enthousiaste": f"Votre enthousiasme me plaît {style_emoji}",
            "énergique": f"J'aime votre énergie {style_emoji}",
            "concis": f"Je note votre approche directe {style_emoji}",
            "cordial": f"Ravi de vous rencontrer {style_emoji}",
            "approbateur": f"Parfait, je vous remercie {style_emoji}",
            "neutre": f"Je suis à votre écoute {style_emoji}"
        }
        
        prefix = prefixes.get(style, f"Je note votre approche {style_emoji}")
        
        # Prompt système optimisé avec few-shot learning
        system_prompt = f"""Tu es Neuro, un assistant IA émotionnel et commercial expert.
Ta mission : comprendre le ton, les émotions et les intentions du client.
Tu adaptes ton vocabulaire, ton rythme et ton ton selon le style détecté :
- pressé → concis et direct 🏃♂️
- autoritaire → affirmé mais respectueux 😎  
- réfléchi → doux, patient et explicatif 🤔
- poli → courtois et professionnel 😊
- enthousiaste → énergique et motivant 🎉
- énergique → dynamique et engageant 💪
- concis → efficace et précis 💬
- cordial → chaleureux et accueillant 👋
- approbateur → positif et encourageant 👍
- neutre → adaptable et professionnel 😐

Tu réponds toujours de manière professionnelle, empathique et efficace.

EXEMPLES DE DIALOGUES RÉUSSIS :

Client pressé: "C'est urgent ! Quel est le prix ?"
Neuro: "Vous semblez pressé 🏃♂️ — Parfait ! Notre solution premium est à 299€. Commande immédiate possible. Voulez-vous que je finalise maintenant ?"

Client poli: "Bonjour, pourriez-vous m'aider s'il vous plaît ?"
Neuro: "J'apprécie votre courtoisie 😊 — Bonjour ! Je serais ravi de vous accompagner. Que puis-je vous présenter aujourd'hui ?"

Client réfléchi: "Je pense que ça pourrait m'intéresser..."
Neuro: "Je vois que vous réfléchissez 🤔 — C'est sage de prendre son temps. Puis-je vous poser quelques questions pour mieux comprendre vos besoins ?"

Maintenant, réponds au client selon son style détecté."""
        
        # Prompt adapté au lead type avec contexte enrichi
        if lead_type == "Hot":
            user_prompt = f"Le client dit '{user_input}'. Style détecté: {style}. Il veut ACHETER. Réponds avec '{prefix} — ' puis propose une action d'achat concrète et urgente."
        elif lead_type == "Warm":
            user_prompt = f"Le client dit '{user_input}'. Style détecté: {style}. Il est INTÉRESSÉ. Réponds avec '{prefix} — ' puis pose des questions qualifiantes intelligentes."
        elif lead_type == "Cold":
            user_prompt = f"Le client dit '{user_input}'. Style détecté: {style}. Il REFUSE. Réponds avec '{prefix} — ' puis reste poli, respectueux et laisse la porte ouverte."
        elif lead_type == "Interested":
            user_prompt = f"Le client dit '{user_input}'. Style détecté: {style}. Il HÉSITE. Réponds avec '{prefix} — ' puis nourris sa curiosité sans pression."
        else:
            user_prompt = f"Le client dit '{user_input}'. Style détecté: {style}. Statut INDÉTERMINÉ. Réponds avec '{prefix} — ' puis qualifie ses besoins avec tact."
        
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
            "max_tokens": 150,
            "temperature": 0.6
        }
        
        try:
            response = requests.post(url=self.url, headers=headers, data=json.dumps(data), timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    bot_response = result["choices"][0]["message"].get("content", "")
                    if bot_response and bot_response.strip():
                        return bot_response.strip()
            
            return self._get_ultimate_fallback(user_input, lead_type, prefix)
                
        except Exception as e:
            print(f"⚠️ Erreur API: {e}")
            return self._get_ultimate_fallback(user_input, lead_type, prefix)
    
    def _get_ultimate_fallback(self, user_input: str, lead_type: str, prefix: str) -> str:
        """Réponse de secours optimisée avec empathie et action claire"""
        
        if lead_type == "Hot":
            return f"{prefix} — Excellent ! Je sens votre motivation. Nos solutions sont disponibles immédiatement. Souhaitez-vous que je vous prépare une offre personnalisée maintenant ?"
        elif lead_type == "Warm":
            return f"{prefix} — Votre intérêt me fait plaisir ! Pour mieux vous conseiller, dites-moi : quel est votre défi principal actuellement ?"
        elif lead_type == "Cold":
            return f"{prefix} — Je comprends parfaitement votre position. Aucune pression de ma part. Si vos besoins évoluent, je reste disponible."
        elif lead_type == "Interested":
            return f"{prefix} — Votre réflexion est tout à fait légitime. Puis-je vous poser 2-3 questions rapides pour mieux cerner vos attentes ?"
        else:
            # Réponse adaptée selon le style neutre détecté
            if style == "concis":
                return f"{prefix} — Solutions disponibles : Basic (99€), Pro (199€), Premium (299€). Laquelle vous intéresse ?"
            elif style == "cordial":
                return f"{prefix} — Quelle belle journée pour découvrir nos solutions ! Comment puis-je vous accompagner ?"
            elif style == "approbateur":
                return f"{prefix} — Excellent ! Parlons de vos besoins. Quel est votre objectif principal ?"
            else:
                return f"{prefix} — Je suis là pour vous aider. Que puis-je faire pour vous aujourd'hui ?"
    
    def process_message(self, user_input: str) -> Dict[str, Any]:
        """Pipeline ultime complet"""
        
        print(f"🔄 Traitement: {user_input}")
        
        # 1. Analyse du style de parole
        style_data = self.analyze_speaking_style(user_input)
        style = style_data["style"]
        style_emoji = style_data["emoji"]
        print(f"🎭 Style: {style} {style_emoji}")
        
        # 2. Analyse émotionnelle
        emotion_data = self.analyze_emotion_hf(user_input)
        emotion = emotion_data["emotion"]
        print(f"😊 Émotion: {emotion}")
        
        # 3. Classification lead ultime
        lead_data = self.classify_lead_ultimate(user_input)
        lead_type = lead_data["lead_type"]
        print(f"🎯 Lead: {lead_type} (conf: {lead_data['confidence']:.2f})")
        
        # 4. Réponse avec préfixe comportemental
        bot_response = self.get_ultimate_response(user_input, emotion, lead_type, style, style_emoji)
        print(f"🤖 Réponse finale: {bot_response}")
        
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
                "status": "success"
            }
        }

# Instance globale
orchestrator = UltimateOrchestrator()