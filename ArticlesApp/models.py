from django.db import models
from UsersApp.models import Badge, Tutor, Tribut, Account, Child
from django.contrib.auth.models import AbstractUser


class Equipment(models.Model):
    id_equipment = models.AutoField(primary_key=True)
    text = models.CharField(max_length=150)
    quantity = models.FloatField()
    unity = models.CharField(max_length=40)

    class Meta:
        managed = True
        db_table = 'equipment'


class Image(models.Model):
    id_image = models.AutoField(primary_key=True)
    num_apparition = models.IntegerField()
    description = models.CharField(max_length=70, blank=True, null=True)
    authors = models.CharField(max_length=60, blank=True, null=True)
    title = models.CharField(max_length=70, blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    image_article = models.ImageField(upload_to='article_image/', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'image'


class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    num_apparition = models.IntegerField()
    description = models.CharField(max_length=70)
    authors = models.CharField(max_length=60)
    title = models.CharField(max_length=70)
    publication_date = models.DateTimeField(auto_now_add=True)
    video_article = models.FileField(upload_to='article_video/', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'video'


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    id_badge = models.ForeignKey('UsersApp.Badge', db_column='id_badge', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    objectif = models.CharField(max_length=150)
    content = models.TextField()
    pedagogic_aims = models.TextField()
    victory_celebration_display = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    article_cover_image = models.ImageField(upload_to='article_cover_image/', null=True, blank=True, default='ex-par-nat_logo.png')
    success_article = models.ManyToManyField(Child, blank=True)
    list_video = models.ManyToManyField(Video, blank=True)
    list_image = models.ManyToManyField(Image, blank=True)
    list_equipement = models.ManyToManyField(Equipment, blank=True)

    class Meta:
        managed = True
        db_table = 'article'


class Author(models.Model):
    account_author = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    bibliography = models.ManyToManyField(Article)

    class Meta:
        managed = True
        db_table = 'author'
