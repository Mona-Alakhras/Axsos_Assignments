from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData.get('name', '')) <= 5:
            errors['name'] = "Course name should be more than 5 characters."
            
        if len(postData.get('description', '')) <= 15:
            errors['description'] = "Description should be more than 15 characters."
            
        return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CourseManager()

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
