from .models import *
from datetime import datetime
import traceback
from .serializers import *
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder


def get_stuff(user):
    return Stuff.objects.get(user=user)


def add_event(form, cur_user):
    response = {}
    try:
        stuff = Stuff.objects.get(user=cur_user)
        start_time_obj = datetime.strptime(form['start_time'], '%d.%m.%Y %H:%M')
        end_time_obj = datetime.strptime(form['end_time'], '%d.%m.%Y %H:%M')
        patient = Patient.objects.get(id=form['patient_id'])
        Event.objects.create(stuff=stuff,
                             patient=patient,
                             title=form['title'],
                             start_time=start_time_obj,
                             end_time=end_time_obj,
                             background_color=form['background'],
                             border_color=form['background'])
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = str(traceback.format_exc())
    return response


def delete_event(id):
    response = {}
    try:
        event = Event.objects.get(id=id)
        event.delete()
        response['success'] = True
    except Exception as e:
        response['error_msg'] = str(traceback.format_exc())
        response['success'] = False
    return response


def add_patient(form, cur_user):
    response = {}
    try:
        stuff = Stuff.objects.get(user=cur_user)
        date_birth = datetime.strptime(form['date_birth'], '%d.%m.%Y')
        Patient.objects.create(clinic=stuff.clinic,
                               full_name=form['full_name'],
                               mobile_phone=form['mobile_phone'],
                               sex=form['sex'],
                               date_birth=date_birth,
                               comments=form['comments'],
                               state='A',
                               cr_by=stuff,
                               up_by=stuff)
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = str(traceback.format_exc())

    return response


def get_patient(patient_id):
    return Patient.objects.get(id=patient_id)


def edit_patient(form, cur_user):
    response = {}
    try:
        Patient.objects.filter(id=form['id']).update(
            full_name=form['full_name'],
            mobile_phone=form['mobile_phone'],
            sex=form['sex'],
            date_birth=datetime.strptime(form['date_birth'], '%d.%m.%Y'),
            comments=form['comments'],
            state=form['state'],
            up_by=get_stuff(cur_user)
        )
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = str(traceback.format_exc())
    return response


def delete_patient(patient_id, cur_user):
    response = {}
    try:
        Patient.objects.filter(id=patient_id).update(
            state='D',
            up_by=get_stuff(cur_user)
        )
        response['success'] = True
    except Exception as e:
        response['success'] = False
        response['error_msg'] = str(traceback.format_exc())
    return response


def get_clinic_patients_json(cur_user):
    patient_list = []
    stuff = get_stuff(cur_user)
    patients = Patient.objects.filter(clinic=stuff.clinic, state='A')
    for p in patients:
        pat = {"id": p.id, "name": p.full_name, "phone": p.mobile_phone}
        patient_list.append(pat)
    return patient_list


def treatment_get_context(cur_user, patient_id):
    stuff = Stuff.objects.get(user=cur_user)
    patient = Patient.objects.get(id=patient_id)
    services = Service.objects.filter(doctor=stuff, status=1).values()
    categories = ServiceCategory.objects.filter(stuff=stuff)
    tooth_states = ToothState.objects.all().values()
    teeth = Teeth.objects.all()
    json_ser = json.dumps(list(services), cls=DjangoJSONEncoder)
    json_states = json.dumps(list(tooth_states), cls=DjangoJSONEncoder)
    context = {'doctor': stuff,
               'patient': patient,
               'categories': categories,
               'tooth_states': json_states,
               'services': json_ser,
               'teeth': teeth}
    return context


def save_treatment(cur_user, data):
    global procedure
    response = {}
    try:
        doctor = Stuff.objects.get(user=cur_user)
        patient = Patient.objects.get(id=data['patient_id'])
        treatment = Treatment.objects.create(doctor=doctor,
                                             patient=patient,
                                             complaint=data['complaint'],
                                             diagnosis=data['diagnosis'],
                                             cr_on=datetime.now(),
                                             description=data['recommendations'],
                                             total_amount=data['total'],
                                             discount=data['discount'],
                                             paid_amount=data['amount_paid'],
                                             cr_by=cur_user)
        for i in data.keys():
            if i.isnumeric():  # IF TOOTH NUMBER
                for s in data[i]:   # SERVICES FOR THAT TOOTH
                    tooth = Teeth.objects.get(id=i)
                    service = Service.objects.get(id=s['id'])
                    procedure = Procedure.objects.create(treatment=treatment,
                                                         teeth=tooth,
                                                         service=service,
                                                         quantity=s['quantity'],
                                                         price=s['price'])

                for ts in data['teeth_states'][i]:  # STATES OF THAT TOOTH
                    tooth_state = ToothState.objects.get(id=ts)
                    tooth = Teeth.objects.get(id=i)
                    ProcedureToothState.objects.create(treatment=treatment,
                                                       teeth=tooth,
                                                       tooth_state=tooth_state)
        response['success'] = True
        response['treatment_id'] = treatment.id
    except Exception as e:
        print(traceback.format_exc())
        response['success'] = False
        response['error_msg'] = traceback.format_exc()
    return response


def get_treatment(treatment_id):
    treatment = Treatment.objects.get(id=treatment_id)
    teeth_set = Treatment.objects.get(id=treatment_id).procedure_set
    context = {"treatment": treatment,
               "teeth_set": teeth_set}
    return context


