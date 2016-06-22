# NOTE: assumes presence of pandas, scipy, matplotlib,
#       such as in a conda environment.

from setuptools import setup, find_packages

test_requirements = ['sentinels>=0.0.6', 'nose>=1.0', 'python-dateutil>=2.2']

setup(
    name = "women_tech",
    version = "0.01",
    packages = find_packages(),

    # Dependencies on other packages:
    setup_requires   = ['nose>=1.1.2'],
    tests_require    = test_requirements,
    install_requires = ['ijson>=1.0', 
			#'pandas>=0.18.0',
			'xlrd>=0.9.4',
			#'scipy>= 0.17.0',
			#'matplotlib>= 1.5.1',
			'survey_utils>=0.0.5',
			] + test_requirements,

    # Unit tests; they are initiated via 'python setup.py test'
    #test_suite       = 'json_to_relation/test',
    test_suite       = 'nose.collector', 

    #data_files = [('pymysql_utils/data', datafiles)],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
     #   '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
     #   'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Andreas Paepcke",
    author_email = "paepcke@cs.stanford.edu",
    description = "Stats analysis for survey on Women in Tech Companies..",
    license = "BSD",
    keywords = "survey analysis",
    #url = "https://github.com/paepcke/json_to_relation",   # project home page, if any
)
