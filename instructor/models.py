from django.db import models


SEMESTERS = [ (i, i) for i in range(1,9) ]
STREAMS = [
        ( 1, 'Computer Science and Engineering' ),
        ( 2, 'Electrical and Electronics Engineering' ),
        ( 3, 'Electronics and Communications Engineering' ),
        ( 4, 'Mechanical Engineering' ),
        ]
RESPONSE_TYPES = [
        ( 1, 'Radio Select'),
        ( 2, 'Text Field'),
        ( 3, 'Multiple Choice'),
        ]


class Users(models.Model):
    username = models.SlugField(unique=True, max_length=63)
    password = models.SlugField(max_length=127)
    role = models.ForeignKey('Roles', on_delete=models.PROTECT)


class Roles(models.Model):
    role = models.CharField(max_length=63)



class Classes(models.Model):
    stream = models.SmallIntegerField(choices=STREAMS)
    semester = models.SmallIntegerField(choices=SEMESTERS)



class Courses(models.Model):
    code = models.SlugField(max_length=15, unique=True)
    name = models.CharField(max_length=127)



class Questions(models.Model):
    text = models.TextField(unique=True)
    response_type = models.SmallIntegerField(choices=RESPONSE_TYPES)


class Feedback(models.Model):
    # todo: Defines attributes to be used in forms
    # todo: Radioboxes, TextArea, Submit button
    pass
