# core/scholarship/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ApplicationForm
from .models import SummerResearchApplication, SupportingDocument

def scholarship_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save main application data
            application = SummerResearchApplication(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                id_number=form.cleaned_data['id_number'],
                contact_number=form.cleaned_data['contact_number'],
                project_objective=form.cleaned_data['project_objective'],
                past_research=form.cleaned_data['past_research'],
                personal_statement=form.cleaned_data['personal_statement'],
                cv=form.cleaned_data['cv'],
                acceptance_letter=form.cleaned_data['acceptance_letter']
            )
            application.save()
            
            # Handle multiple file uploads for supporting documents
            supporting_documents = request.FILES.getlist('supporting_documents')
            for document in supporting_documents:
                SupportingDocument.objects.create(
                    application=application,
                    file=document
                )

            # Send an email notification
            send_mail(
                'Summer Research Application Received',
                f"Dear {application.name},\n\nYour application for the Summer Research Program has been received. Your application ID is {application.id}. We will review your application and get back to you soon.\n\nBest regards,\nAlumni Relations Division",
                settings.DEFAULT_FROM_EMAIL,
                [application.email],
                fail_silently=False,
            )
            
            return redirect('summer_research_application_success')
    else:
        form = ApplicationForm()
    
    return render(request, 'scholarship_form.html', {'form': form})

def summer_research_application_success(request):
    return render(request, 'scholarship_success.html')
