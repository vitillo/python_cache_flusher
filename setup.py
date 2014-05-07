from distutils.core import setup

setup(name='cache_flusher',
      version='1.0',
      author='Roberto Agostino Vitillo',
      author_email='ra.vitillo@gmail.com',
      packages=['cache_flusher'],
      package_dir={'cache_flusher': 'cache_flusher'},
      package_data={'cache_flusher': ['data/Flush.exe']})
