from django.db import models
from django.contrib.auth.models import User

# Note model - har sticky note ka structure yahan define hai
class Note(models.Model):
    # Note ka title - zyada se zyada 200 characters
    title = models.CharField(max_length=200)

    # Note ka asli content / body
    content = models.TextField()

    # Note card ka background color - default yellow sticky note color
    color = models.CharField(max_length=7, default='#FFFF99')

    # Jab note pehli baar bana, woh time automatically save hoga
    created_at = models.DateTimeField(auto_now_add=True)

    # Jab bhi note update ho, yeh time khud update ho jata hai
    updated_at = models.DateTimeField(auto_now=True)

    # Yeh note kis user ka hai - user delete ho to note bhi delete ho
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        # Admin panel mein note ka title dikhega
        return self.title

    class Meta:
        # Naye notes pehle dikhein - updated time ke hisaab se sort
        ordering = ['-updated_at']
