from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

import account.views

from custom_account.forms import CustomSignupForm


class SignupView(account.views.SignupView):
    
    messages = {
        "email_confirmation_sent": {
            "level": messages.INFO,
            "text": _("Go check your e-mail (%(email)s) to verify your e-mail address.")
        },
        "logged_in": {
            "level": messages.SUCCESS,
            "text": _("Successfully logged in as %(user)s.")
        },
        "invalid_signup_code": {
            "level": messages.WARNING,
            "text": _("The code %(code)s is invalid.")
        }
    }
    
    form_class = CustomSignupForm
   
    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)
    
    def create_profile(self, form):
        profile = self.created_user.get_profile()
        profile.terms_and_conditions = form.cleaned_data["terms_and_conditions"]
        profile.save()
