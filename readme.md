## Installation de Django sur Heroku avec ces instructions :

https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4

github : https://github.com/140ch204/djangoherokuapp

Lancement local : 
>
> $ source env/bin/activate
>
> $ cd djangoherokuapp
>
> $ ./manage.py runserver
>


# Variables à définir dans le .env en local ou varaiable d'env Heroku : 




Installation : 

mkdir djangoherokuapp

cd djangoherokuapp

git clone https://github.com/140ch204/djangoherokuapp

virtualenv env -p python3

source env/bin/activate

cd djangoherokuapp 

touch .env 

DATABASE_URL= sqlite:///db.sqlite3
DISABLE_COLLECTSTATIC = "1"
ENV_SECRET_KEY = ''
DEBUGMODE_ACTIVATED = "1"
ENV_LOCALHOST = "1"


+ lancement local


pip install -r requirements.txt






# Console Django

./manage.py shell


User.objects.all()

u = User.objects.get(username='joe')
u.set_password('new password')
u.save()