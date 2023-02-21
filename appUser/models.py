from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    name = models.CharField(("Ad"), max_length=50)
    image = models.FileField(("Fotoğraf"), upload_to="", max_length=100)

    class Meta:
        verbose_name_plural ="Profiller"
    
    def __str__(self):
        return self.name
