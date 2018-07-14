from django.db import models


class Message(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.message) > 30:
            return u"{0}:{1}".format(self.id, self.message[:27]+'...')
        else:
            return u"{0}:{1}".format(self.id, self.message)

    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)
