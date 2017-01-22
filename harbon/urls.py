from django.conf.urls import url
from . import views

app_name = 'harbon'

urlpatterns = [
    #/harbon
    url(r'^$', views.indexView.as_view(), name='index'),
    #/harbon/employee
    url(r'^employeeView/$', views.EmployeeView.as_view(), name='employee-view'),
    #/harbon/addEmployee/
    url(r'^addEmployee/$',views.employeeCreate.as_view(), name="employee-add"),
    #/harbon/holidayRequest/
    url(r'^holidayRequest/$',views.holidayRequestCreate.as_view(),name="holiday-request"),
    #/harbon/holidayRequest/approve/(primary key)
    url(r'^holidayRequest/approve/(?P<pk>[0-9]+)$',views.holidayRequestApprove.as_view(),name="holiday-approve"),

    url(r'^holidayRequest/reject/(?P<pk>[0-9]+)$',views.holidayRequestReject.as_view(), name="holiday-reject"),

    url(r'^holidayRequest/delete/(?P<pk>[0-9]+)$',views.holidayRequestDelete.as_view(), name="holiday-delete"),
]
