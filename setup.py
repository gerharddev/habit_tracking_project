from setuptools import setup

setup(
    name='OOFPP_Habits_Phase3',
    version='1.0',
    packages=['habits_backend', 'habits_backend.crud', 'habits_backend.models', 'habits_backend.modules',
              'habits_backend.restapi', 'habits_backend.schemas', 'habits_backend.database', 'habits_backend.services'],
    url='https://github.com/gerharddev/oof_habits_project',
    license='',
    author='Marthinus Maree',
    author_email='marthinusgerhardus.maree@iu-academy.org',
    description='OOFPP'
)
