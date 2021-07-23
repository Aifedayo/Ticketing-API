from django.db import models
import uuid
from django.contrib.auth.models import User

def generate_ticket_id():
    # Generating a unique ticket id
    return str(uuid.uuid4()).split("-")[-1]
