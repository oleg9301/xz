# -*- coding: utf-8 -*-

"""
Задание 11.4

Обновить файл get_data из задания 11.2 или 11.2a.
Добавить поддержку столбца active, который мы добавили в задании 11.3.

Теперь, при запросе информации, сначала должны отображаться активные записи,
а затем, неактивные.

Например:
```
$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
----------------------------------------

=======================================
Inactive values:
----------------------------------------
mac         : 00:09:23:34:16:18
vlan        : 10
interface   : FastEthernet0/4
----------------------------------------
```
"""
