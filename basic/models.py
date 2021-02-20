from django.db import models

# Create your models here.

class Location(models.Model):
    area_name = models.CharField(max_length=255)

    def __str__(self):
        return self.area_name

class School(models.Model):
    Sname = models.CharField(max_length=255)
    Slocation  = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.Sname

class Teacher(models.Model):
    tname = models.CharField(max_length=255)
    tsubject = models.CharField(max_length=255)
    teacher_school = models.ManyToManyField(School)

    def __str__(self):
        return self.tname

class Student(models.Model):
    name = models.CharField(max_length=255)
    student_school = models.ForeignKey(School,on_delete=models.CASCADE)
    student_teacher =  models.ManyToManyField(Teacher)
    student_address = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        db_table='StudentModel'




