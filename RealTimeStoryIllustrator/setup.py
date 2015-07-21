from distutils.core import setup

setup(
    name='RealTimeStoryIllustrator',
    version='0.1',
    packages=['services', 'test', 'ui'],
    url='https://github.com/nichtawitz/bac',
    license='',
    author='hoebartNichtawitz',
    author_email='',
    description='Real Time Story Illustrator - Narrates  german stories and displays fitting images',
    install_requires=[
        'gTTs',
        'PySide',
        'goslate'
    ]
)
