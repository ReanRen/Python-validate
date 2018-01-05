# coding=utf8

import time

__all__ = ['date']


def date(val, rule):
    """
    验证日期,格式验证，大小验证,大小验证和范围验证转换为时间戳验证
    :param val:
    :param rule:
    :return:
    """
    err = '时间格式不正确.'

    if 'format' not in rule:
        raise Exception('没有设置时间验证的格式.')
    try:
        fat = rule['format']
        time_str = time.strptime(val, fat)
    except ValueError:
        return False

    day = time.mktime(time.strptime(time.strftime(fat), fat))  # 根据格式格式化当前时间
    val = time.mktime(time_str)
    if 'min' in rule:
        if rule['min'] != 1:
            try:
                day = time.mktime(time.strptime(rule['min'], fat))
            except ValueError:
                raise Exception(err)
        if val < day:
            return False

    if 'max' in rule:
        if rule['max'] != 1:
            try:
                day = time.mktime(time.strptime(rule['max'], fat))
            except ValueError:
                raise Exception(err)
        if val > day:
            return False

    if 'range' in rule:
        limit = rule['range']
        try:
            a, c = time.mktime(time.strptime(limit[0], fat)), time.mktime(time.strptime(limit[1], fat))
            if a > val or c < val:
                return False
        except ValueError:
            raise ValueError(err)

    return True


if __name__ == '__main__':
    birth = {
        'format': '%Y-%m-%d',
        'min': 1,  # 1，最小值是当前时间，其他字符串
        'max': '2018-01-31',  # 1，最大值是当前时间，其他字符串
        'range': ['2018-01-01', '2018-01-31']
    }
    print(date('2018-01-04', birth))
