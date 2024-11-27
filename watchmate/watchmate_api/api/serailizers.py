from rest_framework import serializers
from watchmate_api.models import Movie

# Validator
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is Too Short!")

# Serailizers

class MovieSerialzier(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField(default=False)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    # Field Level validation on Name Field
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is Too Short")
    #     else:
    #         return value
    
    # Object Level Validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different")
        else:
            return data