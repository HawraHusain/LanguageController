from django.db import models

# Create your models here.
class Country(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5, unique=True)
    countries = models.ManyToManyField(Country, related_name='languages')

    def __str__(self):
        return self.name

class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='words')
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.word} ({self.language.code})"
