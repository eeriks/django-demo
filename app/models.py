from django.db import models


class ParentModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=False)
    modified = models.DateTimeField(auto_now=True)


class ChildModel(ParentModel):
    some_field = models.CharField(max_length=12)
