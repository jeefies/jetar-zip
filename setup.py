from setuptools import setup

with open('requirements.txt') as f:
    deps = tuple(map(lambda x: x.strip(), f.read().split()))

with open('README.md') as f:
    ld = f.read()

setup(
        name = 'jetar-zip',
        packages = ['jetz'],
        version = '0.0.3',
        author = 'jeef',
        author_email = 'jeefyol@outlook.com',
        maintainer = 'Jeefy',
        maintainer_email = "jeefy163@163.com",
        long_description = ld,
        long_description_content_type = "text/markdown",
        description = "A zip/tar file saver for cache"
        )
