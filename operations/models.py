"""
    ****Change Update Log****
    DDMMYY: Change Description

"""

from django.contrib.auth.models import User
from django.db import models

class Country(models.Model):
    CHOICES_CATEGORY = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
    )
    # primary attribute
    name=models.CharField(max_length=255)
    short_name=models.CharField(max_length=255)
    first_letter=models.CharField(max_length=255)
    category=models.CharField(max_length=255, choices=CHOICES_CATEGORY, default="A")
    # backup attribute
    attribute_one=models.CharField(max_length=255, blank=True, null=True)
    attribute_two=models.CharField(max_length=255, blank=True, null=True)
    attribute_three=models.CharField(max_length=255, blank=True, null=True)
    attribute_four=models.CharField(max_length=255, blank=True, null=True)
    attribute_five=models.CharField(max_length=255, blank=True, null=True)
    # standard attribute
    created_by=models.ForeignKey(User, related_name='created_country', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)    
    modified_by=models.ForeignKey(User, related_name='updated_country', on_delete=models.CASCADE, blank=True, null=True)
    modified_at=models.DateField(auto_now=True)

    class Meta:
        ordering = ["short_name"]
        verbose_name_plural = "Countries"

class Assignment(models.Model):
    # primary attribute
    country=models.ForeignKey(Country, related_name='assignment_country',on_delete=models.CASCADE)
    role_actual=models.ForeignKey(User, related_name='role_actual', on_delete=models.CASCADE)    
    role_s_one=models.ForeignKey(User, related_name='role_s_one', on_delete=models.CASCADE)    
    role_s_two=models.ForeignKey(User, related_name='role_s_two', on_delete=models.CASCADE)    
    role_s_three=models.ForeignKey(User, related_name='role_s_three', on_delete=models.CASCADE)    
    role_s_test=models.ForeignKey(User, related_name='role_s_test', on_delete=models.CASCADE)
    # backup attribute
    attribute_one=models.CharField(max_length=255, blank=True, null=True)
    attribute_two=models.CharField(max_length=255, blank=True, null=True)
    attribute_three=models.CharField(max_length=255, blank=True, null=True)
    attribute_four=models.CharField(max_length=255, blank=True, null=True)
    attribute_five=models.CharField(max_length=255, blank=True, null=True)
    # standard attribute
    created_by=models.ForeignKey(User, related_name='created_assignment', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)    
    modified_by=models.ForeignKey(User, related_name='updated_assignment', on_delete=models.CASCADE, blank=True, null=True)
    modified_at=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.country.id)

    class Meta:
        verbose_name_plural = "Assignments"

class Qcticket(models.Model):
    CHOICES_ROLES = (
        ("Actual", "Actual"),
        ("Shadow_1", "Shadow_1"),
        ("Shadow_2", "Shadow_2"),
        ("Shadow_3", "Shadow_3"),
        ("Shadow_test", "Shadow_test"),
    )

    CHOICES_QCRESULT= (
        ("No_Error", "No_Error"),
        ("Has_Error", "Has_Error")
    )

    CHOICES_STATUS = (
        ("In_Queue", "In_Queue"),
        ("Completed", "Completed"),
    )

    requester=models.ForeignKey(User, related_name='requester', on_delete=models.CASCADE)
    country=models.ForeignKey(Country, related_name='ticket_country',on_delete=models.CASCADE)
    role_1=models.CharField(max_length=255, choices=CHOICES_ROLES, default="Actual")  
    role_2=models.CharField(max_length=255, choices=CHOICES_ROLES, default="Shadow_1")   
    qcfile=models.CharField(max_length=255, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True) 
    qcresult=models.CharField(max_length=255, choices=CHOICES_QCRESULT, blank=True, null=True)
    status=models.CharField(max_length=255, choices=CHOICES_STATUS, default="In_Queue")
    mistaked_made_by=models.ForeignKey(User, related_name='user_qclog', on_delete=models.CASCADE, blank=True, null=True)
    flag_script_process=models.BooleanField(default=False)
    # backup attribute
    attribute_one=models.CharField(max_length=255, blank=True, null=True)
    attribute_two=models.CharField(max_length=255, blank=True, null=True)
    attribute_three=models.CharField(max_length=255, blank=True, null=True)
    attribute_four=models.CharField(max_length=255, blank=True, null=True)
    attribute_five=models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "QcTickets"

class QcLogNote(models.Model):
    note=models.ForeignKey(Qcticket, related_name='ticket_note', on_delete=models.CASCADE)
    note_details=models.TextField(max_length=255, blank=True, null=True)
    # standard attribute
    created_by=models.ForeignKey(User, related_name='created_qclognote', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "QcLogNotes"

class Qclog(models.Model):

    CHOICES_ACTION= (
        ("Submit_Ticket", "Submit_Ticket"),
        ("Running_By_Script", "Running_By_Script"),
        ("Completed_By_Script", "Completed_By_Script"),
    )

    # primary attribute
    qcticket=models.ForeignKey(Qcticket, related_name='qcticket', on_delete=models.CASCADE, blank=True, null=True)
    action=models.CharField(max_length=255, choices=CHOICES_ACTION, default="log_action")   
    
    # backup attribute
    attribute_one=models.CharField(max_length=255, blank=True, null=True)
    attribute_two=models.CharField(max_length=255, blank=True, null=True)
    attribute_three=models.CharField(max_length=255, blank=True, null=True)
    attribute_four=models.CharField(max_length=255, blank=True, null=True)
    attribute_five=models.CharField(max_length=255, blank=True, null=True)
    # standard attribute
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "QcLogs"