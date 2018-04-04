# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Owner, Pet
admin.site.register(Owner)
admin.site.register(Pet)

# Register your models here.
