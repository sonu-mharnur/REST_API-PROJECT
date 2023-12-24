from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, auto_created=True)
    customer_name = models.CharField('name',max_length=50)
    customer_address = models.TextField()
    customer_contact = models.BigIntegerField()

    def __str__(self):
        return self.customer_name
    