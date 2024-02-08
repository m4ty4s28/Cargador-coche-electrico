from django.db import models
from django.contrib.auth.models import User

class ChargePoint(models.Model):
    class Choice_status(models.TextChoices):
        READY = "ready", "Ready"
        CHARGING = "charging", "Charging"
        WAITING = "waiting", "Waiting"
        ERROR = "error", "Error"
    #[ready, charging, waiting, error])
    name = models.CharField(max_length = 32)
    status = models.CharField(
        max_length=10,
        choices=Choice_status.choices,
        default=Choice_status.READY
    )
    created_at = models.DateTimeField(blank = True, null=True)
    deleted_at = models.DateTimeField(blank = True, null=True)

    def __str__(self):
        return self.name