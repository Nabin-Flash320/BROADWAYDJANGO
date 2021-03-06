from django.shortcuts import render
from . import models



# Create your views here.
def base():
    views_dict = dict()
    views_dict['feedbacks'] = models.FeedBack.objects.all()
    views_dict['services'] = models.OfferedServices.objects.all()
    views_dict['informations'] = models.Informations.objects.all().order_by('-id')[0:1]
    return views_dict

def home(request):
    views_dict = dict()
    
    return render(request, 'index.html', base())

def about(request):
    return render(request, 'about.html')

def contact(request):
    views_dict = dict()
    if request.method == "POST":
        name    = request.POST['name']
        email   = request.POST['email']
        sub     = request.POST['subject']
        mesg    = request.POST['message']
        data    = models.Contact.objects.create(
                        name        = name,
                        email       = email,
                        subject     = sub,
                        message     = mesg
            )
        data.save()
        views_dict = base().update({'message' : "Your message is send."})
        return render(request, 'contact.html', views_dict)
    return render(request, 'contact.html', base())

def portfolio(request):
    return render(request, 'portfolio.html')

def price(request):
    return render(request, 'price.html')

def services(request):
    return render(request, 'services.html', base())