from fabric.api import local

def deploy():
    local("git push")
    local("git push heroku master")

def fresh_db():
    # destroy db
    # python manage.py syncdb --noinput
    # python manage.py migrate
    pass
