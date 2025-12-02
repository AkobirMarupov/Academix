from rest_framework import serializers
from applications.models import Application, StudentForm, ApplicationStatusNotification

class StudentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentForm
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    form = StudentFormSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'student', 'center', 'course', 'teacher', 'status', 'submitted_at', 'updated_at', 'comment', 'form']


class ApplicationStatusNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatusNotification
        fields = '__all__'


class ApplicationConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status', 'comment']  


