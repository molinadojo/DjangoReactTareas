from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from tasks import views

#esto es para crear las rutas que frontend necesita para consultar

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    
]

#todo esto esta generando las rutas de GET POST PUT DELETE