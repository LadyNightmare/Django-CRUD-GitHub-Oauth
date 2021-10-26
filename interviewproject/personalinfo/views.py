from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from .forms import PersonalInfoForm
from .models import PersonalInfo

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/')

@login_required
def create_info(request):
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.user = request.user
            personal_info.save()
            return redirect('/')
        else:
            context = {
                "form": form,
                "action": 'Create'
            }
            return render(request, "personalinfo/personal_info_form.html", context)
    else:
        form = PersonalInfoForm()
        context = {
            "form": form,
            "action": 'Create'
        }
        return render(request, "personalinfo/personal_info_form.html", context)

@login_required
def delete_info(request):
    request.user.personalinfo.delete()
    return redirect('/')

@login_required
def update_info(request):
    instance = PersonalInfo.objects.get(pk=request.user.personalinfo.id)
    if request.method == 'POST':
        form = PersonalInfoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {
                "form": form,
                "action": 'Update'
            }
            return render(request, "personalinfo/personal_info_form.html", context)
    else:
        form = PersonalInfoForm(instance=instance)
        context = {
            "form": form,
            "action": 'Update'
        }
        return render(request, "personalinfo/personal_info_form.html", context)
