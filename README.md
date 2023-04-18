# IBM_Server
IBM application backend in Django (School Project)

to run the server 

    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
