# Blogcentral⚡

#### Description

> Blogcentral is a CMS application to manage users only where people can share ideas and discuss any topic. A place to share your thoughts and opinions on the topic at hand.

#### Architecture
- Monolithic Architecture

#### Design Pattern
- MVT(Model View Template)

#### Tools & Technologies
- Backend - Django Framework
- Frontend - HTML, CSS, JavaScript
- Database - PostgreSQL
- Versioning - Git, Github
- Hosting - Pythonanywhere[http://www.pythonanywhere.com]

### Quick Start

1. Migrate Command
```
python manage.py makemigrations
python manage.py migrate
```

2. Collect Static Files
```
python manage.py collectstatic
```

3. Run Server
```
python manage.py runserver
```
#### (Note - If you are using django-admin you need to create a super user)
```
python manage.py createsuperuser
```