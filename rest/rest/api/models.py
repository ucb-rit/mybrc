# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(models.Model):
    accountid = models.AutoField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
    users = models.ManyToManyField(
        'User',
        through='Useraccountassociation',
        through_fields=('accountid', 'userid')
    )
    accountname = models.CharField(db_column='AccountName', max_length=50)  # Field name made lowercase.
    accountallocation = models.IntegerField(db_column='AccountAllocation')  # Field name made lowercase.
    accountbalance = models.IntegerField(db_column='AccountBalance')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150)  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'Account'


class Accounttransaction(models.Model):
    transactionid = models.AutoField(db_column='TransactionID', primary_key=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountID')  # Field name made lowercase.
    allocatedon = models.DateTimeField(db_column='AllocatedOn')  # Field name made lowercase.
    newaccountallocation = models.FloatField(db_column='NewAccountAllocation')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
    accountmetadata = models.TextField(db_column='AccountMetadata')  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'AccountTransaction'


class Job(models.Model):
    jobnumber = models.BigAutoField(db_column='JobNumber', primary_key=True)  # Field name made lowercase.
    jobslurmid = models.IntegerField(db_column='JobSlurmID')  # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='SubmitDate')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountID')  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    jobstatus = models.IntegerField(db_column='JobStatus')  # Field name made lowercase.
    partition = models.IntegerField(db_column='Partition')  # Field name made lowercase.
    qos = models.SmallIntegerField(db_column='QOS')  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'Job'


class Jobstatusdict(models.Model):
    jobstatus = models.AutoField(db_column='JobStatus', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150)  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'JobStatusDict'


class Partitiondict(models.Model):
    partition = models.AutoField(db_column='Partition', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150)  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'PartitionDict'


class Permdict(models.Model):
    perm = models.AutoField(db_column='Perm', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150)  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'PermDict'


class Qosdict(models.Model):
    qos = models.SmallIntegerField(db_column='QOS', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=150)  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'QOSDict'


class Role(models.Model):
    accountid = models.IntegerField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    permission = models.IntegerField(db_column='Permission', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'Role'
        unique_together = (('accountid', 'userid'),)


class Roledict(models.Model):
    role = models.AutoField(db_column='Role', primary_key=True)  # Field name made lowercase.
    perm = models.IntegerField(db_column='Perm')  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'RoleDict'


class Superuser(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    ldapuid = models.IntegerField(db_column='LDAPUID')  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'SuperUser'


class User(AbstractBaseUser):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    accounts = models.ManyToManyField(
        'Account',
        through='Useraccountassociation',
        through_fields=('userid', 'accountid')
    )
    username = models.CharField(db_column='UserName', max_length=20, unique=True)  # Field name made lowercase.
    usermetadata = models.TextField(db_column='UserMetadata')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    ldapuid = models.IntegerField(db_column='LDAPUID')  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    # Required fields for AbstractBaseUser
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username, calnetuid']

    # Calnet UID is the 'password' field of the User.

    class Meta:
        db_table = 'User'


class Useraccountassociation(models.Model):
    useraccountassociationid = models.AutoField(db_column='id', primary_key=True)
    userid = models.ForeignKey(User, db_column='UserID')
    accountid = models.ForeignKey(Account, db_column='AccountID')
    userallocation = models.IntegerField(db_column='UserAllocation')  # Field name made lowercase.
    userbalance = models.IntegerField(db_column='UserBalance')  # Field name made lowercase.
    created = models.DateTimeField(auto_now_add=True, db_column='Created')  # Field name made lowercase.
    updated = models.DateTimeField(auto_now_add=True, db_column='Updated')  # Field name made lowercase.

    class Meta:
        db_table = 'UserAccountAssociation'
        unique_together = (('userid', 'accountid'),)
