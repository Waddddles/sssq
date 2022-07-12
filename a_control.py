import sys
import os
from cq_slj import cq_slj
from sc_dzxsksq import sc_dzxsksq
from sc_hdsq import sc_hdsq
from cj_sww_sssq import cj_sww_sssq
from cjsy_sww_sssq import cjsy_sww_sssq

try:
    cq_slj()
    print("重庆水利局-finished!")
except:
    print("重庆水利局-error!(.py is obsolete)")

try:
    sc_dzxsksq()
    print("四川大中型水库水情-finished!")
except:
    print("四川大中型水库水情-error!(.py is obsolete)")

try:
    sc_hdsq()
    print("四川河道水情-finished!")
except:
    print("四川河道水情-error!(.py is obsolete)")

try:
    cj_sww_sssq()
    print("长江水文网实时水情-finished!")
except:
    print("长江水文网实时水情-error!(.py is obsolete)")

try:
    cjsy_sww_sssq()
    print("长江上游水文网实时水情-finished!")
except:
    print("长江上游水文网实时水情-error!(.py is obsolete)")
