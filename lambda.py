#!/usr/bin/env python -u

from datetime import datetime as dt
from datetime import timedelta as tdel
from pprint import pprint as pp

butler_event_time = {
    '2345': dt.now() - tdel(minutes=45),
    '3456': dt.now() - tdel(hours=1, minutes=30),
    '4567': dt.now() - tdel(minutes=60),
    '5678': dt.now() - tdel(minutes=15)
}

if __name__ == '__main__':
    # lambda body can contain 'expressions' only not 'statements'
    sorted_butler_event_time = sorted(butler_event_time.items(), key=lambda kv: kv[1])
    d = {k: v for k,v in sorted_butler_event_time}
    pp(d, sort_dicts=False)

