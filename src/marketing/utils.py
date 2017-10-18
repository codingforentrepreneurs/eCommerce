import json
import requests
from django.conf import settings



MAILCHIMP_API_KEY = getattr(settings, "MAILCHIMP_API_KEY", None)
MAILCHIMP_DATA_CENTER = getattr(settings, "MAILCHIMP_DATA_CENTER", None)
MAILCHIMP_EMAIL_LIST_ID = getattr(settings, "MAILCHIMP_EMAIL_LIST_ID", None)



class Mailchimp(object):
    def __init__(self):
        super(Mailchimp, self).__init__()
        self.key = MAILCHIMP_API_KEY
        self.api_url = "https://{dc}.api.mailchimp.com/3.0".format(
                    dc=MAILCHIMP_DATA_CENTER
                    )
        self.list_id = MAILCHIMP_EMAIL_LIST_ID
        self.list_endpoint = '{api_url}/lists/{list_id}'.format(
                                    api_url = self.api_url,
                                    list_id=self.list_id
                        )

    def check_subcription_status(self, email):
        # endpoint 
        # method
        # data
        # auth
        endpoint = self.api_url
        r = requests.get(endpoint, auth=("", self.key))
        return r.json()

    def check_valid_status(self, status):
        choices = ['subscribed', 'unsubscribed', 'cleaned', 'pending']
        if status not in choices:
            raise ValueError("Not a valid choice for email status")
        return status

    def add_email(self, email):
        # endpoint 
        # method
        # data
        # auth\
        status = "subscribed"
        self.check_valid_status(status)
        data = {
            "email_address": email,
            "status": status
        }
        endpoint = self.list_endpoint + "/members"
        r = requests.post(endpoint, auth=("", self.key), data=json.dumps(data))
        return r.json()

