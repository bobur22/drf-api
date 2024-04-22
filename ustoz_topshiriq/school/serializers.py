from rest_framework import serializers

from .models import StudentModel, CourseModel, ModuleModel, GradesModel, ClassModel, AttendanceLogModel


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        # fields = '__all__'
        exclude = ['created_at', 'updated_at']


class CourseModelSerializer(serializers.ModelSerializer):
    students =  serializers.PrimaryKeyRelatedField(queryset=StudentModel.objects.all(), many=True)
    # students = StudentModelSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModel
        fields = ['course_name', 'course_start_date', 'course_end_date', 'students']
        # exclude = ['id', 'created_at', 'updated_at']


class ModuleModelSerializer(serializers.ModelSerializer):
    # student = serializers.PrimaryKeyRelatedField(queryset=StudentModel.objects.all(), many=True)
    students = StudentModelSerializer(many=True, read_only=True)
    class Meta:
        model = ModuleModel
        # fields = '__all__'
        exclude = ['id', 'created_at', 'updated_at']


class GradesModelSerializer(serializers.ModelSerializer):
    module = ModuleModelSerializer()
    print(module)
    class Meta:
        model = GradesModel
        exclude = ['id', 'created_at', 'updated_at']


class ClassModelSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(queryset=ModuleModel.objects.all(), many=True)
    # module = ModuleModelSerializer(many=True, read_only=True)
    class Meta:
        model = ClassModel
        # fields = '__all__'
        exclude = ['id']


class AttendanceLogSerializer(serializers.ModelSerializer):
    student_attendance = StudentModelSerializer()
    class_s = ClassModelSerializer()
    class Meta:
        model = AttendanceLogModel
        exclude = ['id', 'created_at', 'updated_at']
