from msilib.schema import PublishComponent
from django.db import models
import datetime
# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name= models.CharField(max_length=50)
    desc= models.CharField(max_length=300)
    Pub_date=models.DateField