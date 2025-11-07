#!/usr/bin/env python3
"""Test du problème de réponses répétitives"""

from ultimate_orchestrator import orchestrator

# Tests avec les exemples problématiques
test_messages = [
    "bonjour",
    "Vous faites quoi exactement ?",
    "Comment ça marche ?",
    "Qu'est-ce que vous proposez ?",
    "Salut",
    "Hello"
]

print("=== TEST CORRECTION REPONSES REPETITIVES ===\n")

for i, message in enumerate(test_messages, 1):
    print(f"[TEST {i}] {message}")
    try:
        result = orchestrator.process_message(message)
        print(f"[REPONSE] {result['bot_response']}")
        print(f"[ANALYSE] LEAD: {result['lead_data']['lead_type']} | STYLE: {result['style_data']['style']}")
        print("-" * 60)
    except Exception as e:
        print(f"[ERREUR] {e}")
        print("-" * 60)