# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class variant(models.Model):
    local_id = models.CharField(max_length=200, null=True)
    linking_id = models.CharField(max_length=200, primary_key=True)

    # gene
    reference_sequence = models.CharField(max_length=200)

    # variant definition
    hgvs = models.CharField(max_length=200)

    def __str__(self):
        return self.linking_id
