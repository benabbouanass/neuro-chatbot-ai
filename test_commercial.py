#!/usr/bin/env python3
"""Test des réponses commerciales améliorées"""

from ultimate_orchestrator import orchestrator

# Tests avec les exemples fournis
test_messages = [
    "Pouvez-vous me préparer le produit ? J'arrive",
    "J'ai besoin de quelques informations sur le marketing digital, le marketing d'influence, le marketing de contenu, ou le marketing sur les réseaux sociaux, et sur la façon dont votre entreprise peut aider la mienne à atteindre la croissance.",
    "Bonjour, je cherche des solutions pour développer mon business",
    "C'est urgent ! Quel est le prix ?",
    "Je ne suis pas intéressé"
]

print("=== TEST DES RÉPONSES COMMERCIALES AMÉLIORÉES ===\n")

for i, message in enumerate(test_messages, 1):
    print(f"[TEST {i}] {message}")
    try:
        result = orchestrator.process_message(message)
        print(f"[REPONSE] {result['bot_response']}")
        print(f"[ANALYSE] LEAD: {result['lead_data']['lead_type']} | STYLE: {result['style_data']['style']}")
        print("-" * 80)
    except Exception as e:
        print(f"[ERREUR] {e}")
        print("-" * 80)