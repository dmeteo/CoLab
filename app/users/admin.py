from django.contrib import admin
from app.users.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)