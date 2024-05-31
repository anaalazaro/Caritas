# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django import forms
# from .models import CustomUser
# # Register your models here.

# class CustomUserCreationForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.roles = 'admin' 
#         if commit:
#             user.save()
#         return user
    
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserCreationForm
#     model = CustomUser
#     list_display = ['username', 'email']

# admin.site.register(CustomUser, CustomUserAdmin)