# OrderedDict => Maintains insertion order (mostly unnecessary in Python 3.7+ since dict already does this).

from collections import OrderedDict

od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
print(od)