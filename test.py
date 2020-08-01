#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plain_db
# counter = plain_db.load('counter')
# counter.update('abc', 2)
# counter.inc('abc', 1)
# print(counter.get('abc')) # 3
# print(counter.get('ab')) # None

# existing = plain_db.loadKeyOnlyDB('existing')
# print(existing.items())
# print(existing.add('1'))
# print(existing.add('1'))
# print(existing.add('2'))
# existing.remove('3')
# print(existing.items())

# f = plain_db.loadLargeDB('index1', isIntValue=True, default=5)
# print(f.items())
# f.update('1', 5)
# f.update('4', 1)
# f.update('3', 9)
# print(f.items())
# print(f.get('6'))
# plain_db.cleanupLargeDB('index1')
# f.save_dont_call_in_prod()

rating = plain_db.loadLargeDB('rating', isIntValue = True, default = 0)
rating.update('1', 0)
rating.update('2', 1)