from django.db import models

class Lesson(models.Model):
    group = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    dance = models.CharField(max_length=20)
    start = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    closed = models.BooleanField()

    def __unicode__(self):
        return self.day + self.start

