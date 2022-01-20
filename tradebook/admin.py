from django.contrib import admin
from .models import Note, NseIndexData, NseStockData

admin.site.register(Note)
admin.site.register(NseIndexData)
admin.site.register(NseStockData)

