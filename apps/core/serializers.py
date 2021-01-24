from rest_framework import serializers

# Create your models here.
class BaseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        Model = self.Meta.model
        user = self.context.get('request').user

        company_id = self.context['request'].auth['company']
        validated_data['created_by'] = user
        validated_data['updated_by'] = user

        if getattr(Model, 'company', None):
            validated_data['company_id'] = company_id

        obj = Model.objects.create(**validated_data)
        obj.save()
        return obj

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        instance.__dict__.update(validated_data)
        instance.updated_by = user
        instance.save()
        return instance

    class Meta:
        exclude = ['created_by', 'updated_by', 'created', 'modified', 'is_removed']
        
