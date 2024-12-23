from django.db import models
from django.urls import reverse

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='student_images/')

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])