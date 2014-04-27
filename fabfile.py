import sys
from fabric.api import local, hide

def deploy():
    _title_text(" Deploying")

    with hide('running', 'stdout', 'output'):
        sys.stdout.write("Pushing github...")
        local("git push")
        print "done"

        sys.stdout.write("Pushing heroku...")
        local("git push heroku master")
        print "done"

        sys.stdout.write("Running heroku migrations...")
        local("heroku run python manage.py syncdb --migrate")
        print "done"


def fresh_db():
    _title_text(" Starting from scratch!")

    with hide('running', 'stdout'):
        sys.stdout.write("Dropping database...")
        local('psql -U postgres -c "DROP DATABASE IF EXISTS personalrecord"')
        print "done"

        sys.stdout.write("Creating database...")
        local('psql -U postgres -c "CREATE DATABASE personalrecord"')
        print "done"

        sys.stdout.write("Syncdb and migrate...")
        local('python manage.py syncdb --noinput')
        local('python manage.py migrate')
        print "done"

        sys.stdout.write("Initializing facebook and admin...")
        local('python manage.py init')
        print "done"


def _title_text(title):
    print "%" * 80
    print title
    print "%" * 80
    print ""
