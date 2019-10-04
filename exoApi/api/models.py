from django.db import models

# Create your models here.
class Categories(models.Model):
    nom = models.CharField(_(""), max_length=50)
    description = models.TextField(_(""))
    image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    statut = models.BooleanField(_(""))
    date

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)