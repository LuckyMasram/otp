from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(TempUser)
admin.site.register(Tradesman)
admin.site.register(TradeType)
admin.site.register(BookTradesman)
admin.site.register(ImageUpload)
