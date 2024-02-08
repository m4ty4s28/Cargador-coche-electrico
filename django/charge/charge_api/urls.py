
#from django.conf.urls import url
from django.urls import path, include
from .views import (
    ChargePointListApiView,
    ChargePointDetailApiView,
    dashboard_status
)

urlpatterns = [
    path('chargepoint/', ChargePointListApiView.as_view()),
    path('chargepoint/<int:chargepoint_id>/', ChargePointDetailApiView.as_view()),
    path('status/', dashboard_status, name="dashboard_status"),
]