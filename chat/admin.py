# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from chat.models import user,message,allconnection

# Register your models here.

admin.site.register(user)
admin.site.register(message)
admin.site.register(allconnection)
