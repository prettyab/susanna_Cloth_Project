from django.contrib import admin
from .models import Categories, Filter_Price, Product, Images, Tag,Contact,Order,OrderItem

class ImageTublerinline(admin.TabularInline):  # Fix 1: Use TabularInline
    model = Images

class TagTublerinline(admin.TabularInline):   # Fix 1: Use TabularInline
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageTublerinline, TagTublerinline]  # Fix 3: Correct class names


class OrderItemTublerinline(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTublerinline]

admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Categories)
admin.site.register(Filter_Price)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)


