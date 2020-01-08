from django.db import models
class Gym(models.Model):
    Workout_Name = models.CharField(max_length = 50)
    Image = models.ImageField()
    Username = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    Workout_Description = models.TextField(default = 'DataFlair Django tutorials')

    def __str__(self):
        return self.Workout_Name