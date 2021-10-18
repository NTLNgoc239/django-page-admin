from django.db import models
from datetime import datetime
# from simple_history.models import HistoricalRecords
# Create your models here.


class User_of_shop(models.Model):
    cid_master_shop = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    avatar = models.CharField(max_length=100, null=True)
    cid_user = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    cid_shop = models.CharField(max_length=100, null=True)
    prefix = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=100, null=True)
    is_host = models.CharField(max_length=100, null=True)
    is_pos = models.CharField(max_length=100, null=True)
    is_home = models.CharField(max_length=100, null=True)
    show_rank = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    nick_name = models.CharField(max_length=100, null=True)
    orderby_staff = models.CharField(max_length=100, null=True)
    orderby_host = models.CharField(max_length=100, null=True)
    orderby_manager = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.cid_user


class Role_login(models.Model):
    cid_user = models.CharField(max_length=100, null=False)
    role = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.role


class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    user_name = models.CharField(max_length=100, null=True)
    nick_name = models.CharField(max_length=100, null=True)
    avatar = models.CharField(max_length=100, null=True)
    identity_card = models.CharField(max_length=100, null=True)
    banner = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    password_pos = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    line = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    youtube = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    line_blog = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    height = models.CharField(max_length=100, null=True)
    blood_group = models.CharField(max_length=100, null=True)
    zodiac = models.CharField(max_length=100, null=True)
    birthday = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    cid_location = models.CharField(max_length=100, null=True)
    cid_location_child = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=100, null=True)
    role2 = models.CharField(max_length=100, null=True)
    accessed_count = models.CharField(max_length=100, null=True)
    gift_count = models.CharField(max_length=100, null=True)
    favorite_list = models.CharField(max_length=100, null=True)
    book_list = models.CharField(max_length=100, null=True)
    cid_position = models.CharField(max_length=100, null=True)
    cid_shop = models.CharField(max_length=100, null=True)
    rank_in_shop = models.CharField(max_length=100, null=True)
    notification_token = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    active = models.CharField(max_length=100, null=True)
    master_id = models.CharField(max_length=100, null=True)
    lock_code = models.CharField(max_length=100, null=True)
    check_login = models.CharField(max_length=100, null=True)
    shop_created = models.CharField(max_length=100, null=True)
    email_verified_at = models.CharField(max_length=100, null=True)
    remember_token = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    id_shop = models.CharField(max_length=200, null=False)
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
    avatar_img = models.CharField(max_length=200, null=True)
    open_time = models.CharField(max_length=200, null=True)
    close_time = models.CharField(max_length=200, null=True)
    regular_holiday = models.TextField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=True)
    contents = models.TextField(max_length=200, null=True)
    googlemap = models.CharField(max_length=200, null=True)
    banner = models.CharField(max_length=200, null=True)
    avatar_image = models.CharField(max_length=200, null=True)
    images = models.TextField(max_length=100, null=True)
    multi_images = models.TextField(max_length=100, null=True)
    slider = models.TextField(max_length=100, null=True)
    system = models.CharField(max_length=200, null=True)
    hp = models.CharField(max_length=200, null=True)
    rank_host = models.SmallIntegerField(max_length=200, null=True)
    pos_active = models.SmallIntegerField(max_length=200, null=True)
    status = models.SmallIntegerField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Store(models.Model):
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
    avatar_img = models.CharField(max_length=200, null=True)
    open_time = models.CharField(max_length=200, null=True)
    close_time = models.CharField(max_length=200, null=True)
    regular_holiday = models.TextField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=True)
    contents = models.TextField(max_length=200, null=True)
    googlemap = models.CharField(max_length=200, null=True)
    banner = models.CharField(max_length=200, null=True)
    avatar_image = models.CharField(max_length=200, null=True)
    images = models.TextField(max_length=100, null=True)
    multi_images = models.TextField(max_length=100, null=True)
    slider = models.TextField(max_length=100, null=True)
    system = models.CharField(max_length=200, null=True)
    hp = models.CharField(max_length=200, null=True)
    rank_host = models.SmallIntegerField(max_length=200, null=True)
    pos_active = models.SmallIntegerField(max_length=200, null=True)
    status = models.SmallIntegerField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        if self.date_created == None:
            self.date_created = datetime.now()
            self.date_updated = datetime.now()
        super(Store, self).save()


# class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     history = HistoricalRecords()


# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     history = HistoricalRecords()
