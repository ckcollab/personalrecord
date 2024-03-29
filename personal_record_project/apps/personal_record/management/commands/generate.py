import random
import sys

from django.core.management.base import BaseCommand

from workout.models import Set, Workout


class Command(BaseCommand):
    args = ''
    help = 'Creates admin account and user profile to go with it'

    def handle(self, *args, **options):
        exercises = ('back squat', 'deadlift', 'front squat', 'bench press')
        workout = Workout.objects.get_or_create(user_id=1, pk=1, bodyweight=100, gender="male")[0]

        print "%" * 80
        print " Generating 200 lifts"
        print "%" * 80
        print ""

        sys.stdout.write("Creating lifts...")

        for i in range(0, 200):
            new_set = Set.objects.create(
                gender=random.choice(('male', 'female')),
                exercise=random.choice(exercises),
                bodyweight=random.randrange(80, 345),
                weight=random.randrange(45, 765, 5),
                reps=random.randrange(1, 18),
                workout=workout
            )

        print "done"
