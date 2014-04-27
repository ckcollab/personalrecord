from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel


class Set(models.Model):
    # Person field is only to be used when there is no user assigned to the lift, this is just a regular old personal
    # record
    person = models.TextField(null=True, blank=True)
    workout = models.ForeignKey('workout.Workout', related_name='sets')
    bodyweight = models.IntegerField()
    tags = models.TextField(null=True, blank=True)
    exercise = models.TextField()
    weight = models.FloatField()
    reps = models.IntegerField()
    notes = models.TextField(null=True, blank=True)
    video_youtube_url = models.TextField(null=True, blank=True)
    video_local_file_name = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s %slbs for %s" % (self.exercise, self.weight, self.reps)

    def save(self, **kwargs):
        self.exercise = self.exercise.lower()

        super(Set, self).save(**kwargs)


class Workout(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    bodyweight = models.IntegerField()
