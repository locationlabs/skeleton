"""
Basic Template system for project skeleton,
similar to the template part of PasteScript but without any dependencies.

"""

from skeleton.core import (
    Skeleton, Var, Bool, DependentVar, FileNameKeyError, TemplateKeyError
    )
from skeleton.utils import insert_into_file
