from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from controk_webservice.assets.views import AssetsViewSet
from controk_webservice.clients.views import ClientsViewSet
from controk_webservice.employees.views import EmployeesViewSet
from controk_webservice.stock.views import ProductsViewSet, ShipmentsViewSet
from controk_webservice.suppliers.views import SuppliersViewSet

router = DefaultRouter()
# Custom
router.register(r'assets', AssetsViewSet, base_name='assets')
# Model B
router.register(r'clients', ClientsViewSet)
router.register(r'employees', EmployeesViewSet)
router.register(r'suppliers', SuppliersViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'shipments', ShipmentsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'docs/', get_swagger_view(title='Controk WebService')),
    url(r'^api/v1/', include(router.urls))
]
