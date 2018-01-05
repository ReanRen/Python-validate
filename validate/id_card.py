# coding=utf8

import time
import re

__all__ = ['id_card']


def id_card(val):
    """
    1.验证长度
    2.验证省份
    3.验证年龄
    5.验证校验位
    :param val:
    :return:
    """
    return check_length(val) and check_province(val) and check_birthday(val) and check_last(val)


def check_length(val):
    return True if re.match('(^\d{15}$)|(^\d{17}(\d|X)$)', val) is not None else False


def check_province(val):
    """
    验证身份证的省份
    :param val:
    :return:
    """
    city = {
        '11': '北京',
        '12': '天津',
        '13': '河北',
        '14': '山西',
        '15': '内蒙古',
        '21': '辽宁',
        '22': '吉林',
        '23': '黑龙江',
        '31': '上海',
        '32': '江苏',
        '33': '浙江',
        '34': '安徽',
        '35': '福建',
        '36': '江西',
        '37': '山东',
        '41': '河南',
        '42': '湖北',
        '43': '湖南',
        '44': '广东',
        '45': '广西',
        '46': '海南',
        '50': '重庆',
        '51': '四川',
        '52': '贵州',
        '53': '云南',
        '54': '西藏',
        '61': '陕西',
        '62': '甘肃',
        '63': '青海',
        '64': '宁夏',
        '65': '新疆',
        '71': '台湾',
        '81': '香港',
        '82': '澳门',
        '91': '国外'
    }
    return val[0:2] in city


def verify_birthday(year):
    """
    验证身份证的年龄正不正确
    :param year:
    :return:
    """
    t = time.localtime()
    now_year = t.tm_year
    age = now_year - int(year)
    return 0 <= age < 130


def check_birthday(val):
    """
    验证生日是否
    :param val:
    :return:
    """
    length = len(val)
    if length == 15:
        # 身份证15位时，次序为省（3位）市（3位）年（2位）月（2位）日（2位）校验位（3位），皆为数字
        year = '19' + val[6:8]
        return verify_birthday(year)
    if length == 18:
        # 身份证18位时，次序为省（3位）市（3位）年（4位）月（2 位）日（2位）校验位（4位），校验位末尾可能为X
        return verify_birthday(val[6:10])
    return False


def check_last(val):
    """
    验证最后一个校验位
    :param val:
    :return:
    """
    if len(val) == 15:
        val = fifteen_to_eighteen(val)
    arr_int = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    arr_ch = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    card_temp = 0
    for i in range(0, 17):
        card_temp += int(val[i]) * arr_int[i]
    val_num = arr_ch[card_temp % 11]
    return val[17] == val_num


def fifteen_to_eighteen(val):
    """
    将15位身份证转为18位身份证
    :param val:
    :return:
    """
    if len(val) == 15:
        arr_int = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        arr_ch = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        card_temp = 0
        val = val[0:6] + '19' + val[6:]
        for i in range(0, 17):
            card_temp += int(val[i]) * arr_int[i]
        val += arr_ch[card_temp % 11]
    return val


if __name__ == '__main__':
    print(id_card('5555555'))
    print(id_card('522130931006201'))
    print(id_card('522130199310062011'))
