from rest_framework import serializers
from watchmate_api.models import WatchList, StreamPlatform


# Model Serializer
class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id','name','description']  
        # exclude = ['active']

class StreamPlatformSerailizer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'

""" This model serailizer uses `Serializer` but now we'll use `ModelSerializer` which makes things much simpler"""
# # Validator
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is Too Short!")

# # Serailizers

# # class MovieSerialzier(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField(default=False)
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # Field Level validation on Name Field
#      def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is Too Short")
#         else:
#             return value
    
#     # Object Level Validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different")
#         else:
#             return data