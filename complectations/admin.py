from django.contrib import admin
from .models import Product, ProductSmeta, Complectation, Provider, GroupProduct, Receipts, ServiceSmeta

admin.site.register(Complectation)
admin.site.register(Product)
admin.site.register(GroupProduct)
admin.site.register(ProductSmeta)
admin.site.register(Provider)
admin.site.register(Receipts)
admin.site.register(ServiceSmeta)



