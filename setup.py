from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='NLPnicer',
  version='5.0.1',
  description='NLPnicer helps you to handle abbreviation, emoji and spelling mistake in your text' ,
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/samarthgupta0309/nlpnicer',  
  author='Samarth Gupta',
  author_email='samarthgupta0309@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='NLPnicer', 
  packages=find_packages(),
  install_requires=['textblob'] 
)
