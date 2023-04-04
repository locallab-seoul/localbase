from django.contrib import admin

# Register your models here.
from .models import Spaces
from .models import Category

admin.site.register(Spaces)
admin.site.register(Category)