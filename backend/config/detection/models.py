
from django.db import models


class ThreatDetection(models.Model):
    ip_address = models.CharField(max_length=45)
    failed_attempts = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    threat = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address
