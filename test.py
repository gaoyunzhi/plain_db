#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plain_db
counter = plain_db.load('counter')
# counter.update('abc', 2)
# counter.inc('abc', 1)
print(counter.get('abc')) # 3
