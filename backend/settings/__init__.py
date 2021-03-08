"""Settings package initialization."""

import os
from dotenv import load_dotenv
import sys

load_dotenv()

# Ensure development settings are not used in testing and production:
if os.getenv("ENVIRONMENT") == "PRODUCTION":
    from .production import *
elif os.getenv("GITHUB_WORKFLOW"):
    from .test import *
else:
    from .local import *

if not os.getenv("SOCIAL_AUTH_GITLAB_KEY") and not os.getenv(
    "SOCIAL_AUTH_GITLAB_SECRET"
):
    sys.exit("Exiting!")
