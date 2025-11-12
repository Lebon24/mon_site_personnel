from django.urls import path
from. import views

urlpatterns = [
	path('', views.accueil, name='accueil'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('blog/', views.blog, name='blog'),
	path('blog/<int:article_id>/', views.detail_article, name='detail_article'),
	path('contact/', views.contact, name='contact'),
]