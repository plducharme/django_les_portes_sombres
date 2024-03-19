# À porter attention

## Mappage de urls
voir les commentaires dans le fichier django_les_portes_sombres/urls.py

## Création du modèle
- voir les commentaires dans aventure_web/models.py
- Pour générer automatiquement les tables à partir du modèle défini  
> python manage.py makemigrations  
  - Peut aussi être fait pour un app django en particulier: 
  ```
  python manage.py makemigrations <app>
  ```
- Applique les migrations de BD si nécessaire 
> python manage.py migrate  

## Passer des données à un template
- Remarquer la structure du répertoire "templates" dans aventure_web
- Voir les commentaires des fichiers aventure_web/views.py et aventure_web/templates/aventure_web/index.html
- On peut passer des données:
  - soit en passant un context (dictionnaire) à la réponse pour cette requête
  - soit en utilisant des variables mises en session

## Utilisation de forms
voir aventure_web/forms.pu et voir aventure_web/views.py
- exemple de validation de forms
- exemple d'envoyer des données dans le contexte pour y accéder dans le formulaire
- exemple de mettre des variables dans la session

# Ajout du support Bootstrap5 pour le style
1) installer le package django-bootstrap5
2) dans settings.py, ajouter l'app "django-bootstrap5"
3) L'utiliser dans un template, voir aventure_web/templates/aventure_web/intro.html