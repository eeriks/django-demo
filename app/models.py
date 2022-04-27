from django.db import models


class ParentModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=False)
    modified = models.DateTimeField(auto_now=True)
    one_to_one_relation = models.OneToOneField("RelatedModel", on_delete=models.CASCADE)


class ChildModel(ParentModel):
    some_field = models.CharField(max_length=12)


class RelatedModel(models.Model):
    some_field = models.CharField(max_length=12)