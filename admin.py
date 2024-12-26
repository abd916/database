from django.contrib import admin

from .models import Student, Course, Enrollment ,Grade,Schedule,Faculty  # تأكد من استيراد جميع النماذج

# تسجيل جميع النماذج في الـ Admin
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Faculty)
admin.site.register(Grade)
admin.site.register(Schedule)





