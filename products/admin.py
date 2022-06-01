from django.contrib import admin
from.models import *
# Register your models here.

class cat(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
admin.site.register(category,cat)

class prod(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ['name','price','offerprice','avilability']
    list_editable = ['price','offerprice','avilability']
admin.site.register(productstable,prod)