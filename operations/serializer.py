from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Country, Assignment, Qclog, Qcticket, QcLogNote


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            "id",
            "username",
            "is_active",
        ) 

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields=(
            'id',
            'name',
            'short_name',
            'first_letter',
            'category',
        )

class AssignmentSerializer(serializers.ModelSerializer):
    country=CountrySerializer(read_only=True)
    role_actual=UserSerializer(read_only=True)
    role_s_one=UserSerializer(read_only=True)
    role_s_two=UserSerializer(read_only=True)
    role_s_three=UserSerializer(read_only=True)
    role_s_test=UserSerializer(read_only=True)
    
    class Meta:
        model=Assignment
        fields='__all__'
        
class QcticketSerializer(serializers.ModelSerializer):
    # requester=UserSerializer(read_only=True)
    # country=CountrySerializer(read_only=True)
    mistaked_made_by=UserSerializer(read_only=True)
    class Meta:
        model=Qcticket
        fields=(
            "id",
            "requester",
            "country",
            "role_1",
            "role_2",
            "qcfile",
            "attribute_one",
            "attribute_two",
            "attribute_three",
            "attribute_four",
            "attribute_five",
            "created_at",
            "status",
            "qcresult",
            "mistaked_made_by"
        )
    
    def to_representation(self, instance):
        self.fields['requester'] =  UserSerializer(read_only=True)
        self.fields['country'] = CountrySerializer(read_only=True)
        return super(QcticketSerializer, self).to_representation(instance) 

class GetQcticketSerializer(serializers.ModelSerializer):
    requester=UserSerializer(read_only=True)
    country=CountrySerializer(read_only=True)
    mistaked_made_by=UserSerializer()
    class Meta:
        model=Qcticket
        fields=(
            "id",
            "requester",
            "country",
            "role_1",
            "role_2",
            "qcfile",
            "attribute_one",
            "attribute_two",
            "attribute_three",
            "attribute_four",
            "attribute_five",
            "created_at",
            "status",
            "qcresult",
            "mistaked_made_by"
        )

class TicketNoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=QcLogNote
        fields='__all__'

class GetTicketNoteSerializer(serializers.ModelSerializer):
    created_by=UserSerializer(read_only=True)
    
    class Meta:
        model=QcLogNote
        fields='__all__'

class QClogSerializer(serializers.ModelSerializer):
    pass
    # qcticket=QcticketSerializer(read_only=True)
    # qclognote=QClogNoteSerializer(read_only=True)
    
    # class Meta:
    #     model=Qclog
    #     fields=(
    #         "qcticket",
    #         "each_qcfile",
    #         "status",
    #         "mistaked_made_by",
    #         "qclognote"
    #         "attribute_one",
    #         "attribute_two",
    #         "attribute_three",
    #         "attribute_four",
    #         "attribute_five",
    #         "created_at",
    #     )
