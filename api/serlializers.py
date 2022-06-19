from django.db.models import fields
from rest_framework import serializers
from .models import Item ,History

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('key','value','time')


class HistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = History
		fields = ('key', 'value','time')

