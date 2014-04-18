from fabric.api import local

def deploy():
    local("git push")
    local("git push heroku master")
