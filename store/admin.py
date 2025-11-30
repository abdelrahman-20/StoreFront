# Registering Models
# ------------------
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import aggregates
from django.http import HttpRequest
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]
    search_fields = ["title"]

    @admin.display(ordering="products_count")
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return (
            super()
            .get_queryset(request)
            .annotate(products_count=aggregates.Count("product"))
        )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "inventory_status", "collection_title"]
    list_editable = ["price"]
    list_per_page = 50
    list_select_related = ["collection"]

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"

    def collection_title(self, product):
        return product.collection.title


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page = 50


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "placed_at"]
    list_per_page = 50
