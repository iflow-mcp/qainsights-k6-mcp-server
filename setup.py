from setuptools import setup, find_packages

setup(
    name='iflow-mcp_qainsights_k6-mcp-server',
    version='0.1.1',
    packages=find_packages(),
    py_modules=['main', 'k6_server'],
    include_package_data=True,
    install_requires=[
        'mcp[cli]>=1.6.0',
    ],
    entry_points={
        'console_scripts': [
            'k6-server=main:main',
        ],
    },
)