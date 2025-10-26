from django.db import models

# Create your models here.


#One to One Relationship Example
class Female(models.Model):
    female_name = models.CharField(default='name', max_length=20)
    female_age = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.female_name
    
class Male(models.Model):
    male_name = models.CharField(default='name', max_length=20)
    male_age = models.IntegerField(default=0, null=False, blank=False)
    girls = models.OneToOneField(Female, on_delete=models.CASCADE) #CASCADE, SET_NULL, PROTECT, DO_NOTHING, SET_DEFAULT

    def __str__(self):
        return self.male_name
    
# One to Many Relationship Example

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    

# Many to Many Relationship Example
class Student(models.Model):
    student_name = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.course_name
    

class Login(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)