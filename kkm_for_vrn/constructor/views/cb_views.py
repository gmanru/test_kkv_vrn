from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet

from ..forms import TicketForm
from ..models import Ticket, Flight, Autostation, Carrier, Route 
from ..serializers import TicketSerializer


class TicketListView(APIView):
    def get(self, request):
        items = Ticket.objects.all()
        serializer = TicketSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketFieldsView(TemplateView):
    '''def get(self, request):
        items = Ticket.objects.all()
        serializer = TicketSerializer(items, many=True)
        return Response(serializer.data)'''
    template_name = 'create_sample.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tickets = Ticket.objects.all()
        context.update({"tickets": tickets})

        return context

    

'''class TicketCreateView(CreateView):

    model =  Ticket

    fields = '__all__'
    success_url = '/constructor/'

    def get_success_url(self):
        return '/ticket/{}/'.format(self.object.pk)'''


class TicketCreateView(View):

    def get(self, request):
        #queryset = Ticket.objects.all()
        form = TicketForm()
        return render(request, 'create_sample.html', context={"form": form})

    def post(self, request):
        #queryset = Ticket.objects.all()
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_sample.html', context={"form": form})

'''class TicketItemDetailView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializer(todo)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializer(todo)
        data = serializer.data
        todo.delete()
        return Response(data)'''


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


'''class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer'''
