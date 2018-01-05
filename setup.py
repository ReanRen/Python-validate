from setuptools import setup
from validate import __version__

setup(
    name='python-validate',
    version=__version__,
    packages=['validate'],
    url='https://github.com/ReanRen/Python-validate.git',
    license='Public domain',
    author='Rean',
    author_email='rean.ren@qq.com',
    description='python-validate表单验证',
    long_description='python表单验证，可以对电话号码，身份证号码，电子邮件验证，还可以自定义函数验证.',
    platforms=["any"],
)
