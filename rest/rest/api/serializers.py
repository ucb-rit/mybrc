from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    """Serializer mapping from Model instance to the JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        
        model = User
        fields = ('userid', 'accounts', 'username', 'usermetadata', 'email', 'ldapuid', 'created', 'updated')

class JobSerializer(serializers.ModelSerializer):                                                                    
    """Serializer mapping from Model instance to the JSON format."""                                                  
                                                                                                                      
    class Meta:                                                                                                       
        """Meta class to map serializer's fields with the model fields."""                                            
        model = Job
        fields = ('jobnumber', 'jobslurmid', 'submitdate', 'startdate', 'enddate', 'userid', 'accountid', 'amount', 'jobstatus', 'partition', 'qos', 'created', 'updated')

class AccountSerializer(serializers.ModelSerializer):
    """Serializer mapping from Model instance to the JSON format."""
                                                                                                                      
    class Meta:                                                                                                       
        """Meta class to map serializer's fields with the model fields."""                                            
        model = Account
        fields = ('accountid', 'users', 'accountname', 'accountallocation', 'accountbalance', 'type', 'description', 'created', 'updated')

class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Useraccountassociation
        fields = ('userid', 'accountid', 'userallocation', 'userbalance', 'created', 'updated')
