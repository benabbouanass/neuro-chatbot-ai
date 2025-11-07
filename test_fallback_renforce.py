#!/usr/bin/env python3
"""Test du système de fallback renforcé"""

from ultimate_orchestrator import orchestrator

# Tests par catégorie
test_categories = {
    "COMMANDE": [
        "Je veux passer commande maintenant",
        "Envoyez-moi un devis",
        "Je souhaite acheter vos services"
    ],
    "INFOS ENTREPRISE": [
        "Vous faites quoi exactement ?",
        "Que proposez-vous ?",
        "Quels sont vos services ?"
    ],
    "FONCTIONNEMENT": [
        "Comment ça marche ?",
        "Je ne comprends pas le processus",
        "Quelles sont les étapes ?"
    ],
    "TARIFS": [
        "Combien ça coûte ?",
        "Quel est le prix ?",
        "Votre budget ?"
    ],
    "RESEAUX SOCIAUX": [
        "Comment améliorer ma visibilité sur Instagram ?",
        "Aide pour Facebook",
        "Stratégie réseaux sociaux"
    ],
    "URGENCE": [
        "C'est urgent !",
        "J'ai besoin d'une réponse rapidement",
        "Répondez-moi vite"
    ],
    "SALUTATIONS": [
        "Bonjour",
        "Salut",
        "Hello"
    ],
    "E-COMMERCE": [
        "J'ai une boutique en ligne",
        "Mon site e-commerce",
        "Vente en ligne"
    ]
}

print("=== TEST FALLBACK RENFORCE ===\n")

for category, messages in test_categories.items():
    print(f"[CATEGORIE] {category}")
    print("-" * 40)
    
    for i, message in enumerate(messages, 1):
        print(f"[TEST {i}] {message}")
        try:
            result = orchestrator.process_message(message)
            print(f"[REPONSE] {result['bot_response']}")
            print(f"[ANALYSE] {result['lead_data']['lead_type']} | {result['style_data']['style']}")
        except Exception as e:
            print(f"[ERREUR] {e}")
        print()
    
    print("=" * 60)
    print()

# Test de variation des réponses (même message plusieurs fois)
print("[TEST] VARIATION DES REPONSES")
print("-" * 40)

test_message = "Vous faites quoi exactement ?"
print(f"Message testé 5 fois: '{test_message}'")
print()

for i in range(5):
    result = orchestrator.process_message(test_message)
    print(f"[ESSAI {i+1}] {result['bot_response']}")
    print()