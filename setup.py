import setuptools

with open('README.md', encoding="utf8") as f:
    readme = f.read()

setuptools.setup(
    name='gatepy',
    version='1.0.0',
    description='',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/MrNereof/gatepy/',
    author='MrNereof',
    author_email='mrnereof@gmail.com',
    python_requires='>=3.4',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'],
    keywords=['gate', 'logical gate'],
    packages=['gatepy'],
)
