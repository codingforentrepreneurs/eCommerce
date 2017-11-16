from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum, Avg
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render



from orders.models import Order

class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, "400.html", {})
        return super(SalesView, self).dispatch(*args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super(SalesView, self).get_context_data(*args, **kwargs)
        qs = Order.objects.all()
        context['orders'] = qs
        context['recent_orders'] = qs.recent().not_refunded()[:5]
        context['recent_orders_total'] = context['recent_orders'].aggregate(
                                        Sum("total"), 
                                        Avg("total"), 
                                        # Avg("cart__products__price"), 
                                        # Count("cart__products")
                                    )
        # context['recent_cart_data'] = context['recent_orders'].aggregate(
        #                                 Avg("cart__products__price"), 
        #                                 Count("cart__products")
        #                             )
        # qs = Order.objects.all().aggregate(Sum("total"), Avg("total"), Avg("cart__products__price"), Count("cart__products"))
        # ann = qs.annotate(product_avg=Avg('cart__products__price'), product_total = Sum('cart__products__price'), product__count = Count('cart__products'))
        context['shipped_orders'] = qs.recent().not_refunded().by_status(status='shipped')[:5]
        context['paid_orders'] = qs.recent().not_refunded().by_status(status='paid')[:5]
        return context