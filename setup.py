from setuptools import setup


setup(name="grue",
      version='0.1',
      description='You are in a maze of twisty little passages...',
      long_description='',
      keywords='you are likely to be eaten by a grue',
      url='http://github.com/storborg/grue',
      author='Scott Torborg',
      author_email='scott@cartlogic.com',
      install_requires=[
          'pexpect',
          # These are for tests.
          'coverage',
          'nose>=1.1',
          'nose-cover3',
      ],
      license='MIT',
      packages=['grue'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
