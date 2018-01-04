from validate.utils import id_card, enum, url, email, equal_to, min_value, max_value, range_value, min_length, \
    max_length, range_length, pattern, custom, ipv4, ipv6, date

__all__ = ['default_msg',
           'validate']

default_msg = {
    'required': '字段必填.',
    'enum': '字段必须在给定的范围内.',
    'type': '字段类型不正确.',
    'email': '字段不符合电子邮件格式.',
    'url': '字段不是合法的url.',
    'equal_to': '字段两次输入的值不相等.',
    'min': '字段的值太小.',
    'max': '字段的值太大.',
    'range': '字段的值不在范围内.',
    'min_length': '字段太短.',
    'max_length': '字段太长.',
    'range_length': '字段的长度不在范围内.',
    'pattern:': '字段符合正则表达式.',
    'custom': '字段验证不通过.',
    'id_card': '字段不是合法的身份证号.',
    'ipv4': '字段不是一个合法的ip4地址.',
    'ipv6': '字段不是一个合法的ip6地址.',
    'date': '字段不是一个合法的时间格式.'
}


class ERRMSG(dict):
    """
    获取错误提示
    查找顺序:
    1.自定义每个属性的提示
    2.字段默认提示（_default）
    3.全局默认提示
    """

    def __init__(self, msg, **kwargs):
        super().__init__(**kwargs)
        self.msg = msg

    def __getitem__(self, item):
        field, attr = item.split('.')
        if field in self.msg:
            field = self.msg[field]
            if attr in field:
                return field[attr]
            else:
                if '_default' in field:
                    return field['_default']
                else:
                    pass
        else:
            pass

        try:
            return default_msg[attr]
        except KeyError:
            raise Exception('没有设置默认提示.')


def validate(rules, obj):
    """
    验证函数
    :param rules:验证规则
    :param obj:验证对象
    :param args:错误提示
    :return:
    """
    validate_all = False
    if 'all_validate' in rules and rules['all_validate'] is True:
        validate_all = True
    if 'fields' not in rules or type(rules['fields']) != dict:
        raise Exception('字段参数异常')
    fields = rules['fields']

    if 'msg' in rules:
        errmsg = ERRMSG(rules['msg'])
    else:
        errmsg = ERRMSG({})

    error_list = []
    pass_list = []
    valid_list = list(fields.keys())

    while len(valid_list) != 0:
        if validate_all is False and len(error_list) > 0:
            return True if error_list.__len__() == 0 else False, error_list, pass_list

        field = valid_list[0]
        result, attr = __val_field(field, fields[field], obj)
        if result:
            pass_list.append(field)
        else:
            error_list.append((field, errmsg['.'.join([field, attr])]))
        del valid_list[0]

    return True if error_list.__len__() == 0 else False, error_list, pass_list


def __val_field(field, rule, obj):
    """
    验证每个字段
    :param field:字段名
    :param rule:验证规则
    :param obj:待验证对象
    :return:
    """
    if 'required' in rule:
        if rule['required'] and field not in obj:
            return False, 'required'

    try:
        value = obj[field]
    except KeyError:
        return False, 'required'

    if 'enum' in rule:
        if enum(value, rule['enum']) is False:
            return False, 'enum'

    if 'type' in rule:
        if rule['type'] != type(value) is False:
            return False, 'type'

    if 'email' in rule and rule['email'] is True:
        if email(value) is False:
            return False, 'email'

    if 'url' in rule and rule['url'] is True:
        if url(value) is False:
            return False, 'url'

    if 'equal_to' in rule:
        if equal_to(obj[rule['equal_to']], value) is False:
            return 'equal_to'

    if 'min' in rule:
        if min_value(value, rule['min']) is False:
            return False, 'min'

    if 'max' in rule:
        if max_value(value, rule['max']) is False:
            return False, 'max'

    if 'range' in rule:
        if range_value(value, rule['range']) is False:
            return False, 'range'

    # 只有字符串才能验证长度，其他数据类型不能,汉字算一个字符
    if 'min_length' in rule:
        if min_length(value, rule['min_length']) is False:
            return False, 'min_length'

    if 'max_length' in rule:
        if max_length(value, rule['min_length']) is False:
            return False, 'max_length'

    if 'range_length' in rule:
        if range_length(value, rule['range_length']) is False:
            return False, 'range_length'

    if 'pattern' in rule:
        if pattern(rule['pattern'], value) is None:
            return False, 'pattern'

    if 'custom' in rule:
        if custom(field, value, rule['custom']) is False:
            return False, 'custom'

    if 'id_card' in rule and rule['id_card'] is True:
        if id_card(obj['field']) is False:
            return False, 'id_card'

    if 'ipv4' in rule and rule['ipv4']:
        if not ipv4(value):
            return False, 'ipv4'

    if 'ipv6' in rule and rule['ipv6']:
        if not ipv6(value):
            return False, 'ipv6'

    if 'date' in rule:
        date_rule = rule['date']
        if not date(value, date_rule):
            return False, 'date'

    return True, field


if __name__ == '__main__':
    print(id_card('5555555'))
    print(id_card('522130931006201'))
    print(id_card('522130199310062011'))
    print(ipv4('192.168.168.1'))
    print(ipv6('fe80::356c:4a6f:64f4:c88e'))
