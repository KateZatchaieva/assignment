from setuptools import setup, find_packages


setup(name='jsonplaceholder',
      description='assignment for qbtech',
      author='kzaetchaieva',
      packages=find_packages(),
      install_requires=[
            "certifi==2023.7.22",
            "charset-normalizer==3.2.0",
            "exceptiongroup==1.1.3",
            "idna==3.4",
            "iniconfig==2.0.0",
            "Jinja2==3.1.2",
            "logging==0.4.9.6",
            "MarkupSafe==2.1.3",
            "packaging==23.1",
            "pluggy==1.3.0",
            "pytest==7.4.1",
            "pytest-html==4.0.0",
            "pytest-metadata==3.0.0",
            "requests==2.31.0",
            "tomli==2.0.1",
            "urllib3==2.0.4"
      ]
      )
