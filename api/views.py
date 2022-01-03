from django.shortcuts import render
from django.http import HttpResponse

# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# models and serializers
from .serializers import ListStudentSerializer, ListParentSerializer
from .models import Student, School, Parent

# Create your views here.
def sample(request):
    return HttpResponse("Hello")

# Index
@api_view(['GET'])
def index(request):
    apiList = {
        "student": {
            "list",
            "add",
            "update",
            "delete"
        }
    }
    return Response(apiList)

# 1: lists
@api_view(['GET'])
def StudentList(request):
    list = Student.objects.all()
    # print("student ", Student.objects.get(id=id))
    serializer = ListStudentSerializer(list, many=True)
    return Response(status=200, data=serializer.data)

@api_view(['GET'])
def ParentList(request):
    list = Parent.objects.all()
    serializer = ListParentSerializer(list, many=True)
    return Response(serializer.data)