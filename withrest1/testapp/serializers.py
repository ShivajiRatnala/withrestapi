from rest_framework import serializers
from testapp.models import Student
class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    rollno = serializers.IntegerField()
    address = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.rollno = validated_data.get('rollno', instance.rollno)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
