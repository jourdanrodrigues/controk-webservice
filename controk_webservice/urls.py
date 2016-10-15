from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from controk_webservice.clients.views import ClientsViewSet
from controk_webservice.employees.views import EmployeesViewSet

router = DefaultRouter()
router.register(r'clients', ClientsViewSet)
router.register(r'employees', EmployeesViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls))
]
