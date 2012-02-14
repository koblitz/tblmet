#-*- coding: utf-8 -*-
import csv
from grmetodos.models import *
import settings
a=TblUnidades.objects.all()
nome=[i.nome for i in a]
of = open('test1.csv', 'w')
w=csv.writer(of, delimiter = '\t', quotechar='"', quoting=csv.QUOTE_NONE)
for r in nome:
 w.writerow(r)

of.close()