import uuid
from django.db import models

# Create your models here.

class BaseMixin(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True,editable=False,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,editable=False,null=True,blank=True)
    
    class Meta:
        abstract = True