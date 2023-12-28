from django.contrib import admin
from .models import (
    Product,
    ProductCategory,
    Inventory,
    InventoryAttributeValue,
    Attribute,
    AttributeValue,
    Category,
    Image,
    StockControl
)

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image


class StockControlInline(admin.TabularInline):
    model = StockControl


@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    inlines = [ImageInline, StockControlInline]


class AttribueValueInline(admin.TabularInline):
    model = AttributeValue


@admin.register(Attribute)
class Attribute(admin.ModelAdmin):
    inlines = [AttribueValueInline]


@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Product)
class Product(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ("name",),
    }
