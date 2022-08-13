
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


    # A tuple of 2-tuples
SOAPS = (
    ('D', 'Dove'),
    ('P', 'PetSmart Brand'),
    ('H', 'Head and Shoulders'),
    ('B', 'Brawny'),
    ('L', 'Lysol')
)
# new code above

# Create your models here.
class Dirt(models.Model):
    consistency = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.consistency} {self.color}"
    def get_absolute_url(self):
        return reverse('dirt_detail', kwargs={'pk': self.id})


class Rock(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    grams = models.IntegerField()
    dirt = models.ManyToManyField(Dirt)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.name} ({self.id})'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'rock_id': self.id})
    def cleaned_for_today(self):
        return self.cleaning_set.filter(date=date.today()).count() >=len(SOAPS)


class Cleaning(models.Model):
    date = models.DateField('cleaning date')
    soap = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=SOAPS,
        default=SOAPS[0][0]
    )
    rock = models.ForeignKey(Rock, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date']
    # set the default value for meal to be 'B'
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_soap_display()} on {self.date}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    rock = models.ForeignKey(Rock, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for rock_id: {self.rock_id} @{self.url}"