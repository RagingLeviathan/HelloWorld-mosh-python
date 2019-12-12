# first way... too verbose
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
# second way... better
# from ecommerce.shipping import calc_shipping
# calc_shipping()
# third way... the best...
from ecommerce import shipping

shipping.calc_shipping()