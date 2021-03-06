from setuptools import setup, find_packages
setup(
    name = 'mahuri',
    version = '0.1.0',
    description = 'test description',
    long_description = 'longgggggg description',
    author = 'Aakash Basnet',
    author_email = 'dummyemail@hahaha.com',
    url = 'www.google.com',
    lisence = '243123',
    packages = find_packages(exclude=('tests', 'docs')
    # entry_points = {
    #     'console_scripts': [
    #         'mahuri = mahuri.__main__:main'
    #     ]
    }
)