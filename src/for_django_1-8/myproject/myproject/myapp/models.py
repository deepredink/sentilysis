# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    upload_to='documents'+'\\'
    #upload_to=upload_to.replace("/", "\/")
    #upload_to=upload_to.replace("/"," ")
    docfile = models.FileField(upload_to)