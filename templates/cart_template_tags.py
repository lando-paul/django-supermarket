from django import template
from catalog.models import order

register = template.Library()
@register.filter
def cart_item_count(user):
  if user. is authentificated:
    qs = order.objects.filter(user=user, ordered= false)
    if qs.exists():
      order = qs[0]
      return order.items.count()
  return 0
