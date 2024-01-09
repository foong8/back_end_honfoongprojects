from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField
from django.db import models


from taggit.managers import TaggableManager
from datetime import datetime, timedelta

class Post(models.Model):
    
    def get_deadline():
        return datetime.today() + timedelta(days=7)

    CHOICES_COUNTRY = (
        ("MY", "MY"),
        ("SG","SG"),
        ("TW", "TW"),
        ("TH", "TH"),
        ("VN","VN")
    )

    CHOICES_CATEGORY = (
        ("System_Change_Request", "System_Change_Request"),
        ("System_Bug","System_Bug"),
        ("General", "General"),
        ("Ad_Hoc_Requests", "Ad_Hoc_Requests"),
        ("Routine_Tasks","Routine_Tasks")
    )

    CHOICES_SUBCAT = (
        ("Module_A","Module_A"),
        ("Module_B","Module_B"),
        ("Module_C","Module_C"),
        ("Module_D","Module_D"),
    )

    CHOICES_STATUS = (
        ("New", "New"),
        ("Working_In_Progress", "Working_In_Progress"),
        ("Pending_Review", "Pending_Review"),
        ("Pending_Approve", "Pending_Approve"),
        ("Completed","Completed"),
        ("Request_To_Cancel","Request_To_Cancel"),
        ("Cancelled", "Cancelled"),
        ("Request_To_Reopen", "Request_To_Reopen"),
    )

    CHOICES_PRIORITY = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Urgent", "Urgent"),
    )

    CHOICES_GENERAL = (
        ("Others", "Others"),
        ("Public_Holidays", "Public_Holidays"),
        ("Process", "Process"),
        ("Documentation", "Documentation"),        
    )


    # main attribute    
    # choices
    category=models.CharField(max_length=255, choices=CHOICES_CATEGORY, default="General")
    subcat=models.CharField(max_length=255, choices=CHOICES_SUBCAT, default="Module_A",blank=True,null=True)
    general_title=models.CharField(max_length=255, choices=CHOICES_GENERAL, default="Others",blank=True,null=True)
    priority=models.CharField(max_length=255, choices=CHOICES_PRIORITY, default="Low",blank=True,null=True)
    due_date=models.DateField(default=get_deadline)
    country_tag=TaggableManager()

    # details
    title=models.CharField(max_length=255)
    details=models.CharField(max_length=255,blank=True,null=True)
    description=models.CharField(max_length=255,blank=True,null=True)
    remarks=models.CharField(max_length=255,blank=True,null=True)
    status=models.CharField(max_length=255, choices=CHOICES_STATUS, default="New")
    uploadfile=models.FileField(upload_to="",blank=True,null=True)
    flag_overdue=models.BooleanField(default=False)
    
    # approval workflow
    requester=models.ForeignKey(User, related_name='post_requester', on_delete=models.CASCADE,blank=True,null=True)
    assignee=models.ForeignKey(User, related_name='post_assignee', on_delete=models.CASCADE,blank=True,null=True)
    reviewer=models.ForeignKey(User, related_name='post_reviewer', on_delete=models.CASCADE,blank=True,null=True)
    approver=models.ForeignKey(User, related_name='post_approver', on_delete=models.CASCADE,blank=True,null=True)

    # standard attribute
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category"]
        verbose_name_plural = "Posts"



class ActionItem(models.Model):
    post=models.ForeignKey(Post, related_name='actionitem_post', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    details=models.CharField(max_length=255, blank=True, null=True)
    completed_date=models.DateField(blank=True, null=True)
    completed_flag=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, related_name='actionitem_created_by', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["title"]
        verbose_name_plural = "ActionItems"

    def __str__(self):
        return str(self.title) 

class ActionItemComment(models.Model):
    actionitem=models.ForeignKey(ActionItem, related_name='comment_actionitem', on_delete=models.CASCADE)
    details=models.TextField(max_length=255, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "ActionItemComments"   

    def __str__(self):
        return str(self.actionitem) 

class Progress(models.Model):
    post=models.ForeignKey(Post, related_name='progress_post', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.TextField(max_length=255, blank=True, null=True)
    action_date=models.DateField(blank=True, null=True)

    # standard attribute
    created_by=models.ForeignKey(User, related_name='progress_created_by', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["action_date"]
        verbose_name_plural = "Progresses"    

class Comment(models.Model):

    post=models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    detail=models.TextField(max_length=255, blank=True, null=True)
    # standard attribute
    created_by=models.ForeignKey(User, related_name='comment_created_by', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Comments"

class HistoryLog(models.Model):
    post=models.ForeignKey(Post, related_name='historylog_post', on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    # standard attribute
    created_by=models.ForeignKey(User, related_name='historylog_created_by', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "HistoryLogs"