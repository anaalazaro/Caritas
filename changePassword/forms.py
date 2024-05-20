from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class DesiredPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
