from pybo.models import Question, Answer 
from django.utils import timezone
import os
q = Question(subject='what is pybo', content='wanna konw about pybo',create_date=timezone.now())
#
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
q.save()
q.id
q = Question(subject='this is django model Question', content='id is nomally automatically created?',create_date=timezone.now())
q.save()
q.id
Question.objects.all()