from django.db import models

# Create your models here.
class Feedback(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(1, "Very Bad"), (2, "Bad"), (3, "Neutral"), (4, "Good"), (5, "Excellent")])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.rating}/5"

class SocialMediaComment(models.Model):
    PLATFORM_CHOICES = [
        ("twitter", "X (Twitter)"),
        ("pinterest", "Pinterest"),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    comment_text = models.TextField()
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.platform})"

class SentimentAnalysis(models.Model):
    SENTIMENT_CHOICES = [
        ("positive", "Positive"),
        ("neutral", "Neutral"),
        ("negative", "Negative"),
    ]
    
    comment = models.ForeignKey(SocialMediaComment, on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=10, choices=SENTIMENT_CHOICES)
    score = models.FloatField()  # Sentiment score from analysis
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment.username} - {self.sentiment}"
