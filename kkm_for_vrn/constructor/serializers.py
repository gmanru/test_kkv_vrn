from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = 'id', 'passenger_name', 'flight', 'ticket_number', 'ticket_place', 'ticket_type'
        view_name = 'tickets'



