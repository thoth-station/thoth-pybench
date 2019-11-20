import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="thoth-pybench",
    version="0.0.5",
    description="Adopted PyBench tool to benchmark Python interpreter by the Thoth team.",
    long_description=read("README"),
    author="Marc-Andre Lemburg",
    author_email="mal@lemburg.com",
    maintainer="Francesco Murdaca",
    maintainer_email="fmurdaca@redhat.com",
    url="https://openbenchmarking.org/test/pts/pybench",
    download_url="https://github.com/thoth-station/thoth-pybench",
    packages=[
        "pybench",
        "pybench.package",
    ],
    zip_safe=False,
    install_requires=[],
    long_description_content_type="text/plain",
    entry_points={"console_scripts": ["pybench=pybench.pybench:PyBenchCmdline"]},
)
