############################ Copyrights and license ############################
#                                                                              #
# Copyright 2022 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import unittest

import github


class Requester(unittest.TestCase):

    PrimaryRateLimitErrors = [
        "API rate limit exceeded for x.x.x.x. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)"
    ]
    SecondaryRateLimitErrors = [
        "You have exceeded a secondary rate limit and have been temporarily blocked from content creation. Please retry your request again later.",
        "You have exceeded a secondary rate limit. Please wait a few minutes before you try again."
    ]
    OtherErrors = [
        "User does not exist or is not a member of the organization"
    ]

    def testIsRateLimitError(self):
        for message in self.PrimaryRateLimitErrors + self.SecondaryRateLimitErrors:
            self.assertTrue(github.Requester.Requester.isRateLimitError(message), message)
        for message in self.OtherErrors:
            self.assertFalse(github.Requester.Requester.isRateLimitError(message), message)

    def testIsPrimaryRateLimitError(self):
        for message in self.PrimaryRateLimitErrors:
            self.assertTrue(github.Requester.Requester.isPrimaryRateLimitError(message), message)
        for message in self.OtherErrors + self.SecondaryRateLimitErrors:
            self.assertFalse(github.Requester.Requester.isPrimaryRateLimitError(message), message)

    def testIsSecondaryRateLimitError(self):
        for message in self.SecondaryRateLimitErrors:
            self.assertTrue(github.Requester.Requester.isSecondaryRateLimitError(message), message)
        for message in self.OtherErrors + self.PrimaryRateLimitErrors:
            self.assertFalse(github.Requester.Requester.isSecondaryRateLimitError(message), message)
