from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

GENDER_OPTIONS = (
    ('male','Male'),
    ('female', 'Female'),
    ('trans', 'Transgender'),
    ('na','Prefer not to say'),
)

STATE_OPTIONS = (
    ('chennai','Chennai'),
    ('coimbatore', 'Coimbatore'),
    ('salem', 'Salem'),
)

COUNTRY_OPTIONS = (
    ('india','India'),
    ('china', 'China'),
    ('japan', 'Japan'),
)

STD_OPTIONS = (
    ('1','I'),
    ('2', 'II'),
    ('3', 'III'),
    ('4', 'IV'),
    ('5', 'V'),
    ('6', 'VI'),
    ('7', 'VII'),
    ('8', 'VIII'),
    ('9', 'IX'),
    ('10', 'X'),
    ('11', 'XI'),
    ('12', 'XII'),
)

RATING_OPTIONS = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)

class Standard(models.Model):
    standard = models.IntegerField(null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(12)])

    def __str__(self):
        return str(self.standard)

class State(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=False)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        unique_together = ['state', 'country', 'place']

    def __str__(self):
        return self.state.name + ", " + self.country.name + ", " + self.place.name

class Certification(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False)

    def __str__(self):
        return self.name

class Goal(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False)

    def __str__(self):
        return self.name

class Parent(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=250, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, null=False, blank=False)

    class Meta:
        unique_together = ['name', 'email' ,'phone']

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        unique_together = ['name', 'location']

    def __str__(self):
        return self.name + ", " + self.location.state.name

class Staff(models.Model):
    name = models.TextField(max_length=150, null=False, blank=False)
    email = models.EmailField(max_length=150, unique=True, null=False, blank=False)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=False)

    class Meta:
        unique_together = ['name', 'email']

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(60)])
    sex = models.CharField(max_length=20, choices=GENDER_OPTIONS, null=False)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=False)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=False)
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    acheivement = models.TextField(max_length=1250, blank=True, null=True)
    certification = models.ForeignKey(Certification, blank=True, on_delete=models.SET_NULL, null=True)
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name + ", " + str(self.age) + ", " + self.sex

class Feedback(models.Model):
    name = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=False)
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True, blank=False)
    rating = models.CharField(choices=RATING_OPTIONS, max_length=25, null=True, blank=True)
    feedback = models.TextField(max_length=1250, default='',null=False, blank=False)

    class Meta:
        unique_together = ['name', 'standard']

    def __str__(self):
        return self.name.name