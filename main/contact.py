from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        
        # Sauvegarde en base
        MessageContact.objects.create(
            nom=nom, email=email, message=message_text
        )
        
        # Envoi d'email de notification
        sujet = f"Nouveau message de {nom}"
        contenu = f"""
        Nom: {nom}
        Email: {email}
        Message: {message_text}
        """
        
        send_mail(
            sujet,
            contenu,
            settings.DEFAULT_FROM_EMAIL,
            ['votre.email@domaine.com'],  # Votre email ici
            fail_silently=False,
        )
        
        # ... reste du code ...