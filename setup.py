from setuptools import setup, find_packages

setup(
    name='retirement_prediction',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',   # Библиотека для машинного обучения
        'pandas',         # Библиотека для работы с данными
        'numpy',          # Библиотека для численных вычислений
        'xgboost',        # Библиотека для градиентного бустинга
        'matplotlib',     # Библиотека для визуализации данных
        'seaborn',        # Библиотека для улучшенной визуализации
        'scipy',          # Библиотека для научных вычислений
        'statsmodels',    # Библиотека для статистического моделирования
        'imbalanced-learn',  # Библиотека для работы с несбалансированными данными
        'jupyter',        # Библиотека для работы с ноутбуками Jupyter
        'notebook',       # Библиотека для запуска Jupyter Notebook
        'pytest',         # Библиотека для тестирования
        'joblib',         # Библиотека для сохранения объектов
    ],
    entry_points={
        'console_scripts': [
            'retirement-predict=retirement_prediction.pipeline:main',
        ],
    },
)
