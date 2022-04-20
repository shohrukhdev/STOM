from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from dent import views as mainviews
from django.contrib.auth import views as authview
from dent import api_views, table_views

router = routers.DefaultRouter()
router.register('event', viewset=api_views.EventViewSet)
router.register('patient', viewset=table_views.PatientViewSet)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', mainviews.user_login, name='login'),
    path('logout/', authview.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', mainviews.home),
    path('home/', mainviews.home),
    path('calendar/', mainviews.calendar, name='calendar'),
    path('calendar/event/add/', mainviews.add_event, name='add_event'),
    path('calendar/event/delete', mainviews.delete_event, name='delete_event'),
    path('patient/list/', mainviews.patient_list, name='patient_list'),
    path('patient/add/', mainviews.patient_add, name='patient_add'),
    path('patient/edit', mainviews.patient_edit, name='patient_edit'),
    path('patient/list_json', mainviews.get_patient_list_json, name='patient_list_json'),
    path('treatement/add', mainviews.treatment, name='treatement')
]
