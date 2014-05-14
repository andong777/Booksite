__author__ = 'andong'

from django.contrib import admin
from App.models import *

admin.site.register(Writer)
admin.site.register(Press)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Comment)