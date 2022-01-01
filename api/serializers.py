from rest_framework import serializers
from .models import Student, State, Parent

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class ListParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"

class ListStudentSerializer(serializers.ModelSerializer):
    # school = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # parent = ParentSerializer(many=True)
    # standard = serializers.StringRelatedField()
    # location = serializers.StringRelatedField()

    class Meta:
        model = Student
        # fields = ['id', 'name', 'school', 'parent', 'standard', 'location']
        fields = "__all__"