from django.core.management.commands import createsuperuser
from django.utils.translation import gettext_lazy as _
from Account.models import User  # Make sure to import your custom user model
from django.db import models

class Command(createsuperuser.Command):
    help = "Create a superuser for the system"

    def handle(self, *args, **options):
        # Set the 'username' option to None
        options['username'] = None
        # Ensure the email field is set as a required field instead of 'username'
        options['email'] = options.get('email') or input("Email: ")

        # Call the parent class handle method
        super().handle(*args, **options)
