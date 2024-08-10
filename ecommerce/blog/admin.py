from django.contrib import admin
from.models import *

# Register your models here.

admin.site.register(registration)
admin.site.register(category)
admin.site.register(product)
admin.site.register(Cart)
admin.site.register(Cartitem)
admin.site.register(Order)