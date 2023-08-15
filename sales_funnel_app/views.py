from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Lead
from django.shortcuts import redirect
from .forms import LeadCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Lead

def home(request):
    return render(request, 'sales_funnel_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('lead_list')  # Redirect to lead list page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

@login_required
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'sales_funnel_app/lead_list.html', {'leads': leads})

def create_lead(request):
    if request.method == 'POST':
        form = LeadCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')  # Redirect to the lead list page
    else:
        form = LeadCreationForm()
    return render(request, 'sales_funnel_app/create_lead.html', {'form': form})

def update_lead_status(request, lead_id):
    lead = Lead.objects.get(pk=lead_id)
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        lead.status = new_status
        lead.save()
        return redirect('lead_list')  # Redirect to the lead list page
    return render(request, 'sales_funnel_app/update_lead_status.html', {'lead': lead})

def lead_detail(request, lead_id):
    lead = get_object_or_404(Lead, pk=lead_id)
    return render(request, 'sales_funnel_app/lead_detail.html', {'lead': lead})

def delete_lead(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    if request.method == 'POST':
        lead.delete()
        return redirect('lead_list')
    return render(request, 'sales_funnel_app/delete_lead.html', {'lead': lead})

def default_redirect(request):
    return redirect('lead_list')
