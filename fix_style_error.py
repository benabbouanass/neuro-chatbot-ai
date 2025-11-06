# Fix pour l'erreur NameError: name 'style' is not defined

# Dans ultimate_orchestrator.py, ligne 404, remplacer:
# if style == "concis":

# Par:
# style = style_data.get("style", "neutre")
# if style == "concis":