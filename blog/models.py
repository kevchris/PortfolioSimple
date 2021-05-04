from django.db import models

# Create your Blog model here.
class Blog(models.Model):
    title=models.CharField(max_length=255)
    pubDate=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
# title, published date, body, image
# Add blog app to settings
#create a migration
#migrate
#add to the admin
