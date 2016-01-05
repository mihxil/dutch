#!/usr/bin/env python3
from dutch import Dutch
import sys
import unicodedata

s = Dutch.number(sys.argv[1])
if sys.stdout.encoding in (None, "US-ASCII"):
    nfkd_form = unicodedata.normalize('NFKD', s)
    s =  u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

print(s)
