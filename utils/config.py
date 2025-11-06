# config.py
# Paramètres globaux (utiliser des variables d'environnement pour les clés sensibles)

import os

# OpenRouter (DeepSeek)
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "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")
OPENROUTER_API_URL = os.environ.get("OPENROUTER_API_URL", "https://openrouter.ai/api/v1")
DEEPSEEK_MODEL = os.environ.get("DEEPSEEK_MODEL", "meta-llama/llama-3.2-3b-instruct:free")

# Hugging Face
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY", None)
# Modèles recommandés
HF_EMOTION_MODEL = os.environ.get("HF_EMOTION_MODEL", "cardiffnlp/twitter-roberta-base-emotion")
HF_SENTIMENT_MODEL = os.environ.get("HF_SENTIMENT_MODEL", "nlptown/bert-base-multilingual-uncased-sentiment")

# Stockage
LEADS_JSON_PATH = os.environ.get("LEADS_JSON_PATH", "leads_data.json")

# Application
DEFAULT_CONFIDENCE_THRESHOLD = 0.5
