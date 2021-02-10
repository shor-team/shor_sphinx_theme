from setuptools import setup
from io import open
from shor_sphinx_theme import __version__

setup(
    name = 'shor_sphinx_theme',
    version =__version__,
    author = 'Shift Lab',
    author_email= 'info@shiftlabny.com',
    url="https://github.com/shor-team/shor_sphinx_theme",
    docs_url="https://github.com/shor-team/shor_sphinx_theme",
    description='Shor Sphinx Theme',
    py_modules = ['shor_sphinx_theme'],
    packages = ['shor_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'shor_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/fonts/*.*',
        'static/images/*.*',
        'theme_variables.jinja'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'shor_sphinx_theme = shor_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ]
)
