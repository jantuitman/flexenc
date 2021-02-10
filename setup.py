from setuptools import find_packages, setup
setup(
    name='flexenc',
    packages=find_packages(include=['flexenc']),
    version='0.1.1',
    description='an encoder/decoder/tokenizer to preprocess text you want to train a neural network with',
    author='Jan Tuitman',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)