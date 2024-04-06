from django.db import models

class Conversation(models.Model):
    question = models.TextField()
    answer = models.TextField()
    ip_address = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)