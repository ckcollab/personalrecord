import sys
import os

from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site

from user_profile.models import UserProfile


class Command(BaseCommand):
    args = ''
    help = 'Creates admin account and user profile to go with it'

    def handle(self, *args, **options):
        print "%" * 80
        print " Initializing PersonalRecord!"
        print "%" * 80
        print ""

        sys.stdout.write("Creating admin...")

        # Setup admin
        u = UserProfile.objects.get_or_create(username='admin')[0]
        u.set_password('admin')
        u.email = "admin@personalrecord.net"
        u.is_superuser = True
        u.is_staff = True
        u.save()

        print "done"
