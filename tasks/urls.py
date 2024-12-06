from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from tasks import views

#esto es para crear las rutas que frontend necesita para consultar

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")

schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="Description of your API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[],
)

urlpatterns = [
    path("api/v1/", include(router.urls)) ,
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

#todo esto esta generando las rutas de GET POST PUT DELETE
#este para que haga la documentacion.