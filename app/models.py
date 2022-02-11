from django.db import models


class SomeBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class OtherModel(SomeBaseModel):
    some_field = models.CharField(max_length=12)
