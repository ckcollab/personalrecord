import os

from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

from user_profile.models import UserProfile


class Command(BaseCommand):
    args = ''
    help = 'Creates admin account and user profile to go with it'

    def handle(self, *args, **options):
        print "Creating Admin"
        # Setup admin
        u = UserProfile.objects.get_or_create(username='admin')[0]
        u.set_password('admin')
        u.email = "admin@personalrecord.net"
        u.is_superuser = True
        u.is_staff = True
        u.save()

        print " --> Created admin//admin"

        print "Creating Facebook allauth settings"

        # Setup Facebook
        FACEBOOK_API_CLIENT_ID = os.environ.get("FACEBOOK_API_CLIENT_ID", None)
        FACEBOOK_API_SECRET = os.environ.get("FACEBOOK_API_SECRET", None)

        if not FACEBOOK_API_CLIENT_ID or not FACEBOOK_API_SECRET:
            raise ValueError("Facebook env vars not set!")

        facebook, created = SocialApp.objects.get_or_create(
            provider="facebook",
            name="facebook",
            client_id=FACEBOOK_API_CLIENT_ID,
            secret=FACEBOOK_API_SECRET,
        )
        facebook.sites.add(Site.objects.get_current())

        print " --> Created SocialApp for Facebook"
