from django.contrib import admin
from .models import Article, Equipment, Image, Video, Author


admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Equipment)
admin.site.register(Image)
admin.site.register(Video)
