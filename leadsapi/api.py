from rest_framework import serializers, viewsets, permissions

from leadsapi.models import Lead
from .serializers import LeadSerializer

class LeadViewset(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user.leads.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)