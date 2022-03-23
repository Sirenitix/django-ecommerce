import django
from django import template
from core.models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        if django.utils.translation.get_language() == 'en':
             qs = Order.objects.using('default').filter(user=user, ordered=False)
             if qs.exists():
                 return qs[0].items.count()
        elif django.utils.translation.get_language() == 'ru':
             qs = Order.objects.using('users').filter(user=user, ordered=False)
             if qs.exists():
                 return qs[0].items.count()
        else:
             qs = Order.objects.using('some').filter(user=user, ordered=False)
             if qs.exists():
                 return qs[0].items.count()
    return 0
