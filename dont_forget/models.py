from django.db import models

# Create your models here.


class Topic(models.Model):
    '''A way to create a new topic in the Don't Forget app'''
    text = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



class Entry(models.Model):
    '''An entry within a newly created topic'''
    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "topics"


    def __str__(self):
        return self.text[:50] + "..."



class Note(models.Model):
    '''A way to create a new note in the Don't Forget app'''
    text = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class NoteEntry(models.Model):
    '''An item within a newly created note'''
    note = models.ForeignKey(Note,  on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)


    class Meta:
        verbose_name_plural = "notes"


    def __str__(self):
        return self.text[:50]

