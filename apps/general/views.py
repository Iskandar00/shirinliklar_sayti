from django.views.generic import TemplateView
from apps.about.models import About, CustomerOpinion
from apps.categories.models import Category
from apps.general.models import General
from apps.products.models import Product, AdditionalAdvertising


class GeneralTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.filter(ordering_number__in=[1, 2, 3, 4]).select_related()
        products_by_category = {
            1: Product.objects.filter(category__ordering_number=1).select_related('category'),
            2: Product.objects.filter(category__ordering_number=2).select_related('category'),
            3: Product.objects.filter(category__ordering_number=3).select_related('category'),
            4: Product.objects.filter(category__ordering_number=4).select_related('category')
        }

        for category in categories:
            context[f'categories_{category.ordering_number}'] = category
            context[f'categories_{category.ordering_number}_products'] = products_by_category[category.ordering_number]

        context['general'] = General.objects.first()
        context['additional_advertisings'] = AdditionalAdvertising.objects.all()

        abouts = About.objects.filter(ordering_number__in=[1, 2, 3, 4])
        for about in abouts:
            context[f'about_{about.ordering_number}'] = about

        context['all_products'] = Product.objects.all()
        context['customer_opinions'] = CustomerOpinion.objects.all()

        return context
