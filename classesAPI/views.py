from django.shortcuts import render
from classes.models import Classroom
from .serializers import (ClassroomSerializer, DetailSerializer,CreateSerializer, RegisterSerializer)
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView,RetrieveUpdateAPIView, DestroyAPIView)

class APIListView (ListAPIView) :
	queryset = Classroom.objects.all()
	serializer_class = ClassroomSerializer

class APIDetailsView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class APICreateView (CreateAPIView) :
	serializer_class = CreateSerializer
	def perform_create (self, serializer) :
		serializer.save(teacher=self.request.user)

class APIUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = CreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class APIDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
