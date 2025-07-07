from django.db import models

class Correction(models.Model):
    user_id = models.CharField(max_length=100)
    original_prediction = models.CharField(max_length=10)
    corrected_label = models.CharField(max_length=10)
    image = models.ImageField(upload_to='corrections/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} corrected {self.original_prediction} → {self.corrected_label}"
