from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='pysend-mailer',
    version='0.0.1',
    description='Python send mailer package',
    classifiers=[
        'Development Status :: 0.0.1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7^',
        'Topic :: Send Email Processing :: Linguistic',
      ],
    packages=['pysend-mail'],
    keywords='python sender emails',
    entry_points={
        'console_scripts': [
            'pysend-mailer=pysend-mailer.command_line:run'
        ]
    },
    url='https://github.com/j4l13n/pysend-mailer',
    author='Karangwa Hirwa Julien',
    author_email='juliushirwa@gmail.com',
    license='MIT',
)
