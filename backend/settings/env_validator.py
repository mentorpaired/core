import os
import sys

from dotenv import load_dotenv

load_dotenv()


def validate_env_vars(*args):
    for arg in args:
        if not os.getenv(arg):
            sys.exit(f"{arg} environment variable is required.")
