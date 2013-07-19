"""
Tornado-WeRoBot
---------------

Adds WeRoBot support to Tornado.

:copyright: (c) 2013 by whtsky.
:license: BSD, see LICENSE for more details.

Links
`````

* `documentation <https://tornado-werobot.readthedocs.org/>`_
"""


from setuptools import setup

setup(
    name='Tornado-WeRoBot',
    version='0.2.0',
    url='https://github.com/whtsky/Tornado-WeRoBot',
    license='BSD',
    author='whtsky',
    author_email='whtsky@gmail.com',
    description='Writing WeChat Robot by WeRoBot in Tornado.',
    long_description=__doc__,
    py_modules=['Tornado_werobot'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Tornado',
        'WeRoBot>=0.3.5'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
