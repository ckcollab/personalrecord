import sys
from fabric.api import local, hide

def deploy():
    local("git push")
    local("git push heroku master")

def fresh_db():
    print "%" * 80
    print " Starting from scratch!"
    print "%" * 80
    print ""

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
