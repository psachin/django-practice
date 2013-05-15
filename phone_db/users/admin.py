from django.contrib import admin

from users.models import FullName, Emp, Record

admin.site.register(FullName)
admin.site.register(Emp)
admin.site.register(Record)


