from .views import CustomerViews
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',CustomerViews)

urlpatterns = router.urls
