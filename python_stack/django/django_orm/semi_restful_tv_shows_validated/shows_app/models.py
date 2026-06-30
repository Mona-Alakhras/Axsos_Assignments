from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData, show_id=None):
        errors = {}
        
        if len(postData.get('title', '')) < 2:
            errors['title'] = "Title should be at least 2 characters."
            
        if len(postData.get('network', '')) < 3:
            errors['network'] = "Network should be at least 3 characters."
            
        desc = postData.get('description', '').strip()
        if len(desc) > 0 and len(desc) < 10:
            errors['description'] = "Description should be at least 10 characters if provided."

        release_date_str = postData.get('release_date', '')
        if not release_date_str:
            errors['release_date'] = "Release date is required."
        else:
            release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
            if release_date >= datetime.today().date():
                errors['release_date'] = "Release date should be in the past."

        title = postData.get('title', '')
        existing_shows = Show.objects.filter(title=title)
        
        if show_id:
            existing_shows = existing_shows.exclude(id=show_id)
            
        if existing_shows.exists():
            errors['unique_title'] = "A TV Show with this title already exists."

        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()