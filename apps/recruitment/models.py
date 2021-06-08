from django.db import models
from django.contrib.postgres.fields import ArrayField

## Django signal Import
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid

# Create your models here.

## Questions taken from the domain recruiters and pushed into database of this model.
## Both for Form responses and form filling frontend (questions and options) can be taken from here to display.
class QuestionsForRecruitment(models.Model):
    CHOICES_QTYPE = [
        ('SingleChoice', 'SingleChoice'),
        ('MultipleChoice', 'MultipleChoice'),
        ('Answer', 'Answer'),
    ]

    CHOICES_DOMAIN = [
        ('All', 'All'),
        ('Web', 'Web'),
        ('Core', 'Core'),
        ('Design', 'Design'),
        ('Docs', 'Docs'),
        ('PR', 'PR'),
    ]

    question  = models.CharField(max_length=1000)
    question_id = models.AutoField(primary_key=True)
    question_type  = models.CharField(max_length=1000, choices=CHOICES_QTYPE)
    question_for_domain  = models.CharField(max_length=1000, choices=CHOICES_DOMAIN)
    option1 = models.CharField(max_length=1000, blank=True)
    option2 = models.CharField(max_length=1000, blank=True)
    option3 = models.CharField(max_length=1000, blank=True)
    option4 = models.CharField(max_length=1000, blank=True)



## Every candidates responses 
class SubmittedUser(models.Model):
    candidate_name = models.CharField(max_length=1000)
    candidate_id = models.UUIDField(primary_key=True, default=uuid.uuid4, auto_created=True, unique=True)
    candidate_mobile_number = models.CharField(max_length=10)
    candidate_emailid = models.EmailField()
    candidate_domain_choices = ArrayField(models.CharField(max_length=100, blank=True),size=2)      ## Limiting the choices to only two.


class FormResponses(models.Model):
    question_id = models.ForeignKey('QuestionsForRecruitment', on_delete=models.CASCADE , null=True)
    submitted_candidate_id = models.ForeignKey('SubmittedUser', on_delete=models.CASCADE, null=True)
    answer_given = models.CharField(max_length=20000, blank=True)
    options_answer_selected =  ArrayField(models.CharField(max_length=100, blank=True), size=4, null=True, blank=True)


## Saving the emails and phone numbers to Global level Email and Phone number DB
# @receiver(post_save,sender=FormResponses)
# def global_email(created,instance,*args,**kwargs):
#     if created:
#         ## For Global level Email save
#         pass