from django.db import models

# Create your models here.
class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Wycieczki(models.Model): #Wycieczki
    def __str__(self):
        return self.nazwa

    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=40)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12,decimal_places=2)
    #data
    #dlugosc

    class Meta:
        verbose_name = "Wycieczka"
        verbose_name_plural = "Wycieczki"