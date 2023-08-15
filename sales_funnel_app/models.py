from django.db import models
from django.utils import timezone

class Lead(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default="Unknown Company")  # Add default value
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status_choices = (
        ('NEW', 'New Lead'),
        ('CONTACTED', 'Contacted'),
        ('QUALIFIED', 'Qualified'),
        ('CONVERTED', 'Converted'),
        ('LOST', 'Lost'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
