from django.db import models

# Create your models here.

class teacher(models.Model):
    first_name= models.CharField(max_length=50)
    last_name=  models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date_join = models.DateField(auto_now=False, auto_now_add=False)
    is_active: models.IntegerField()
    password = models.CharField(max_length=50)
    last_login = models.DateField(auto_now=False, auto_now_add=False)
    addhar_no = models.BigIntegerField()
    fathers_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    img = models.ImageField(upload_to='pics')
    addrress = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    class_teacher_of = models.CharField(max_length=50,null=True)
    salary = models.IntegerField()
    emp_status = models.CharField(max_length=50)
    e_id = models.IntegerField()

class timetable(models.Model):
    e_id = models.ForeignKey(teacher, on_delete=models.CASCADE)
    days = models.CharField(max_length=50)
    period_1 = models.CharField(max_length=50)
    period_2 = models.CharField(max_length=50)
    period_3 = models.CharField(max_length=50)
    period_4 = models.CharField(max_length=50)
    period_5 = models.CharField(max_length=50)
    period_6 = models.CharField(max_length=50)
    period_7 = models.CharField(max_length=50)
    period_8 = models.CharField(max_length=50)
    period_9 = models.CharField(max_length=50)

class student(models.Model):
    adm_no = models.CharField(max_length=50,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_no = models.BigIntegerField(default=1234567890)
    date_join = models.DateField(auto_now=False, auto_now_add=False)
    addhar_no = models.BigIntegerField()
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    addrress = models.CharField(max_length=50)
    class_in = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    roll_no = models.IntegerField()

class student_marks(models.Model):
    adm_no=models.ForeignKey(student,default=1, on_delete=models.SET_DEFAULT)
    subject=models.CharField(max_length=50)
    marks_in_theory = models.CharField(max_length=50)
    marks_in_practical = models.CharField(max_length=50)


