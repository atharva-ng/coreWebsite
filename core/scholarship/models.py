# core/scholarship/models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class SummerResearchApplication(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    project_objective = models.TextField()
    past_research = models.TextField()
    personal_statement = models.TextField()
    cv = models.FileField(
        upload_to='summer_research_applications/cv/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    acceptance_letter = models.FileField(
        upload_to='summer_research_applications/acceptance_letters/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    
    # Additional fields for data management
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('under_review', 'Under Review'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.name} - {self.id_number}"

    class Meta:
        verbose_name = "Summer Research Application"
        verbose_name_plural = "Summer Research Applications"


class SupportingDocument(models.Model):
    application = models.ForeignKey(
        SummerResearchApplication,
        related_name='supporting_documents',
        on_delete=models.CASCADE
    )
    file = models.FileField(
        upload_to='summer_research_applications/supporting_documents/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.application.name}"
