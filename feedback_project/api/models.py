import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField()
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    email = models.EmailField(
        unique=True, 
        help_text="The email address must be unique for each feedback submission."
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        help_text="The rating score must be between 1 and 10."
    )
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        managed = True
        db_table = "feedback"
