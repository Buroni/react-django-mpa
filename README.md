# react-django-mpa

## Setup
In repo root directory, install dependencies and run migrations:
```
npm i --dev
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Run the Django project:
```
python manage.py runserver
```

Run the webpack bundler:
```
npm run watch
```

