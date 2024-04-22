from django.db import models


class StudentModel(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class CourseModel(models.Model):
    course_name = models.CharField(max_length=100)
    course_start_date = models.DateField()
    course_end_date = models.DateField()

    students = models.ManyToManyField(StudentModel, related_name='course_students')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course_name}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class ModuleModel(models.Model):
    module_name = models.CharField(max_length=100)

    student = models.ManyToManyField(StudentModel, related_name='module_students', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.module_name

    class Meta:
        verbose_name = 'module'
        verbose_name_plural = 'modules'


class GradesModel(models.Model):
    grade = models.PositiveIntegerField(default=0)

    student_grade = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='student_grade')
    module = models.ForeignKey(ModuleModel, on_delete=models.CASCADE, related_name='module_grade')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grade}"

    class Meta:
        verbose_name = 'grade'
        verbose_name_plural = 'grades'


class ClassModel(models.Model):
    class_date = models.DateField()

    module = models.ManyToManyField(ModuleModel)

    class_start_time = models.TimeField()
    class_end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_date}"

    class Meta:
        verbose_name = 'class'
        verbose_name_plural = 'classes'


class AttendanceLogModel(models.Model):
    status = models.BooleanField(default=False)

    student_attendance = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='student_attendance')
    class_s = models.ForeignKey(ClassModel, on_delete=models.CASCADE, related_name='class_attendance')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.class_s} - {self.student_attendance.f_name} {self.student_attendance.l_name}'

    class Meta:
        verbose_name = 'attendance'
        verbose_name_plural = 'attendances'
