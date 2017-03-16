# -*- coding: utf-8 -*-
from retrying import retry

@retry(stop_max_attempt_number=10,wait_fixed=5000)
def retry():
    print('test')
    raise ''


retry()