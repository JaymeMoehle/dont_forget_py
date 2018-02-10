from django.db import models

# Create your models here.


class Note(models.Model):
    '''A way to create a new note in the Don't Forget app'''
    text = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''An entry within a newly created note'''
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "notes"


    def __str__(self):
        return self.text[:50] + "..."
