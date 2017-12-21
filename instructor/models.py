from django.db import models


RESPONSE_TYPES = [
        (1, 'Radio Select'), (2, 'Text Field'), (3, 'Multiple Choice')
]

RADIO_CHOICE = [
    (2, 'Very Good'), (1, 'Good'), (0, 'Okay'),
    (-1, 'Bad'), (-2, 'Very Bad')
]

SEMESTERS = [(i, i) for i in range(1, 9)]


class Users(models.Model):
    username = models.SlugField(unique=True, max_length=63)
    password = models.SlugField(max_length=63, default=None)
    role = models.ForeignKey('Roles', on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class Roles(models.Model):
    role = models.CharField(max_length=63)

    def __str__(self):
        return self.role


class Classes(models.Model):
    stream = models.CharField(max_length=127)
    semester = models.SmallIntegerField(choices=SEMESTERS)

    class Meta:
        unique_together = ("stream", "semester")

    def __str__(self):
        return str(self.stream) + ' - ' + str(self.semester)


class Courses(models.Model):
    code = models.SlugField(max_length=15, unique=True)
    name = models.CharField(max_length=127)
    instructor = models.ForeignKey('Users', on_delete=models.CASCADE,
                                   blank=True, null=True)
    class_id = models.ForeignKey('Classes', on_delete=models.CASCADE,
                                 blank=False, null=False)

    def __str__(self):
        return self.name


class Questions(models.Model):
    text = models.TextField(unique=True)
    response_type = models.SmallIntegerField(choices=RESPONSE_TYPES,
                                             default=1)

    def __str__(self):
        return self.text


class Feedback(models.Model):
    review = models.SmallIntegerField(choices=RADIO_CHOICE, default=0,
                                      blank=True, null=False)
    question = models.ForeignKey('Questions', on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        return self.get_review_display() + ' ' + self.question.text
