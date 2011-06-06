#! /usr/bin/env python

from distutils.core import setup

import pdftools

setup(
    name         = "pdftools",
    description  = "PDF document reading classes",
    author       = "David Boddie",
    author_email = "david@boddie.org.uk",
    url          = "http://www.boddie.org.uk/david/Projects/Python/pdftools",
    version      = pdftools.__version__,
    packages     = ["pdftools"]
    )
