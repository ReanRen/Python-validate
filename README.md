# Python-Validate
python表单验证,类似于jQuery validation前端验证，其中ipv4和ipv6的验证参考了jQuery validation中的验证。通常用于后台开发验证前端的数据。目前支持 `python3`,`python2可以正常使用，但是返回的提示是unicode编码.`

# 1. 安装

## 1.1 通过 pip 安装
```sh
pip3 install python-validate
```


## 1.2 通过whl安装
下载地址： 
[python_validate-0.0.2.dev0-py2.py3-none-any.whl](https://pypi.python.org/packages/c9/5a/0163dfbd42bda5af13159d3b1c1d865faf0b41359eea06962e3523cfa039/python_validate-0.0.2.dev0-py2.py3-none-any.whl)

# 2.使用
```python
from validate import check

# 验证身份证号码
check.id_card('522130199310062011')
# True

check.id_card('522130199310062012')
# False

check.ipv4('192.168.1.1')
# True
```

# 2.1.常用方法列表：
```
check.id_card           #字符串，验证是否是中国公民身份证号码,check.id_card('522130199310062012') # False
check.enum              #第一个是任何类型a，第二个是集合b，验证a是否在b中，check.enum('1',[1,2,3]) #False
check.url               #字符串，验证是否是合法的url,check.url('http://wwwbaidu.com') #True
check.email             #字符串，验证电子邮件地址，check.email('rean.ren@qq.com') #True
check.equal_to          #比较两个参数是否相等，check.equal_to('a','b') #False

check.min_value         #验证a是否小于最小值b，先转换为数值比较，如果转换不成功，则转换为字符串比较,check.min_value(1,3) #False
chech.max_value         #验证a是否大于最大值b,先转换为数值比较，如果转换不成功，则转换为字符串比较,check.max_value(1,3) #True
check.range_value       #验证a是否在范围b内（元组或者数组）,先转换为数值比较，如果转换不成功，则转换为字符串比较,check.rang_value(2,[1,3]) #True

check.min_length        #验证a的长度是否小于给定值b,check.min_length('22',1) #True
check.max_length        #验证a的长度是否大于给定值b,check.max_length('22',1) #False
check.range_length      #验证a的长度是否在范围b内（元组或者数组）,check.range_length('22',(1,3)) #True

check.pattern           #验证b是否符合正则表达式a,check.pattern('www','www.baidu.com') #False
check.ipv4              #验证ipv4地址，check.ipv4('192.168.1.1') #True
check.ipv6              #验证ipv6地址，check.ipv6('2001:0:9d38:953c:2486:2115:3f57:5f07')
check.tel               #验证11位中国电话号码
check.post_code         #验证6位中国邮编
```

# 2.2 时间格式验证
```
check.date              #验证时间格式，第一个参数a为要验证的字符串，第二个为要验证规则，举例如下：
a='2018-01-04'
birth = {
        'format': '%Y-%m-%d', 
        'min': 1,  # 1，最小值是当前时间，其他字符串
        'max': '2018-01-31',  # 1，最大值是当前时间，其他字符串
        'range': ['2018-01-01', '2018-01-31']
}
check.date(a,birth) #False min没有通过
```

* format 为时间格式，如下：
```
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
```
* min 时间的最小值，如果是1则代表当前时间
* max 时间最大值，如果是1则代表当前时间
* range 时间最小值最大值的范围
* min,max,range中的时间格式要和format格式一样

# 3.数据验证

使用check.validate(a,b)进行数据验证,为验证的规则，b为验证的对象。参见[example.py]('example.py').

# 3.1 规则
规则字典包含三个键：
* all_validate              True或者False,如果是True，表示验证全部字段，False,只要有一个字段不通过就返回。
* fields                    dict，键为验证的字段，值为验证的规则，规则如下
```
required            True或者False,True表示必填，如果要验证该属性，则需要将其放在第一位，如果没有该属性但是有其他的属性，则会默认验证该属性
enum                使用enum函数验证
type                验证数据类型，常用的有int和str
email               使用email函数验证
url                 使用url函数验证
equal_to            使用equal_to函数验证
min                 使用min_value函数验证
max                 使用max_value函数验证
range               使用range_value函数验证
min_length          使用min_length函数验证
max_length          使用max_length函数验证
range_length        使用range_length函数验证
pattern             使用pattern函数验证
custom              自定义函数验证，函数参数为field(字段名),value(字段值),如果验证成功返回True,否则返回False
id_card             使用id_card函数验证
ipv4                True或者False,True使用ipv4函数验证
ipv6                True或者False,True使用ipv6函数验证
date                使用date函数验证
tel                 True或者False,True使用tel函数验证
post_code           True或者False,True使用post_cdoe函数验证
``` 
* msg dict,验证不通过的提示信息，键和fields一致

如下验证：
```
def custom(filed, value):
    """
    自定义验证函数
    :param filed:字段名
    :param value:字段值
    :return:
    """
    if filed == 'ipaddr':
        return check.pattern(value, '^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$')


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
                'custom': custom  #自定义函数验证
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
                'enum': '姓名必须在huen和rean中'
            },
            'confirm_password': {
                'equal_to': '两次输入的密码不一样。'
            }
        }
    }

```


## 3.2 提示信息

* 设置全局提示信息：
```
#覆盖默认提示
check.default_msg={
    'required':'字段必填'
}
```
* 设置字段指定规则的提示
```
rule={
    'msg':{
        'name':{
            'rquired':'请填写姓名'
    }
}
```
* 设置字段默认提示
```
rule={
    'msg':{
        'name':{
            '_default':'姓名填写不正确',
            'rquired':'请填写姓名'
    }
}

```

* 消息查找顺序
    * 1.自定义每个属性的消息
    * 2.字段默认消息（_default）
    * 3.全局默认消息
# 3.3 返回参数
返回参数是一个元组，三个值。
* 第一个是True或者False,表示验证成功或者失败
* 第二个是一个list，验证失败的字段,每一个元素是一个元组，分别是字段名和提示信息
* 第三个是一个list,验证成功的字段
```
(False, [('name', '默认消息提示'), ('password', '字段的长度不在范围内.'), ('score', '字段的值不在范围内.'), ('address', '字段太长.'), ('address1', '字段的长度不在范围内.'), ('birth', '生日输入不正确.')], ['confirm_password', 'home_page', 'ipaddr'])
```


# 3.4 完整例子

请参考[example.py]('example.py').

# 4.欢迎提issue和PR
有更好的验证方和建议，欢迎提issue和PR,weolcome!