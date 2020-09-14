import setuptools


setuptools.setup(
    name='brewing-inventory',
    version='0.0.0',
    author='Merlin Webster',
    author_email='mjftwebster@gmail.com',
    description='Brewing inventory management system',
    url='https://github.com/mjftw/pywebapp-demo',
    package_dir={'': 'src'},
    packages=['brewinv'],
    python_requires='>=3.6',
    install_requires=[
        'fastapi'
    ]
)
