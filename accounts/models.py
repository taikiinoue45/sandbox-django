from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta(object):
        db_table = "user"

    login_count = models.IntegerField(verbose_name="ログイン回数", default=0)

    def post_login(self):

        self.login_count += 1
        self.save()

