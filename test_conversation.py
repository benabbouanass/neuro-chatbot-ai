#!/usr/bin/env python3
"""Test de conversation continue"""

from ultimate_orchestrator import orchestrator

# Simulation d'une conversation
conversation = [
    "bonjour",
    "Vous faites quoi exactement ?",
    "J'ai une entreprise de e-commerce",
    "Combien ça coûte ?",
    "C'est trop cher pour moi"
]

print("=== TEST CONVERSATION CONTINUE ===\n")

for i, message in enumerate(conversation, 1):
    print(f"USER: {message}")
    try:
        result = orchestrator.process_message(message)
        print(f"BOT: {result['bot_response']}")
        print(f"[{result['lead_data']['lead_type']} | {result['style_data']['style']}]")
        print()
    except Exception as e:
        print(f"ERREUR: {e}")
        print()