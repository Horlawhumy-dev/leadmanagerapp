from django.db import models
from django.db.models import fields
from rest_framework import serializers
from lead.models import Lead

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = '__all__'