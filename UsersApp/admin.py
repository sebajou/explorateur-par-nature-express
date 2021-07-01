from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Badge, Tribut, Child, Trophies, TutorLink


admin.site.register(Trophies)
admin.site.register(Badge)
admin.site.register(Tribut)
admin.site.register(Child)
admin.site.register(TutorLink)
admin.site.register(Users, UserAdmin)
