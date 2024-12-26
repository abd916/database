from django.db import models


# جدول الطلاب
class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Major = models.CharField(max_length=100)
    EnrollmentDate = models.DateField()

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

# جدول أعضاء هيئة التدريس
class Faculty(models.Model):
    FacultyID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Department = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

# جدول المقررات الدراسية
class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    Credits = models.IntegerField()
    FacultyID = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.CourseName

# جدول التسجيل
class Enrollment(models.Model):
    EnrollmentID = models.AutoField(primary_key=True)
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    EnrollmentDate = models.DateField()

    def __str__(self):
        return f"Enrollment {self.EnrollmentID}"

# جدول الدرجات
class Grade(models.Model):
    GradeID = models.AutoField(primary_key=True)
    EnrollmentID = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    Grade = models.CharField(max_length=2)  # e.g., A, B, C, etc.

    def __str__(self):
        return f"Grade {self.GradeID}: {self.Grade}"

# جدول الجداول الدراسية
class Schedule(models.Model):
    ScheduleID = models.AutoField(primary_key=True)
    CourseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    DayOfWeek = models.CharField(max_length=10)  # e.g., Monday
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Location = models.CharField(max_length=100)

    def __str__(self):
        return f"Schedule {self.ScheduleID} for {self.CourseID}"

