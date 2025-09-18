from django.db import models

class MyModel(models.Model):
    text_field = models.CharField(max_length=255)
    number_field = models.IntegerField()
    image_field = models.ImageField(upload_to='images/')
    audio_field = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.text_field
