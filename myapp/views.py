from django.shortcuts import render
from myapp.forms import BookingForm


# Create your views here.
def bookings(request):
    form = BookingForm()
    print(request.method)
    print(form.is_valid())
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'booking.html', {'form': form})
