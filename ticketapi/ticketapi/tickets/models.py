from django.db import models
import uuid
from django.contrib.auth.models import User

def generate_ticket_id():
    # Generating a unique ticket id
    return str(uuid.uuid4()).split("-")[-1]


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)