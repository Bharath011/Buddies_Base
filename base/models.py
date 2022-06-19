from tkinter import CASCADE
from turtle import update
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Room(models.Model):

    host=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    #participants=
    #taking time stamps when saved and created
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    #for ordering of rooms by recent updates
    class Meta:
        ordering=['-updated','created']

    def __str__(self) -> str:
        return self.name
    
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #message is a child table of room table as messaging is done in rooms
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    #the message is stored here
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:30]
    

