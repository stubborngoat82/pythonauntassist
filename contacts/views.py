from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ExternalContact, UserContact
from .forms import ExternalContactForm, UserContactForm

# ExternalContact Views
@login_required
def external_contact_list(request):
    contacts = ExternalContact.objects.filter(user=request.user)
    return render(request, 'contacts/external_contact_list.html', {'contacts': contacts})

@login_required
def external_contact_create(request):
    if request.method == 'POST':
        form = ExternalContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('external_contact_list')
    else:
        form = ExternalContactForm()
    return render(request, 'contacts/external_contact_form.html', {'form': form})

@login_required
def external_contact_update(request, pk):
    contact = get_object_or_404(ExternalContact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExternalContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('external_contact_list')
    else:
        form = ExternalContactForm(instance=contact)
    return render(request, 'contacts/external_contact_form.html', {'form': form})

@login_required
def external_contact_delete(request, pk):
    contact = get_object_or_404(ExternalContact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('external_contact_list')
    return render(request, 'contacts/external_contact_confirm_delete.html', {'contact': contact})

# UserContact Views
@login_required
def user_contact_list(request):
    contacts = UserContact.objects.filter(user=request.user)
    return render(request, 'contacts/user_contact_list.html', {'contacts': contacts})

@login_required
def user_contact_create(request):
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('user_contact_list')
    else:
        form = UserContactForm()
    return render(request, 'contacts/user_contact_form.html', {'form': form})
