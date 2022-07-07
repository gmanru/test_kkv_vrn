from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.list import ListView

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet

from ..forms import TicketForm
from ..models import Ticket
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
    template_name = 'create_sample.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tickets = Ticket.objects.all()
        context.update({"tickets": tickets})

        return context

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

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


