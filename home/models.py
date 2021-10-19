from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):
#     class Meta:
#         app_label = 'home'
#         db_table = 'users'

# class User(AbstractUser):
#     status = models.CharField(max_length=12,unique=True)
#     USERNAME_FIELD = 'status'

class Shop(models.Model):
    name = models.CharField(max_length=200, null=False)
    alias = models.CharField(max_length=200, null=True)
    cid_location = models.IntegerField(null=True)
    job_name = models.CharField(max_length=200, null=True)
    cid_user = models.CharField(max_length=200, null=True)
    cid_career = models.IntegerField(null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    lat = models.CharField(max_length=200, null=True)
    lng = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    social = models.TextField(max_length=200, null=True)
    open_time = models.CharField(max_length=200, null=True)
    close_time = models.CharField(max_length=200, null=True)
    regular_holiday = models.TextField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=True)
    contents = models.TextField(max_length=200, null=True)
    google_map = models.CharField(max_length=200, null=True)
    banner = models.CharField(max_length=200, null=True)
    avatar_image = models.CharField(max_length=200, null=True)
    images = models.TextField(max_length=100, null=True)
    multi_images = models.TextField(max_length=100, null=True)
    slider = models.TextField(max_length=100, null=True)
    system = models.CharField(max_length=200, null=True)
    hp = models.CharField(max_length=200, null=True)
    ranking_host = models.SmallIntegerField(null=True)
    pos_active = models.SmallIntegerField(null=True)
    status = models.SmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        # app_label = 'home'
        db_table = 'hc_shop'
    def __str__(self):
        return self.name

