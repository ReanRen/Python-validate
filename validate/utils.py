# coding=utf8

import re

try:
    from id_card import id_card
    from vdate import date
except ImportError:
    from .id_card import id_card
    from .vdate import date

__all__ = [
    'id_card',
    'date',
    'email',
    'enum',
    'url',
    'equal_to',
    'min_value',
    'max_value',
    'range_value',
    'min_length',
    'max_length',
    'range_length',
    'pattern',
    'custom',
    'ipv4',
    'ipv6',
    'tel',
    'post_code'
]


def email(val):
    """
    验证电子邮件
    :param val:电子邮件地址
    :return:
    """
    return pattern(val, '^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]+$')


def enum(val, coll):
    """
    验证枚举类型
    :param val:
    :param coll:
    :return:
    """
    return val in coll


def url(val):
    """
    验证URL
    :param val:
    :return:
    """
    return pattern(val, '(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')


def equal_to(left, right):
    """
    验证两个字段是否相等
    :param left:
    :param rigth:
    :return:
    """
    return left == right


def min_value(val, limit):
    """
    验证是否小于最小值，先转换为数值比较，如果转换不成功，则转换为字符串比较
    :param val:
    :return:
    """
    try:
        a, b = int(val), int(limit)
    except ValueError:
        a, b = str(val), str(limit)
    return a > b


def max_value(val, limit):
    """
    验证是否大于最大值，先转换为数值比较，如果转换不成功，则转换为字符串比较
    :param val:
    :param limit:
    :return:
    """
    try:
        a, b = int(val), int(limit)
    except ValueError:
        a, b = str(val), str(limit)
    return a < b


def range_value(val, limit):
    """
    验证给定值是否在范围内,先转换为数值比较，如果转换不成功，则转换为字符串比较
    :param val:
    :param limit:
    :return:
    """
    if (isinstance(limit, tuple) or isinstance(limit, list)) and len(limit) == 2:
        try:
            a, b, c = int(limit[0]), int(val), int(limit[1])
        except ValueError:
            a, b, c = str(limit[0]), str(val), str(limit[1])

        return a <= b <= c

    return False


def min_length(val, limit):
    """
    验证长度是否小于给定值
    :param val:
    :param length:
    :return:
    """
    return str(val).__len__() >= limit


def max_length(val, limit):
    """
    验证长度是否大于给定值
    :param val:
    :param limit:
    :return:
    """
    return str(val).__len__() <= limit


def range_length(val, limit):
    """
    验证长度是否在范围内
    :param val:
    :param limit:
    :return:
    """
    if (isinstance(limit, tuple) or isinstance(limit, list)) and len(limit) == 2:
        return limit[0] <= len(str(val)) <= limit[1]

    return False


def pattern(val, limit):
    """
    正则验证值是否在范围内
    :param val:
    :param limit:
    :return:
    """
    result = re.match(limit, val)
    return True if result is not None else False


def custom(field, val, limit):
    """
    使用自定义函数验证
    :param field: 字段名
    :param val:值
    :param limit: 自定义函数
    :return:
    """
    if callable(limit) is True:
        return limit(field, val)
    return False


def tel(val):
    """
    验证中国手机号,+86格式的不验证，指验证11为手机号:
    :param val:要验证的电话号码
    :return:
    """
    return pattern(str(val), '^1[34578]\d{9}$')


def post_code(val):
    """
    验证中国邮政编码
    :param val:
    :return:
    """
    return pattern(str(val), '^[1-9]\d{5}$')


def ipv4(val):
    """
    验证IPV4
    :param val:
    :return:
    """
    return pattern(val,
                   '^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$')


def ipv6(val):
    """
    验证IPV6
    :param val:
    :return:
    """
    return pattern(val,
                   '^((([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}:[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){5}:([0-9A-Fa-f]{1,4}:)?[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){4}:([0-9A-Fa-f]{1,4}:){0,2}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){3}:([0-9A-Fa-f]{1,4}:){0,3}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){2}:([0-9A-Fa-f]{1,4}:){0,4}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){6}((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|(([0-9A-Fa-f]{1,4}:){0,5}:((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|(::([0-9A-Fa-f]{1,4}:){0,5}((\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b)\.){3}(\b((25[0-5])|(1\d{2})|(2[0-4]\d)|(\d{1,2}))\b))|([0-9A-Fa-f]{1,4}::([0-9A-Fa-f]{1,4}:){0,5}[0-9A-Fa-f]{1,4})|(::([0-9A-Fa-f]{1,4}:){0,6}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){1,7}:))$')


id_card('522130199310062011')
if __name__ == '__main__':
    print(id_card('522130199310062011'))
    print(email('674038364@qq.com'))
    print(range_value(2, [1, 3]))
    print(min_length(22, 1))
    print(ipv4('192.168.168.1'))
    print(ipv6('fe80::356c:4a6f:64f4:c88e'))
