from django.shortcuts import render, redirect
from .models import Projet, Article, MessageContact
from django.http import JsonResponse
from django.contrib import messages

def accueil(request):
	projets = Projet.objects.filter(en_avant=True)[:3]
	articles = Article.objects.filter(publie=True)[:3]
	return render(request, 'main/accueil.html',{
		'projets':projets,
		'articles':articles
		})

def portfolio(request):
	projets = Projet.objects.all()
	return render(request, 'main/portfolio.html', {'projets':projets})

def blog(request):
	articles = Article.objects.filter(publie=True)
	return render(request, 'main/blog.html',{'articles':articles})

def contact(request):
	if request.method == 'POST':
		nom = request.POST.get("nom")
		email = request.POST.get("email")
		message_text = request.POST.get("message")

		MessageContact.objects.create(
			nom=nom,
			email=email,
			message=message_text
			)

		if request.headers.get('HX-Request'):
			return JsonResponse({'success': True, 'message': 'Message envoyé avec succès !'})
		else:
			messages.success(request, 'Message envoyé avec succès !')
			return redirect('contact')

	return render(request, 'main/contact.html')


def detail_article(request, article_id):
	try:
		article = Article.objects.get(id=article_id, publie=True)
	except Article.DoesNotExist:
		return render(request, "main/404.html", status=404)

	return render(request, "main/detail_article.html", {'article': article})


def handler404(request, exception):
	return render(request, 'main/404.html', status=404)
	
def handler500(request):
	return render(request, 'main/500.html', status=500)
