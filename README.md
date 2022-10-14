# Django GraphQL Schema-first Barebone using Ariadne

## Installing application

1. Clone project:
```
git clone https://github.com/anisimovih/DjangoJWTEmailBarebone
```

2. Setup empty python virtual environment
```
virtualenv -p python3.8 .venv
source .venv/bin/activate
```

3. Install project requirements to your local virtual environment:
```
pipenv install --dev
```

4. Migrate database scheme:
```
python manage.py migrate
python manage.py createsuperuser
```

5. Start server:
```
python manage.py runserver 127.0.0.1:8000
```


## Using application

Go to url: http://127.0.0.1:8000/graphql/