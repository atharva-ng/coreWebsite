from django import forms

class ApplicationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}))
    id_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}))
    contact_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}))
    project_objective = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}))
    past_research = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}))
    personal_statement = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'}))
    
    # Changed cv and acceptance_letter to allow single file uploads
    cv = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
    }))
    
    acceptance_letter = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
    }))

    # For multiple file uploads
    supporting_documents = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'multiple': True,
            'class': 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
        })
    )
