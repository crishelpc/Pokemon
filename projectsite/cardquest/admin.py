from django.contrib import admin
from .models import Trainer

@admin.register(Trainer)
class TrainerAdmini(admin.ModelAdmin): 
    list_display =("name", "birthdate", "location", "email")
    search_fields = ("name", "location", )
# Register your models here.



## add to model pokemon cards, location 
##upd the admin.py 
