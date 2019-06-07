from setuptools import find_packages, setup

setup(
    name='touchterrain',
    packages=find_packages(),
    include_package_data=True,
    dependency_links=[
        'https://github.com/allelos/vectors/tarball/master#egg=vectors-99.0.0'
    ],
    install_requires=[
        'Jinja2>=2.10.1',
        'Pillow>=6.0.0',
        'earthengine-api>=0.1.178',
        'Flask>=1.0.2',
        'vectors==99.0.0',
        'vectormath>=0.2.2',
        'oauth2client>=4.1.3',
    ],
    extras_require={
        'server': [
            'gunicorn>=19.9.0',
        ],
    },
)
