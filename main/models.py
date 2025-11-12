from django.db import models
from django.urls import reverse


class Projet(models.Model):
	CATEGORIE_CHOICES = [
		('developpement', 'Developpement'),
		('design', 'Design & Infographie'),
	]
	titre = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='projets/', blank=True, null=True)

	categorie = models.CharField(
		max_length=20,
		choices=CATEGORIE_CHOICES,
		default='developpement'
		)

	technologie = models.CharField(max_length=200)
	lien_demo = models.URLField(blank=True)
	lien_code = models.URLField(blank=True)
	date_creation = models.DateTimeField(auto_now_add=True)
	en_avant = models.BooleanField(default=False)

	def __str__(self):
		return self.titre

class Article(models.Model):
	titre = models.CharField(max_length=200)
	contenu = models.TextField()
	date_publication = models.DateTimeField(auto_now_add=True)
	publie = models.BooleanField(default=True)

	def __str__(self):
		return self.titre

class MessageContact(models.Model):
	nom = models.CharField(max_length=100)
	email = models.EmailField()
	message = models.TextField()
	date_envoi = models.DateTimeField(auto_now_add=True)
	lu = models.BooleanField(default=False)

	def __str__(self):
		return f"Message de {self.nom}"
