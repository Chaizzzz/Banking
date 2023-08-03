from django.contrib import admin
from .models import District,SubDistrict,AccountType

# Register your models here.
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(AccountType)