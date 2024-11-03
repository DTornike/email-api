from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings


class Email(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='sent_emails', on_delete=models.CASCADE)
    recipients = models.ManyToManyField(User, related_name='received_emails')
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def save(self, *args, **kwargs):
        attachments_dir = os.path.join(settings.MEDIA_ROOT, 'attachments')
        if not os.path.exists(attachments_dir):
            os.makedirs(attachments_dir)

        super(Email, self).save(*args, **kwargs)

    def __str__(self):
        return self.subject
