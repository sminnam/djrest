#!/usr/bin/env python
# encoding: utf-8
"""
admin.py
"""

from multipart_form_data.models import MyFiles
from django.contrib import admin

class FilesAdmin(admin.ModelAdmin):
    list_display = ('created', 'docfile')

admin.site.register(MyFiles, FilesAdmin)
