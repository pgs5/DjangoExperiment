from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Sheet(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    composer = models.TextField()
    sheet_pdf = models.FileField( default = 'default.jpg', upload_to = 'sheet_music')
    initial_key = models.CharField(max_length=16)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    def save(self):
        super().save()
        #pdf = Reader(open(self.sheet_pdf.path, 'rb'))
