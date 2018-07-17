from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'jobs', JobViewSet, base_name='jobs')
router.register(r'accounts', AccountViewSet, base_name='accounts')
router.register(r'useraccountassociations', UserAccountAssociationViewSet, base_name='associations')
urlpatterns = router.urls
