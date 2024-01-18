from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','is_active']
    list_editable = ['price','is_active']
    # readonly_fields = ['description','slug']
    prepopulated_fields = {'slug':['title']}
    list_filter = ['price','is_active']

class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['color','size']
    list_editable = ['size']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','url_title']
    list_editable = ['url_title']

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag']
admin.site.register(models.products,ProductAdmin)
admin.site.register(models.ProductCategory,ProductCategoryAdmin)
admin.site.register(models.ProductInformation,ProductInfoAdmin)
admin.site.register(models.ProductTag,ProductTagAdmin)