from django.db import models

# Create your models here.


class reservation_form(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    occasion = models.CharField(max_length=50, null=True)
    date_and_time = models.CharField(max_length=50)
    message = models.TextField(null=True)

    class Meta:
        db_table = 'reservation_form'
