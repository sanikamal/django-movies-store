from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    # list_display = ('name', 'release_year', 'price')
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
