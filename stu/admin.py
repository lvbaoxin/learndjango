from django.contrib import admin
from .models import Student, Movie

# Register your models here.
admin.site.register([Student, Movie])
