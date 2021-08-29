from django.contrib import admin
from .models import TODOModel


@admin.register(TODOModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
