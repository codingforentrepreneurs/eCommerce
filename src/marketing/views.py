from django.conf import settings

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views.generic import UpdateView, View
from django.shortcuts import render, redirect


from .forms import MarketingPreferenceForm
from .mixins import CsrfExemptMixin
from .models import MarketingPreference
from .utils import Mailchimp
MAILCHIMP_EMAIL_LIST_ID = getattr(settings, "MAILCHIMP_EMAIL_LIST_ID", None)

class MarketingPreferenceUpdateView(SuccessMessageMixin, UpdateView):
    form_class = MarketingPreferenceForm
    template_name = 'base/forms.html' # yeah create this
    success_url = '/settings/email/'
    success_message = 'Your email preferences have been updated. Thank you.'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated():
            return redirect("/login/?next=/settings/email/") # HttpResponse("Not allowed", status=400)
        return super(MarketingPreferenceUpdateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(MarketingPreferenceUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Email Preferences'
        return context

    def get_object(self):
        user = self.request.user
        obj, created = MarketingPreference.objects.get_or_create(user=user) # get_absolute_url
        return obj






"""
POST METHOD
data[list_id]: e2ef12efee
fired_at: 2017-10-18 18:49:49
data[merges][FNAME]:
data[email]: hello@teamcfe.com
data[merges][LNAME]:
data[email_type]: html
data[reason]: manual
data[merges][BIRTHDAY]:
data[id]: d686033a32
data[merges][EMAIL]: hello@teamcfe.com
data[ip_opt]: 108.184.68.3
data[web_id]: 349661
type: unsubscribe
data[action]: unsub
"""

class MailchimpWebhookView(CsrfExemptMixin, View): # HTTP GET -- def get() CSRF?????
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("Thank you", status=200)
    def post(self, request, *args, **kwargs):
        data = request.POST
        list_id = data.get('data[list_id]')
        if str(list_id) == str(MAILCHIMP_EMAIL_LIST_ID):
            hook_type = data.get("type")
            email = data.get('data[email]')
            response_status, response = Mailchimp().check_subcription_status(email)
            sub_status  = response['status']
            is_subbed = None
            mailchimp_subbed = None
            if sub_status == "subscribed":
                is_subbed, mailchimp_subbed  = (True, True)
            elif sub_status == "unsubscribed":
                is_subbed, mailchimp_subbed  = (False, False)
            if is_subbed is not None and mailchimp_subbed is not None:
                qs = MarketingPreference.objects.filter(user__email__iexact=email)
                if qs.exists():
                    qs.update(
                            subscribed=is_subbed, 
                            mailchimp_subscribed=mailchimp_subbed, 
                            mailchimp_msg=str(data))
        return HttpResponse("Thank you", status=200)

# def mailchimp_webhook_view(request):
#     data = request.POST
#     list_id = data.get('data[list_id]')
#     if str(list_id) == str(MAILCHIMP_EMAIL_LIST_ID):
#         hook_type = data.get("type")
#         email = data.get('data[email]')
#         response_status, response = Mailchimp().check_subcription_status(email)
#         sub_status  = response['status']
#         is_subbed = None
#         mailchimp_subbed = None
#         if sub_status == "subscribed":
#             is_subbed, mailchimp_subbed  = (True, True)
#         elif sub_status == "unsubscribed":
#             is_subbed, mailchimp_subbed  = (False, False)
#         if is_subbed is not None and mailchimp_subbed is not None:
#             qs = MarketingPreference.objects.filter(user__email__iexact=email)
#             if qs.exists():
#                 qs.update(
#                         subscribed=is_subbed, 
#                         mailchimp_subscribed=mailchimp_subbed, 
#                         mailchimp_msg=str(data))
#     return HttpResponse("Thank you", status=200)



