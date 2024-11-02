from django.db import models

# Create your models here.

class Chats(models.Model):
    username = models.CharField(max_length=200, unique=True)
    instruction = models.TextField(max_length=200, default='')

    def clear(self):
        self.instruction = ''
        for message in self.messages:
            message.delete()
        return True


class Message(models.Model):
    chat = models.ForeignKey(Chats, related_name="messages", null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=20)
    textContent = models.TextField(null=True)
    file = models.URLField("filepath", null=True)

    def __str__(self):
        return f"{self.role}: {self.textContent} {self.file and '[file]'}"


    def process(self):
        parts = []

        if self.file:
            parts.append(self.file)
        parts.append(self.textContent)

        return {
            "role": self.role,
            "parts": parts
        }