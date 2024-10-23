import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.getenv("DJANGO_ENV_FILE", str(BASE_DIR / ".env")))
