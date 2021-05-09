from django.db import models

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
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]

    def pretty_date(self):
        return self.pubDate.strftime('%b %e %Y')
