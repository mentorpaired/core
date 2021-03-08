"""Settings package initialization."""

import os
from dotenv import load_dotenv

from backend.settings.env_validator import validate_env_vars

load_dotenv()

# Ensure development settings are not used in testing and production:
if os.getenv("ENVIRONMENT") == "PRODUCTION":
    from .production import *
elif os.getenv("GITHUB_WORKFLOW"):
    from .test import *
else:
    from .local import *

validate_env_vars(
    "SOCIAL_AUTH_GITLAB_KEY",
    "SOCIAL_AUTH_GITLAB_SECRET",
    "SOCIAL_AUTH_GITHUB_KEY",
    "SOCIAL_AUTH_GITHUB_SECRET",
)
