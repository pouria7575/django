# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Expense,Income,Token

admin.site.register(Expense)

admin.site.register(Income)

admin.site.register(Token)

