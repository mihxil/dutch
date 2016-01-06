#!/usr/bin/env python3
from dutch import Dutch
from english import English
import sys
import unicodedata

for F in (Dutch, English):
    s = F.number(sys.argv[1])
    if sys.stdout.encoding in (None, "US-ASCII"):
        nfkd_form = unicodedata.normalize('NFKD', s)
        s =  u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
    print(s)
