# Django Université Ben M'sick

## Project Ecommerce

1. Créer un dossier qui porte le nom du projet
1. Ouvrir le dossier dans VSCode
1. Ouvrir CMD ou Terminal (Windows/Unix)
1. Créer un environnement virtuel
    ```bash
    $ python -m venv .envEcommerce
    ```
1. Activer l'environnement
    ```bash
    $ .envEcommerce\Scripts\activate                # Windows
    $ source .envEcommerce/bin/activate             # Unix
    ```
1. Créer un fichier 'requirements.txt'
    ```python
    # requirements.txt
    django
    ```
1. Instalation des paquages
    ```bash
    $ pip3 install -r requirements.txt
    ```
1. Créer le projet django
    ```bash
    $ django-admin startproject core
    ```
1. Démarer le projet django
    ```bash
    $ python manage.py runserver
    ```
1. Créer une application django
    ```bash
    $ python manage.py startapp <app_name>
    ```
1. Créer des migrations django
    ```bash
    $ python manage.py makemigrations <app_name> # app_name est optionnel
    ```
1. Lancer les migrations
    ```bash
    $ python manage.py migrate
    ```
1. Créer un super-utilisateur
    ```bash
    $ python manage.py createsuperuser
    ```
