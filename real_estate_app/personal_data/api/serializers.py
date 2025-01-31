from rest_framework import serializers

from personal_data.models import PersonalData


class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'


class PersonalFullDataCreateXerializer(serializers.ModelSerializer):
    class Meta(PersonalDataSerializer.Meta):
        fields = 'city', 'target', 'type_of_housing', 'payment_type', 'full_name', 'phone_number',


class PersonalShortDataCreateXerializer(serializers.ModelSerializer):
    class Meta(PersonalDataSerializer.Meta):
        fields = 'full_name', 'phone_number',
