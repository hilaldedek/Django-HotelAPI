from .views import RezervationViews,ReservationDetailViews
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hotels',RezervationViews)

router.register('detail',ReservationDetailViews)
urlpatterns = router.urls


