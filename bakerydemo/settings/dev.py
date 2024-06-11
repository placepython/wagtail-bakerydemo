"""
Projet: BakeryDemo

Configuration de développement.

Pour plus d'information, la liste complète des variables de configuration est
disponible dans la doc officielle ici:
https://docs.djangoproject.com/fr/5.1/ref/settings/
"""

from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from .base import env

# DEBUG:
# En développement, on active le mode DEBUG
# https://docs.djangoproject.com/fr/5.1/ref/settings/#debug
DEBUG = True

# Clé secrète de l'installation Django. Elle est utilisée dans le contexte de
# la signature cryptographique, et doit être définie à une valeur unique et
# non prédictible.
# https://docs.djangoproject.com/fr/5.1/ref/settings/#std-setting-SECRET_KEY
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="3E9AEJf1l1JNJnTwPmwhkKCpGgD6RP8rNALkFyqnhLs",
)

# ALLOWED_HOSTS:
# Une liste de chaînes représentant des noms de domaine/d’hôte que ce site
# Django peut servir. C’est une mesure de sécurité pour empêcher les attaques
# d’en-tête Host HTTP, qui sont possibles même avec bien des configurations de
# serveur web apparemment sécurisées.
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS", default=["localhost", "0.0.0.0", "127.0.0.1"]
)

# EMAIL
# Configuration de l'email. Par défaut, les courriels sont affichés dans le
# le terminal.
# Pour définir un back-end d'envoi d'emails, définir la variable d'environnement
# DJANGO_EMAIL_URL avec les valeurs suivantes:
# - SMTP avec SSL: smtp+ssl://USER:PASSWORD@HOST:PORT
# - SMTP avec STARTTLS: smtp+tls://USER:PASSWORD@HOST:PORT
# - Console: consolemail://
# https://docs.djangoproject.com/fr/5.1/ref/settings/
EMAIL_BACKEND = env.email(
    "DJANGO_EMAIL_URL",
    default="consolemail://",
)

# DJANGO-DEBUG-TOOLBAR
# La Django Debug Toolbar est un outil de débogage qui s'intègre à Django pour
# afficher des informations détaillées sur les requêtes, les bases de données,
# les templates, les vues et bien d'autres aspects:
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# La barre d'outils de débogage ne s'affiche que si votre adresse IP figure
# dans le paramètre INTERNAL_IPS de Django.
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

# Ce dictionnaire contient toutes les autres options de configuration de
# Django-Debug-Toolbar. Certaines s'appliquent à la barre d'outils elle-même,
# d'autres sont spécifiques à certains panneaux.
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        # Désactive le panneau de profilage à cause d'un problème avec Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}

DJANGO_ADMIN_URL = env("DJANGO_ADMIN_URL", default="django-admin/")
WAGTAIL_ADMIN_URL = env("WAGTAIL_ADMIN_URL", default="admin/")

try:
    from .local import *  # noqa
except ImportError:
    pass
