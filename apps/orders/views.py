from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from apps.orders.models import Order
from apps.orders.forms import OrderForm


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'index.html'
    success_url = reverse_lazy('general_page')
