# coding=utf8

from validate import check


def custom(filed, value):
    """
    自定义验证函数
    :param filed:字段名
    :param value:字段值
    :return:
    """
    if filed == 'ipaddr':
        return check.pattern(value, '^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$')


if __name__ == '__main__':
    # 覆盖默认提示
    check.default_msg['required'] = u'字段必填'
    # 提示查找顺序
    # 1.自定义每个属性的提示
    # 2.字段默认提示（_default）
    # 3.全局默认提示

    rule = {
        'all_validate': True,  # 全部验证在返回，否则只要有错就返回
        'fields': {
            'name': {
                'required': True,
                'enum': ['rean', 'huen'],
                'type': str,
            },
            'email': {
                'required': True,
                'email': True
            },
            'home_page': {
                'url': True
            },

            'password': {
                'range_length': [16, 20]
            },
            'confirm_password': {
                'equal_to': 'password',  # password 字段一样
            },
            'age': {
                'min': 0,
                'max': 130
            },
            'score': {
                'range': [0, 100]
            },
            'address': {
                'min_length': 4,
                'max_length': 40,
                'range_length': (4, 40)
            },
            'ipaddr': {
                'custom': custom  # 自定义函数验证
            },
            'phone_number': {
                'tel': True
            },
            'post_code': {
                'post_code': True
            },
            'birth': {
                'date': {
                    'format': '%Y-%m-%d',
                    'min': 1,  # 1，最小值是当前时间，其他字符串
                    'max': '2018-01-31',  # 1，最大值是当前时间，其他字符串
                    'range': ['2018-01-01', '2018-01-31']
                }
            }
        },
        'msg': {
            'name': {
                # 默认消息提示，如果找不到下一级的消息提示则提示该消息
                '_default': u'默认消息提示',
                # 覆盖默认提示
                'enum': u'姓名必须在huen和rean中'
            },
            'confirm_password': {
                'equal_to': u'两次输入的密码不一样。'
            },
            'birth': {
                'date': u'生日输入不正确.'
            }
        }
    }

    value = {
        'name': 'rean',
        'email': 'rean.ren@qq.com',
        'password': '1234567890123456',
        'home_page': 'http://baidu.com',
        'confirm_password': '1234567890123456',
        'age': 30,
        'score': 90,
        'address': '花22dasdsadsadsadasdsad道',
        'ipaddr': '255.255.255.255',
        'phone_number': '13984927617',
        'post_code': '564500',
        'birth': '2018-01-43'
    }
    print(check.validate(rule, value))
    print(check.id_card('52130199310062011'))

    # (False, [('address', '字段太长.'), ('birth', '生日输入不正确.')], ['name', 'email', 'home_page', 'password', 'confirm_password', 'age', 'score', 'ipaddr', 'phone_number', 'post_code'])
    # False
