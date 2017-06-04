# -*- coding: utf-8 -*-

"""
Задание 13.3

Создайте шаблон templates/ospf.txt на основе конфигурации OSPF в файле cisco_ospf.txt.
Пример конфигурации дан, чтобы напомнить синтаксис.

Какие значения должны быть переменными:
* номер процесса. Имя переменной - process
* router-id. Имя переменной - router_id
* reference-bandwidth. Имя переменной - ref_bw
* интерфейсы, на которых нужно включить OSPF. Имя переменной - ospf_intf
 * на месте этой переменной ожидается список словарей с такими ключами:
  * name - имя интерфейса, вида Fa0/1, VLan10, Gi0/0
  * ip - IP-адрес интерфейса, вида 10.0.1.1
  * area - номер зоны
  * passive - является ли интерфейс пассивным. Допустимые значения: True или False

Для всех интерфейсов в списке ospf_intf, надо сгенерировать строки:
 network x.x.x.x 0.0.0.0 area x

Если интерфейс пассивный, для него должна быть добавлена строка:
 passive-interface x

Для интерфейсов, которые не являются пассивными, в режиме конфигурации интерфейса,
надо добавить строку:
 ip ospf hello-interval 1


Все команды должны быть в соответствующих режимах.

Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf.yml,
с помощью функции generate_cfg_from_template из задания 13.1-13.1d.
Не копируйте код функции.


"""

import sys
from task_13_1d import generate_cfg_from_template
template_path = sys.argv[1]
data = sys.argv[2]


print(generate_cfg_from_template(template_path, data, trim_blocks=True, lstrip_blocks=True))