#!/usr/bin/env python3
from dutch import Dutch
from english import English
from esperanto import Esperanto
import sys
import unicodedata

for F in (Dutch, English, Esperanto):
    s = F().number(sys.argv[1])
    if sys.stdout.encoding in (None, "US-ASCII"):
        nfkd = unicodedata.normalize('NFKD', s)
        s = "".join([c for c in nfkd if not unicodedata.combining(c)])
    print(s)
