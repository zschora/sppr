from django.contrib import admin
from .models import User, Artist

# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
  list_display = ('User_id', 'Artist_id', 'Scrobbles')

@admin.register(Artist)
class Artist(admin.ModelAdmin):
  list_display = ('Artist_id', 'Artist_name')