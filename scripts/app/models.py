from django.db import models


class Account(models.Model):
    account_number = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    # Дополнительные поля для корректировки данных
    reading = models.DecimalField(max_digits=10, decimal_places=2)
    stamp = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.account_number
