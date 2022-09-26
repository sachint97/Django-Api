from django.db import models
from django.template.defaultfilters import slugify

# unique slugify generator
def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    record_count = 0
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + "-1"
        while model.objects.filter(slug=unique_slug).exists():
            record_count = record_count + 1
            unique_slug = slug + "-" + str(record_count)
    return unique_slug

# Create your models here.
class College(models.Model):
    college_name= models.CharField(max_length=100, null=False , blank=False)
    college_address = models.CharField(max_length=100, null=False , blank=False)
    slug = models.SlugField(max_length=250, null=True, editable=False)

    def __str__(self):
        return self.college_name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = slugify(self.college_name)
            self.slug = unique_slugify(self, slug_text)
        self.clean()
        super().save(*args, **kwargs)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100, null=False , blank=False)
    teacher_subject = models.CharField(max_length=100, null=False , blank=False)
    slug = models.SlugField(max_length=250, null=True, editable=False)

    def __str__(self):
        return self.teacher_name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = slugify(self.teacher_name)
            self.slug = unique_slugify(self, slug_text)
        self.clean()
        super().save(*args, **kwargs)
    

class Student(models.Model):
    student_name = models.CharField(max_length=100, null=False , blank=False)
    student_roll_no = models.IntegerField(null=False , blank = False)
    college = models.ForeignKey(College,null=False, blank=False, related_name='student_college', default=None, on_delete=models.CASCADE )
    guide = models.ForeignKey(Teacher,null=False, blank=False, related_name='student_teacher', default=None, on_delete=models.CASCADE )
    slug = models.SlugField(max_length=250, null=True, editable=False)

    def __str__(self):
        return self.student_name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = slugify(self.student_name)
            self.slug = unique_slugify(self, slug_text)
        self.clean()
        super().save(*args, **kwargs)