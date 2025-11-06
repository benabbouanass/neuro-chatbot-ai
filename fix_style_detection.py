# Fix pour améliorer la détection de style

# Dans ultimate_orchestrator.py, ligne ~50, modifier la logique :

# AVANT:
# if len(text.split()) <= 3:
#     style = "concis"

# APRÈS:
# if any(word in text_lower for word in ["bonjour", "salut", "hello", "bonsoir"]):
#     style = "cordial"
# elif len(text.split()) <= 3:
#     style = "concis"