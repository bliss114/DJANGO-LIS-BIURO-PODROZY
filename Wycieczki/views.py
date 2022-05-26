from django.shortcuts import render
from django.http import HttpResponse
from .models import Wycieczki, Kategoria

def index(request):
    #wszystkie = Wycieczki.objects.all()
    #jeden = Wycieczki.objects.get(pk=3)
    #kategoria = Wycieczki.objects.filter(kategoria=4)
    #kateg_nazwa = Kategoria.objects.get(id=2)
    kategorie = Kategoria.objects.all()
    #null = Wycieczki.objects.filter(kategoria__isnull=False)
    #zawiera = Wycieczki.objects.filter(opis__icontains='przygoda')
    #return HttpResponse(kategorie)
    dane = {'kategorie' : kategorie}
    return render(request, 'szablon.html', dane)

    #return HttpResponse(Wycieczki.objects.all())

def kategoria (request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def wycieczka (request, id):
    wycieczka_user = Wycieczki.objects.get(pk=id)
    napis = "<h1>" + str(wycieczka_user) + "</h1>" + \
            "<p>" + str(wycieczka_user.opis) + "</p>" + \
            "<p>" + str(wycieczka_user.cena) + "</p>"
    return HttpResponse(napis)
