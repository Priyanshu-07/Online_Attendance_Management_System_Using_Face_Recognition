from django.db import models
from django.urls import reverse
import os


class stud(models.Model):

    def update_filename(self, filename):
        path = "student_images/"
        format = '%s.jpg' % self.roll_no
        return os.path.join(path, format)

    roll_no = models.CharField(max_length=255)
    stud_image = models.ImageField( null=True, blank=False, upload_to= update_filename)


    def __str__(self):
        return self.roll_no

    def get_absolute_url(self):
        return reverse('home')

