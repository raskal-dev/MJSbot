import logging

logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Créer un gestionnaire de journalisation pour la console (affiche les logs dans la console)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Récupérer le logger racine et ajouter le gestionnaire de la console
logger = logging.getLogger()
logger.addHandler(console_handler)
