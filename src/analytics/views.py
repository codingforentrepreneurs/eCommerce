import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum, Avg
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View
from django.shortcuts import render

from django.utils import  timezone


from orders.models import Order

class SalesAjaxView(View):
    def get(self, request, *args, **kwargs):
        data = {}
        print(request.user)
        if request.user.is_staff:
            if request.GET.get('type') == 'week':
                data['labels'] = ["Mon", "Tues", "Weds", "Thurs", "Fri","Sat", "Sun"]
                data['data'] = [123, 131, 232, 12, 323,313, 3193]
            if request.GET.get('type') == '4weeks':
                data['labels'] = ["Last Week", "Two Weeks Ago", "Three Weeks Ago", "Four Weeks Ago"]
                data['data'] = [123, 131, 343, 13231]
        return JsonResponse(data)



class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, "400.html", {})
        return super(SalesView, self).dispatch(*args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super(SalesView, self).get_context_data(*args, **kwargs)
        #two_weeks_ago = timezone.now() - datetime.timedelta(days=14)
        #one_week_ago = timezone.now() - datetime.timedelta(days=7)
        qs = Order.objects.all().by_weeks_range(weeks_ago=10, number_of_weeks=10)
        context['today'] = qs.by_range(start_date=timezone.now().date()).get_sales_breakdown()
        context['this_week'] = qs.by_weeks_range(weeks_ago=1, number_of_weeks=1).get_sales_breakdown()
        context['last_four_weeks'] = qs.by_weeks_range(weeks_ago=5, number_of_weeks=4).get_sales_breakdown()
        return context