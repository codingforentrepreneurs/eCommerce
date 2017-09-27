from django.db import models
from django.db.models.signals import pre_save


from carts.models import Cart
from ecommerce.utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

# Random, Unique
class Order(models.Model):
    order_id        = models.CharField(max_length=120, blank=True) # AB31DE3
    # billing_profile = ?
    # shipping_address
    # billing_address 
    cart            = models.ForeignKey(Cart)
    status          = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total  = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total           = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id, sender=Order)



# generate the order id?
# generate the order total?