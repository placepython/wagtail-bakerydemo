# Projet de démonstration Wagtail

Il s'agit d'un projet de démonstration pour le superbe [CMS Django nommé Wagtail](https://github.com/wagtail/wagtail).

Le site de démonstration est conçu pour fournir des exemples de fonctionnalités courantes et de recettes afin de vous initier au développement de Wagtail. Au-delà du code, il vous permettra également d'explorer l'interface admin/éditoriale du CMS. ==Il a par ailleurs été simplifié a partir du dépôt de code original pour servir à un webinaire sur le déploiement d'une application Django. [Vous trouverez le dépôt de code original ici](https://github.com/wagtail/bakerydemo).==

Notez que nous ne recommandons _pas_ d'utiliser ce projet pour démarrer votre propre site - la démo est conçue pour être un tremplin pour vous aider à démarrer. N'hésitez pas à copier le code de la démo dans votre propre projet.

### Fonctionnalités de Wagtail illustrées dans cette démo

Cette démo est principalement destinée aux développeurs souhaitant en savoir plus sur le fonctionnement interne de Wagtail, et suppose que vous lirez son code source. Après avoir parcouru les fonctionnalités, prêtez une attention particulière au code que nous avons utilisé pour :

- Diviser un projet en plusieurs applications
- Modèles de contenu personnalisés et "contextes" dans les applications "breads" et "locations"
- Un blog typique dans l'application "blog"
- Exemple d'utilisation d'une application "base" pour contenir diverses fonctionnalités supplémentaires (par exemple, Formulaire de Contact, À propos, etc.)
- Modèle "StandardPage" utilisant des mixins empruntés à d'autres applications
- Exemple de personnalisation de l'Admin Wagtail via _wagtail_hooks_
- Exemple d'utilisation du système de "snippets" de Wagtail pour représenter les catégories de pain, les pays et les ingrédients
- Exemple d'une fonctionnalité "Galleries" personnalisée qui récupère des images utilisées dans d'autres types de contenu du système
- Exemple de création de relations ManyToMany via la fonctionnalité Ingredients sur BreadPage
- Bien plus encore

# Installation

## Configuration avec uv

Vous pouvez exécuter cette démonstration Wagtail en utilisant uv. Si uv n'est pas installé, vous pouvez l'installer en utilisant l'[installeur standalone sur le site officiel](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer). 

### Dépendances

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- [Node.js pour l'installation de npm](https://nodejs.org/en/download/)

### Installation

```bash
cd ~/dev [ou votre répertoire dev préféré]
git clone https://github.com/placepython/wagtail-backerydemo.git bakerydemo
cd bakerydemo
uv sync --extra dev
```

Ensuite, nous configurerons nos variables d'environnement locales. Nous utilisons dans cette démo [django-environ](https://django-environ.readthedocs.io/en/latest/) 
pour nous aider dans cette tâche. Cette bibliothèque lit les variables d'environnement situées dans un fichier nommé `.env` au niveau supérieur du répertoire du projet. Renommez le fichier .env.example en .env pour avoir un modèle avec les variables attendues. Puis, définissez
les variables suivantes:
```bash
## Clé secrète et activation/Désactivation du mode DEBUG
DJANGO_SECRET_KEY=une-secrete-key
DJANGO_DEBUG=True

## Module de settings à utiliser
DJANGO_SETTINGS_MODULE=config.settings.dev

DJANGO_PRIMARY_HOST=localhost:8000
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_DATABASE_URL=sqlite:///bakerydemodb
DJANGO_EMAIL_URL=consolemail:///
DJANGO_ADMIN_URL=django-admin/
WAGTAIL_ADMIN_URL=admin/
```

Pour configurer votre base de données et charger les données initiales, exécutez les commandes suivantes :
```bash
uv run python manage.py migrate
uv run python manage.py collectstatic
uv run python manage.py load_initial_data
uv run python manage.py runserver
```

puis dans un autre terminal:
```bash
npm install
npm start
```
Visitez [la page d'acceuil du site de demo](http://127.0.0.1:8000/) 
et [connectez-vous à l'admin](http://127.0.0.1:8000/admin)  avec les identifiants `admin / changeme`.

# Autres remarques

### Remarque sur la recherche dans la démo

Comme nous ne pouvons pas (facilement) utiliser ElasticSearch pour cette démo, nous utilisons la recherche native de la base de données de Wagtail.
Cependant, la recherche native de la base de données ne peut pas rechercher des champs spécifiques dans nos modèles sur une requête généralisée `Page`.
Donc, pour les besoins de la démonstration UNIQUEMENT, nous codons en dur les noms des modèles que nous voulons rechercher dans `search.views`, ce qui n'est pas idéal. En production, utilisez ElasticSearch et une requête de recherche simplifiée, selon
[https://docs.wagtail.org/en/stable/topics/search/searching.html](https://docs.wagtail.org/en/stable/topics/search/searching.html).

### Envoi d'e-mails depuis le formulaire de contact

Le paramètre suivant dans `base.py` garantit que les e-mails réels ne sont pas envoyés par le formulaire de contact de la démo lorsque vous êtes en mode développement. `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` garantit que les e-mails seront imprimés dans le terminal.

En production, vous devrez configurer les [paramètres SMTP](https://docs.djangoproject.com/en/3.2/topics/email/#smtp-backend) appropriés pour votre fournisseur de messagerie.

### Utilisateurs inclus dans les données de la démo

Les données de la démo incluent des utilisateurs avec différents rôles et préférences. Vous pouvez utiliser ces utilisateurs pour tester rapidement le système de permissions dans Wagtail ou comment la localisation est gérée dans l'interface admin.

| Nom d'utilisateur | Mot de passe | Superutilisateur | Groupes    | Langue préférée | Fuseau horaire | Actif |
| ----------------- | ------------ | ---------------- | ---------- | --------------- | -------------- | ----- |
| `admin`           | `changeme`   | Oui              | Aucun      | non défini      | non défini     | Oui   |
| `editor`          | `changeme`   | Non              | Éditeurs   | non défini      | non défini     | Oui   |
| `moderator`       | `changeme`   | Non              | Modérateurs| non défini      | non défini     | Oui   |
| `inactive`        | `changeme`   | oui              | Aucun      | non défini      | non défini     | Non   |
| `german`          | `changeme`   | oui              | Aucun      | Allemand        | Europe/Berlin  | Oui   |
| `arabic`          | `changeme`   | oui              | Aucun      | Arabe           | Asie/Beirut    | Oui   |

### Propriété du contenu de la démo

Tout le contenu de la démo est dans le domaine public. Le contenu textuel de ce projet provient soit de Wikimedia (Wikipedia pour les articles de blog, [Wikibooks pour les recettes](https://en.wikibooks.org/wiki/Cookbook:Table_of_Contents)) soit est du lorem ipsum. Toutes les images proviennent soit de Wikimedia Commons soit d'autres sources libres de droits.
