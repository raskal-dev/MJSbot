
class Config(object):
    """Configuration de l'application"""
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()

    #: Flask configuration
    APP_NAME = "Messenger Boot"
    APP_PORT = int(environ.get('APP_PORT', 8011))
    APP_HOST = environ.get('APP_HOST', 'localhost')

    #: Facebook configuration
    ACCESS_TOKEN = 'EAAL5ZBOl7IuABOzgPnCeRfKCJqPAupEu8zXT2UPZAwKnZCcNZCnzrZBGPZCO3658MWZAZAuKa1xiatnYZC7ohlFpE4xxfCiqK4YpNT4Pc9UxqJysa1sAjkCmwaELb4RdmLXBKYIM5onTtgRGJXK0Sd0EgJgllRZBvHxoy3Qcl2cYzy9VNCjZBIvMNoPnrj1WcZAJEbRc'
    VERIFY_TOKEN = 'mjs202309S'
    URL_API = "http://127.0.0.1:8000/api/inscription"

    #: Contexte path configuration
    CONTEXTE_PATH = environ.get('CONTEXTE_PATH', '/webhook')

    #: Loggin
    MESSAGE_LOGIN = f"*: STARTING BOT SERVER on {APP_PORT}"

    #: DATE
    PASS_DATE = "01/01/01"

