#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plain_db

print(plain_db.get('https://www.bbc.com/zhongwen/simp'))
print(plain_db.get('https://img9.doubanio.com/view/status/l/public/64f0c054cbc6f3d.jpg', mode='b'))