# -*- coding: utf-8 -*-
from django.db import models


class RDFModel(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return f"<id={self.pk}, name={self.name}>"


class InstanceModel(models.Model):
    type_ = models.ForeignKey('RDFModel', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

