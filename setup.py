from setuptools import setup, find_packages

setup(name='custom_connector_sdk',
      version='1.0.5',
      description='Amazon AppFlow Custom Connector SDK',
      url='https://github.com/awslabs/aws-appflow-custom-connector-python',
      author='Amazon AppFlow',
      license="Apache License 2.0",
      python_requires=">= 3.6",
      packages=find_packages(include=['custom*']),
      include_package_data=True,
      zip_safe=False
      )
