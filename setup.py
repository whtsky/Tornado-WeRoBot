from setuptools import setup
import tornado_werobot

setup(
    name='Tornado-WeRoBot',
    version=tornado_werobot.__version__,
    url='https://github.com/whtsky/Tornado-WeRoBot',
    license='BSD',
    author='whtsky',
    author_email='whtsky@gmail.com',
    description='Writing WeChat Robot by WeRoBot in Tornado.',
    long_description=tornado_werobot.__doc__,
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
