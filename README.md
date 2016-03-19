Cardify
=======

Copyright (C) 2016  F. Brezo and Y. Rubio, i3visio

[![Version in PyPI](https://img.shields.io/pypi/v/cardify.svg)]()
[![Downloads/Month in PyPI](https://img.shields.io/pypi/dm/cardify.svg)]()
[![License](https://img.shields.io/badge/license-GNU%20General%20Public%20License%20Version%203%20or%20Later-blue.svg)]()

1 - Description
---------------

Cardify is a GPLv3+ set of libraries developed by i3visio to work with credit card information.

2 - License: GPLv3+
-------------------

This is free software, and you are welcome to redistribute it under certain conditions.

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.


For more details on this issue, check the [COPYING](COPYING) file.

3 - Installation
----------------

Fast way to do it on any system:
```
pip install cardify
```
Under MacOS or Linux systems, you may need to do this as superuser:
```
sudo pip install cardify
```
This will manage all the dependencies for you.

If you needed further information, check the [INSTALL.md](INSTALL.md) file.

4 - Basic usage
---------------

If everything went correctly (we hope so!), it's time for trying cardify by cheking if we can import it.
```
import cardify
print cardify.__version__
```

Now we can test the tool using the command line tool.
```
cardify_launcher.py -V 1234123456785678
```

Or we can try it using the library:
```
import cardify.utils as utils
print utils.verifyCardNumber("1234123456785678")
```

5 - Hacking
-----------

If you want to extend the functionalities of Cardify and you do not know where to start from, check the [HACKING.md](HACKING.md) file.

6 - Authors
-----------

More details about the authors in the [AUTHORS.md](AUTHORS.md) file.
