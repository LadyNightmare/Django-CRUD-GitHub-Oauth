from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.template import loader
from django.contrib.auth import logout as auth_logout
from .forms import PersonalInfoForm
from .models import PersonalInfo


def logout(request):
    auth_logout(request)
    return redirect('/')

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

def delete_info(request):
    request.user.personalinfo.delete()
    return redirect('/')


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
