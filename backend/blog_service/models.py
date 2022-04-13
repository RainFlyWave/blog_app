from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator



# Simple concept of User model.
# Passwords are stored in plain text 



class Entry(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_entry = models.TextField(max_length=512)
    date_created = models.DateTimeField(default=now)





class EntryStats(models.Model):
    """Model that stores amount of every user"""
    
    # entry_date_created = custom Field in progress
    entry_author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_amount = models.IntegerField(validators=[
        MaxValueValidator(255)
    ])

