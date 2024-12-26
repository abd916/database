from django.shortcuts import render, redirect
from .models import Student, Faculty, Course, Enrollment, Grade, Schedule
from .forms import StudentForm, FacultyForm, CourseForm, EnrollmentForm, GradeForm, ScheduleForm

# الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')

# إضافة طالب
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# إضافة عضو هيئة تدريس
def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', {'form': form})

# إضافة مقرر دراسي
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

# إضافة تسجيل
def add_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'add_enrollment.html', {'form': form})

# إضافة درجة
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'add_grade.html', {'form': form})

# إضافة جدول دراسي
def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})

# قائمة الطلاب
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# قائمة أعضاء هيئة التدريس
def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty_list.html', {'faculties': faculties})

# قائمة المقررات الدراسية
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# قائمة التسجيلات
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})

# قائمة الدرجات
def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade_list.html', {'grades': grades})

# قائمة الجداول الدراسية
def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})
