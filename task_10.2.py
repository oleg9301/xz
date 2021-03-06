# -*- coding: utf-8 -*-
'''
Задание 2

Создать функции:
- generate_access_config - генерирует конфигурацию для access-портов,
                           на основе словарей access и psecurity из файла sw_templates.yaml
- generate_trunk_config - генерирует конфигурацию для trunk-портов,
                           на основе словаря trunk из файла sw_templates.yaml
- generate_ospf_config - генерирует конфигурацию ospf, на основе словаря ospf из файла templates.yaml
- generate_mngmt_config - генерирует конфигурацию менеджмент настроек, на основе словаря mngmt из файла templates.yaml
- generate_alias_config - генерирует конфигурацию alias, на основе словаря alias из файла templates.yaml
- generate_switch_config - генерирует конфигурацию коммутатора, в зависимости от переданных параметров,
                           использует для этого остальные функции
'''

import yaml
access_dict = {'FastEthernet0/12': 10,
                'FastEthernet0/14': 11,
                'FastEthernet0/16': 17,
                'FastEthernet0/17': 150}

trunk_dict = { 'FastEthernet0/1': [10,20,30],
               'FastEthernet0/2': [11,30],
               'FastEthernet0/4': [17]}


sw_config = []


def generate_access_config(access, psecurity=False):
    for interface, vlan in access.items():
        sw_config.append('interface ' + interface)
        with open('sw_templates.yaml', 'r') as f:
            for string in yaml.load(f)['access']:
                if 'access vlan' in string:
                    sw_config.append(string + ' ' + str(vlan))
                else:
                    sw_config.append(string)
        with open('sw_templates.yaml', 'r') as f:
            if psecurity:
                for string in yaml.load(f)['psecurity']:
                    sw_config.append(string)
    return sw_config


def generate_trunk_config(trunk):
    for interface, vlan in trunk.items():
        sw_config.append('interface ' + interface)
        with open('sw_templates.yaml', 'r') as f:
            for string in yaml.load(f)['trunk']:
                if 'allowed vlan' in string:
                    sw_config.append(string + ' ' + ','.join(str(num) for num in vlan))
                else:
                    sw_config.append(string)
    return sw_config


def generate_ospf_config(filename):
    with open(filename, 'r') as f:
        for string in (yaml.load(f)['ospf']):
            sw_config.append(string)
    return sw_config


def generate_mngmt_config(filename):
    with open(filename, 'r') as f:
        for string in (yaml.load(f)['mngmt']):
            sw_config.append(string)
    return sw_config


def generate_alias_config(filename):
    with open(filename, 'r') as f:
        for string in (yaml.load(f)['alias']):
            sw_config.append(string)
    return sw_config


def generate_switch_config(access=True, psecurity=False, trunk=True,
                           ospf=True, mngmt=True, alias=False):
    if access and psecurity:
        generate_access_config(access_dict,  psecurity=True)
    if access:
        generate_access_config(access_dict)
    if trunk:
        generate_trunk_config(trunk_dict)
    if ospf:
        generate_ospf_config('templates.yaml')
    if mngmt:
        generate_mngmt_config('templates.yaml')
    if alias:
        generate_alias_config('templates.yaml')
    return '\n'.join(sw_config)


sw1 = generate_switch_config()
sw2 = generate_switch_config(psecurity=True, alias=True)
sw3 = generate_switch_config(ospf=False)

