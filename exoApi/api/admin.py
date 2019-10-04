from django.contrib import admin

# Register your models here.


from .models import Categories, SousCategories, Articles, Commentaires

admin.site.register(Categories)
admin.site.register(SousCategories)
admin.site.register(Articles)
admin.site.register(Commentaires)