from django.contrib import admin

# Register your models here.
from djhuskyapp.models import Party, Song
admin.site.register(Party)
admin.site.register(Song)
