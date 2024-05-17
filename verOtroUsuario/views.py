from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def view_other_profile(request, username):
    other_user = get_object_or_404(User, username=username)
    return render(request, 'other_profile.html', {'other_user': other_user})
