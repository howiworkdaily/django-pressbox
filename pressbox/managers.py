from django.db import models
from django.db.models.query import QuerySet
import datetime

class PressItemManager(models.Manager):
    """
    A basic ''Manager'' subclass. It provides access to helpful utility methods.  
    """
    
    def active(self,):
        qs = self.get_query_set().filter(is_active__exact=True)
        return qs
