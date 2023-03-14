import json
import traceback

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
import dent.services as service
from datetime import datetime

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                stuff = service.get_stuff(user)
                request.session['role'] = stuff.role.code
                request.session['clinic'] = stuff.clinic.name
                return HttpResponseRedirect("/home")
            else:
                return HttpResponse("Your account is disabled")
        else:
            return render(request, 'login.html', {"error": "Incorrect username or password"})
    else:
        return render(request, 'login.html', {})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def calendar(request):
    return render(request, 'dent/calendar.html')


@login_required
def calendar_list(request):
    return render(request, 'dent/calendar_list.html')


@login_required
def add_event(request):
    response = {}
    if request.is_ajax and request.method == 'POST':
        response = service.add_event(request.POST, request.user)
    else:
        response['success'] = False
        response['error_msg'] = 'Only POST allowed !'
    return JsonResponse(response, status=200)


@login_required
def delete_event(request):
    response = {}
    if request.is_ajax and request.method == 'POST':
        response = service.delete_event(request.POST['event_id'])
        return JsonResponse(response, status=200)
    else:
        return JsonResponse(response, status=400)


@login_required
def patient_list(request):
    return render(request, 'dent/patient_list.html')


@login_required
def patient_add(request):
    response = {}
    if request.method == 'GET':
        return render(request, 'dent/add_patient.html')
    elif request.method == 'POST' and request.is_ajax:
        response = service.add_patient(request.POST, request.user)
        return JsonResponse(response, status=200, safe=False)
    else:
        return JsonResponse(response, status=405)


@login_required
def patient_edit(request):
    response = {}
    if request.method == 'GET':
        context = {"patient": service.get_patient(request.GET['patient_ref_id'])}
        return render(request, 'dent/edit_patient.html', context=context)
    elif request.method == 'POST':
        response = service.edit_patient(request.POST, request.user)
        return JsonResponse(response, status=200, safe=False)


@login_required
def get_patient_list_json(request):
    response = {}
    try:
        response['success'] = True
        response['data'] = service.get_clinic_patients_json(request.user)
    except Exception as e:
        response['success'] = False
        response['error_msg'] = str(traceback.format_exc())
    return JsonResponse(response, status=200, safe=False)


@login_required
def treatment(request):
    if request.method == 'GET':
        context = service.treatment_get_context(request.user, request.GET['patient_ref_id'])
        return render(request, 'dent/treatement.html', context=context)


@login_required
def save_treatment(request):
    if request.is_ajax and request.method == 'POST':
        data = json.loads(request.body)
        response = service.save_treatment(request.user, data)
        return JsonResponse(response, status=200, safe=False)


@login_required
def get_treatment(request):
    if request.method == 'GET':
        context = service.get_treatment(request.GET['treatment_ref_id'])
        return render(request, 'dent/treatment_info.html', context=context)


@login_required
def treatment_print(request):
    if request.method == 'GET':
        context = service.get_treatment(request.GET['treatment_ref_id'])
        return render(request, 'dent/treatment_print.html', context=context)


@login_required
def patient_treatment_history(request):
    if request.method == 'GET':
        context = service.get_patient_treatment_history(request.GET['patient_ref_id'])
        return render(request, 'dent/treatment_history.html', context=context)


@login_required
def event_edit(request):
    if request.is_ajax and request.method == 'POST':
        data = json.loads(request.body)
        response = service.edit_event(data)
        return JsonResponse(response, status=200, safe=False)
