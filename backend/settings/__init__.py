"""Settings package initialization."""

from dotenv import load_dotenv

load_dotenv()

# Ensure development settings are not used in testing and production:
if os.getenv('ENVIRONMENT') == 'PRODUCTION':
    from .production import *
elif os.getenv('ENVIRONMENT') == 'TRAVIS':
    from .test import *
else:
    from .local import *
