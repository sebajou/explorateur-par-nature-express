from .models import Tutor, Badge, Tribut, Child, Trophies, TutorLink
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


admin.site.register(Trophies)
admin.site.register(Badge)
admin.site.register(Tribut, UserAdmin)
admin.site.register(Child)
admin.site.register(TutorLink)
admin.site.register(Tutor)
