## TechnotrackSocialNet

Here is a social network sample project supporting social authentification, email interaction, browser notifications and a full-text search. 

### Key components and technologies:
  * Database: [MySQL](https://www.mysql.com/)
  * Backend: [Django REST framework](https://www.django-rest-framework.org/)
  
    - Oauth2: [Python Social Auth](https://pypi.org/project/social-auth-app-django/)
    - Email confirmation: [Django-Templated-Email](https://github.com/vintasoftware/django-templated-email) to use django models in message body + [django-email-registration](https://github.com/matthiask/django-email-registration) to organise message sending
    - Newsletter: [Django-Templated-Email](https://github.com/vintasoftware/django-templated-email) to use django models in message body + [celery](http://www.celeryproject.org/) to make sending asynchronious + [redis](https://redis.io/) to broker tasks
    - Browser notifications: [centrifuge](https://github.com/centrifugal/centrifuge)'s [adjacent wrapper](https://github.com/centrifugal/adjacent) 
    - Full-text search: [DRF-Haystack](https://drf-haystack.readthedocs.io/en/latest/) interfaces + [Whoosh](https://bitbucket.org/mchaput/whoosh/wiki/Home) backend
