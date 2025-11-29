from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db import transaction
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

from store.models import Collection, Product, OrderItem, Order, Customer
from tags.models import TaggedItem
from decimal import Decimal


@transaction.atomic()
def say_hello(request):

    # order = Order()
    # order.customer = Customer(pk=1)
    # order.payment_status = Order.PAYMENT_PENDING
    # order.save()

    # item = OrderItem()
    # item.order = Order.objects.get(pk=2)
    # item.product = Product.objects.get(pk=1)
    # item.quantity = 10
    # item.unit_price = Decimal(10)
    # item.save()

    return render(request, "hello.html", {"name": "Abdelrahman"})


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

# discount_price = ExpressionWrapper(F("price") * 0.8, output_field=DecimalField())
# results = Product.objects.annotate(discount_price=discount_price)

# collection = Collection(pk=1)
# collection.title = "Games"
# collection.featured_product = None
# collection.save()

# collection = Collection(pk=1)
# collection.delete()

# Collection.objects.filter(id=1).delete()
"""
