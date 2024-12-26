from django import forms
from .models import Student, Faculty, Course, Enrollment, Grade, Schedule

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['FirstName', 'LastName', 'Email', 'Phone', 'Major', 'EnrollmentDate']

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['FirstName', 'LastName', 'Email', 'Phone', 'Department']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['CourseName', 'Credits', 'FacultyID']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['StudentID', 'CourseID', 'EnrollmentDate']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['EnrollmentID', 'Grade']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['CourseID', 'DayOfWeek', 'StartTime', 'EndTime', 'Location']
