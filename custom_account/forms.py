from django import forms
from django.core.urlresolvers import reverse_lazy

import account.forms

class CustomSignupForm(account.forms.SignupForm):
    
    # the url for the terms is hardcoded, 'cause reverse-lazy does not do the job
    # and there is no clear way to resolve this.
    terms_url = "/about/terms/"
    label_terms_and_condition = 'I accept the <a href="%s">Terms and Conditions</a>' %terms_url
    terms_and_conditions = forms.BooleanField(initial=False, 
                                              required=True,
                                              label=label_terms_and_condition,
                                              error_messages={'required': 'To register you need to accept our term and condition'}
                                              )