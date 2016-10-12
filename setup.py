from setuptools import setup


setup(
    name='Cigenerator',
    version='0.1',
    description='jenkins generator based on pipeline templates',
    keywords='ci jenkins pipeline generator',
    url='https://github.com/widgetpl/cigenerator',
    author='Mike Dziedziela',
    author_email='michal.dziedziela@gmail.com',
    requires=['yaml', 'jinja2']
)