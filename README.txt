========
pdftools
========

Introduction
------------

pdftools is a library of classes for parsing and rendering PDF documents.


Installation
------------

Installation is optional as long as the directory containing the pdftools
package is included in the list of paths stored in the PYTHONPATH environment
variable.

To install the pdftools module, enter the following at the command line from
within the directory unpacked from the archive:

  python setup.py install

You may need to be the root user to install the package.


Font Metrics
------------

pdftools will automatically import the PyQt4 package, if available, so that
information about font metrics can be obtained if requested by the user. If
the PyQt4 package is not installed, this information will not be available.

If the PyQt4 package is available and you need to obtain font metrics, you
must first ensure that a QApplication instance has been created. This can be
achieved by adding the following lines of code to your application:

  from PyQt4.QtGui import QApplication
  app = QApplication([])

Please see the documentation for PyQt4 for more information about QApplication.

The mechanism used to automatically import PyQt4 and use Qt classes may change
in future versions of this package.


License
-------

Copyright (C) 2001-2008 by David Boddie

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
