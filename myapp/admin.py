from django.contrib import admin

# Register your models here.
from myapp.models import FileModel


class FileModelAdmin(admin.ModelAdmin):
    fields = ['key', 'time', 'file']


admin.site.register(FileModel, FileModelAdmin)


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ()
