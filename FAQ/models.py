from django.db import models

class Question(models.Model):
    question= models.CharField(max_length=200)
    answer= models.CharField(max_length=200)
    parent= models.CharField(max_length=200)
    created_at = models.DateTimeField('date created',blank=True)
    def __str__(self):
        return self.question


class Users(models.Model):
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(help_text="Please Input a valid Email address")
    password=models.CharField(max_length=200)


class UsersSession(models.Model):
    session_id=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)