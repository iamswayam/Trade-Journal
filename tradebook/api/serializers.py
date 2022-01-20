from rest_framework import serializers
from ..models import Note, NseIndexData, NseStockData

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['date','time', 'index', 'strike_price', 'position', 
                  'call_type', 'lot', 'avg_price', 'sqo_price', 'sqo_price2', 
                  'swing_high', 'swing_low', 'profit_loss', 'upload']
        
        
class NseIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = NseIndexData
        fields = ['ticker']
        
class NseStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = NseStockData
        fields = ['ticker']