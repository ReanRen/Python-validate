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
    check.default_msg['required'] = '字段必填'
    msg = {
        'name': {
            # 默认消息提示，如果找不到下一级的消息提示则提示该消息
            '_default': '默认消息提示',

            # 覆盖默认提示
            'enum': '姓名必须在huen和rean中'
        },
        'confirm_password': {
            'equal_to': '两次输入的密码不一样。'
        }
    }
    # 消息查找顺序
    # 1.自定义每个属性的消息
    # 2.字段默认消息（_default）
    # 3.全局默认消息

    rule = {
        'all_validate': True,  # 全部验证在返回，否则只要有错就返回
        'fields': {
            'name': {
                'required': True,
                'enum': ['rean', 'huen'],
                'type': str,
                'range': [1, 100],
                'range_length': [2, 10],
            },
            'password': {
                'email': True,
                'range_length': [16, 20]
            },
            'confirm_password': {
                'equal_to': 'password',
                'message': '两次的密码不一样'
            },
            'home_page': {
                'url': True
            },
            'score': {
                'range': [200, 2000]
            },
            'address': {
                'min_length': 4,
                'max_length': 10
            },
            'address1': {
                'range_length': [2, 10]
            },
            'ipaddr': {
                'custom': custom
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
                '_default': '默认消息提示',

                # 覆盖默认提示
                'enum': '姓名必须在huen和rean中'
            },
            'confirm_password': {
                'equal_to': '两次输入的密码不一样。'
            },
            'birth': {
                'date': '生日输入不正确.'
            }
        }
    }

    obj = {
        'name': 'rean',
        'password': '674038364@qq.com',
        'home_page': 'http://baidu.com',
        'confirm_password': '674038364@qq.com',
        'score': 200,
        'address': '花22dasdsadsadsadasdsad道',
        'address1': '22',
        'ipaddr': '255.255.255.255',
        'birth': '2018-01-43'
    }
    print(check.validate(rule, obj))
    print(check.id_card('52130199310062011'))
