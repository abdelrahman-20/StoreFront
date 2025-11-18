# from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import (
    Q,
    F,
    aggregates,
    Value,
    Func,
    functions,
    ExpressionWrapper,
    DecimalField,
)
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    """
    # results = Product.objects.filter(inventory__lt=10, price__lt=20)
    # results = Product.objects.filter(Q(inventory__lt=10) & ~Q(price__lt=20))
    # results = Product.objects.filter(inventory=F("price"))
    # results = Product.objects.order_by("title")

    # results = OrderItem.objects.values_list("id", "product__title").order_by(
    #     "product__title"
    # )

    # results = Product.objects.filter(
    #     id__in=OrderItem.objects.values("product__id")
    #     .distinct()
    #     .order_by("product__id")
    # )

    # Select_related -> 1 Instance -> Product Has One Collection
    # Prefetch_related -> Many Instances -> Product Has Many Promotions
    # results = (
    #     Order.objects.select_related("customer")
    #     .prefetch_related("orderitem_set__product")
    #     .order_by("-placed_at")[:5]
    # )

    # results = Product.objects.aggregate(count=aggregates.Count("id"), min_price=aggregates.Min("price"))

    # results = Customer.objects.annotate(is_new=Value(True))

    # results = Customer.objects.annotate(
    #     # CONCAT
    #     # full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    #     full_name=functions.Concat("first_name", Value(" "), "last_name")
    # )

    # results = Customer.objects.annotate(orders_count=aggregates.Count("order"))

    """
    discount_price = ExpressionWrapper(F("price") * 0.8, output_field=DecimalField())
    results = Product.objects.annotate(discount_price=discount_price)
    return render(request, "hello.html", {"name": "Abdelrahman", "results": (results)})
