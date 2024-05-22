from django.db import models
from app.models import CustomUser

class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_notifications', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='received_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
