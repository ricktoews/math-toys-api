from setuptools import setup

setup(
    name='tri',
    version='0.1',
    py_modules=['tri'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        tri=tri:nth_tri
        dc=dc:dc
    ''',
)

