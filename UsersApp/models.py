from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from PIL import Image
from io import BytesIO
from django.core.files import File
# from sorl.thumbnail import ImageField, get_thumbnail
# from backend.ArticlesApp.models import


# Create your models here.


class Account(AbstractUser, models.Model):
    id_account = models.AutoField(primary_key=True)
    is_tribut = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'account'


class Badge(models.Model):
    id_badge = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    level = models.IntegerField()
    type = models.CharField(max_length=40)
    filefield = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'badge'


class Child(models.Model):
    id_child = models.AutoField(primary_key=True)
    account_tribut = models.ForeignKey('Tribut', models.DO_NOTHING, db_column='account_tribut_id', null=False)
    child_username = models.CharField(max_length=70)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_jointed = models.DateTimeField(auto_now_add=True)
    # trophies = models.ManyToManyField(Badge)
    image_profile_child = models.ImageField(upload_to='profile_image/', null=True, blank=True,
                                       default='elephant.jpeg')

    # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        new_image = self.reduce_image_size(self.image_profile_child)
        self.image_profile_child = new_image
        super().save(*args, **kwargs)

    def reduce_image_size(self, image_profile_child):
        size = 500, 500
        print("reduced")
        img = Image.open(image_profile_child)
        thumb_io = BytesIO()
        # Resize/modify the image
        width = img.width
        height = img.height
        ratio = width / height
        new_width = 750
        new_height = int(new_width / ratio)
        img = img.resize((new_width, new_height))
        img.save(thumb_io, 'jpeg', quality=90)
        new_image = File(thumb_io, name=image_profile_child.name)
        return new_image

    class Meta:
        managed = True
        db_table = 'child'


class Tutor(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    id_tutor = models.AutoField(primary_key=True)
    account_tribut = models.ForeignKey('Tribut', models.DO_NOTHING, db_column='account_tribut_id', null=False)
    tutor_username = models.CharField(max_length=70)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_jointed = models.DateTimeField(auto_now_add=True)
    is_author = models.BooleanField(null=True)
    image_profile_tutor = models.ImageField(upload_to='profile_image/', null=True, blank=True,
                                       default='elephant.jpeg')

    # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        new_image = self.reduce_image_size(self.image_profile_tutor)
        self.image_profile_tutor = new_image
        super().save(*args, **kwargs)

    def reduce_image_size(self, image_profile_tutor):
        size = 500, 500
        print("reduced")
        img = Image.open(image_profile_tutor)
        thumb_io = BytesIO()
        # Resize/modify the image
        width = img.width
        height = img.height
        ratio = width / height
        new_width = 750
        new_height = int(new_width / ratio)
        img = img.resize((new_width, new_height))
        img.save(thumb_io, 'jpeg', quality=90)
        new_image = File(thumb_io, name=image_profile_tutor.name)
        return new_image

    class Meta:
        managed = True
        db_table = 'tutor'


class Tribut(models.Model):
    account_tribut = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        managed = True
        db_table = 'tribut'


class Trophies(models.Model):
    id_trophies = models.AutoField(primary_key=True)
    id_child = models.ForeignKey(Child, models.DO_NOTHING, db_column='id_child')
    id_badge = models.ForeignKey(Badge, models.DO_NOTHING, db_column='id_badge')

    class Meta:
        managed = True
        db_table = 'trophies'
