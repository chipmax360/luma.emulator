# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import hashlib
import os.path

try:
    from unittest.mock import call, patch
except ImportError:
    from mock import call, patch, Mock  # noqa: F401


def md5(fname):
    with open(fname, 'rb') as fp:
        return hashlib.md5(fp.read()).hexdigest()


def get_reference_image(fname):
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'reference',
        fname))


def assert_identical(rname, fname):
    reference = get_reference_image(rname)
    assert md5(reference) == md5(fname)
