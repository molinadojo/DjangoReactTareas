
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
#esto crea todo el crud que vamos a necesitar
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @swagger_auto_schema(operation_summary="Retrieve a list of tasks")
    def list(self, request):
        return super().list(request)