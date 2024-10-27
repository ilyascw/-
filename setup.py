from setuptools import setup, find_packages

setup(
    name='retirement_prediction',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'pandas',
        'numpy',
        'xgboost',
    ],
    entry_points={
        'console_scripts': [
            'retirement-predict=retirement_pipeline.pipeline:main',
        ],
    },
)
