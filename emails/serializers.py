import mimetypes
from rest_framework import serializers
from .models import Email


class EmailSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    attachment = serializers.FileField(required=False)
    attachment_detail = serializers.SerializerMethodField()

    # Allowed file types list for validation
    ALLOWED_FILE_TYPES = [
        {'type': 'JPEG', 'content_type': 'image/jpeg'},
        {'type': 'PNG', 'content_type': 'image/png'},
        {'type': 'PDF', 'content_type': 'application/pdf'},
        {'type': 'DOCX', 'content_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'},
        {'type': 'XLSX', 'content_type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'},
        {'type': 'DOC', 'content_type': 'application/msword'},
        {'type': 'XLS', 'content_type': 'application/vnd.ms-excel'}
    ]

    class Meta:
        model = Email
        fields = '__all__'
        extra_fields = ['attachment_detail']

    def validate_attachment(self, value):
        allowed_content_types = [file['content_type'] for file in self.ALLOWED_FILE_TYPES]

        if value.content_type not in allowed_content_types:
            allowed_types_str = ", ".join([file['type'] for file in self.ALLOWED_FILE_TYPES])
            raise serializers.ValidationError(f"Unsupported file type. Allowed types are: {allowed_types_str}.")

        return value

    def get_attachment_detail(self, obj):
        if obj.attachment:
            attachment_path = obj.attachment.name
            mime_type, _ = mimetypes.guess_type(attachment_path)

            return {
                "name": attachment_path.split('/')[-1],
                "type": mime_type if mime_type else "Unknown",
                "url": obj.attachment.url
            }
        return None
