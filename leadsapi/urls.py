from rest_framework import routers

from .api import LeadViewset

router = routers.DefaultRouter()
router.register('leads', LeadViewset, 'leads')

urlpatterns = router.urls