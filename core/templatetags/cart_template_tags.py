import django
from django import template
from core.models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        if django.utils.translation.get_language() == 'eu':
            qs = Order.objects.using('default').filter(user=user, ordered=False)
        else:
            if django.utils.translation.get_language() == 'ru':
                qs = Order.objects.using('users').filter(user=user, ordered=False)
            else:
                qs = Order.objects.using('some').filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
