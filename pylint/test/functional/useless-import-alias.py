# pylint: disable=unused-import, missing-docstring, invalid-name, reimported, import-error, wrong-import-order, no-name-in-module, relative-beyond-top-level
from collections import OrderedDict as OrderedDict # [useless-import-alias]
from collections import OrderedDict as o_dict
import os.path as path # [useless-import-alias]
import os.path as p
import foo.bar.foobar as foobar # [useless-import-alias]
import os
import os as OS
from sys import version
from . import bar as bar # [useless-import-alias]
from . import bar as Bar
from . import bar
from ..foo import bar as bar # [useless-import-alias]
from ..foo.bar import foobar as foobar # [useless-import-alias]
from ..foo.bar import foobar as anotherfoobar
