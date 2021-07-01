from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from backend.ArticlesApp.models import


# Create your models here.


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
    id_tribut = models.ForeignKey('Tribut', models.DO_NOTHING, db_column='id_tribut')
    username = models.CharField(max_length=70)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image_profil = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateTimeField()
    date_jointed = models.DateTimeField()
    pwd = models.CharField(max_length=3)

    class Meta:
        managed = True
        db_table = 'child'


class Users(AbstractUser, models.Model):
    # USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and blank to false
    # REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS
    id = models.AutoField(primary_key=True)
    id_tribut = models.ForeignKey('Tribut', models.DO_NOTHING, db_column='id_tribut', null=True)
    image_profil = models.CharField(max_length=100, blank=True, null=True)
    is_author = models.BooleanField(null=True)

    class Meta:
        managed = True
        db_table = 'users'


class Tribut(models.Model):
    id_tribut = models.AutoField(primary_key=True)
    tribut_name = models.CharField(max_length=100)

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


class TutorLink(models.Model):
    id_tutor_link = models.AutoField(primary_key=True)
    id_child = models.ForeignKey(Child, models.DO_NOTHING, db_column='id_child')
    id_users = models.ForeignKey(Users, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = True
        db_table = 'tutor_link'

