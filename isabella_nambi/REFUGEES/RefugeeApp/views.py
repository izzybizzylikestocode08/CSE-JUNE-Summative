from django.shortcuts import render
from .forms import BeneficiaryForm

def landing_page(request):
    return render(request, 'RefugeeApp/landing_page.html')
def beneficiary_registration(request):
    success = False
    if request.method == 'POST':
        form = BeneficiaryForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = BeneficiaryForm() 
    else:
        form = BeneficiaryForm()
    return render(request, 'RefugeeApp/beneficiary_registration.html', {'form': form, 'success': success})
