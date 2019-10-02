#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright (C) Incuvers, Inc - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by David Sean
#
import unittest

from badger import Badger


class TestApp(unittest.TestCase):
    def setUp(self):
        self.badge = Badger(fname="test_badge.svg")

    def tearDown(self):
        del self.badge

    # Endpoints
    def SKIPtest_string_nologo(self):

        self.badge.define("0123456789", "0123456789")
        self.badge.save()

    def test_string(self):
        self.badge.init_blank()
        self.badge.define("0123456789", "0123456789")
        self.badge.add_logo()
        self.badge.save()


if __name__ == '__main__':
    unittest.main()
