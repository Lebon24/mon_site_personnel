from django.contrib import admin
from .models import Article, Projet, MessageContact


@admin.register(Projet)
class DomaineActiviteAdmin(admin.ModelAdmin):
	list_display = ['titre', 'technologie', 'description', 'lien_code', 'lien_demo', 'en_avant', 'date_creation']
	list_filter = ['en_avant', 'date_creation']
	list_editable = ['en_avant']

@admin.register(Article)
class Article(admin.ModelAdmin):
	list_display =['titre', 'date_publication', 'publie']
	list_filter = ['publie', 'date_publication']
	list_editable = ['publie']


@admin.register(MessageContact)
class MessageContact(admin.ModelAdmin):
	list_display = ['nom', 'email', 'message', 'date_envoi', 'lu']
	list_filter = ['lu', 'date_envoi']
	list_editable = ['lu']
	readonly_fields = ['date_envoi']