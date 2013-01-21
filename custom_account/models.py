from django.db import models

from account.models import Account

class CustomAccount(Account):
    terms_and_conditions = models.BooleanField()