import pytest

from Tests.contest import base_ch_Test
from pages.Homepage import Homepage


class Test_thepage(base_ch_Test):
    def test_choosedates(self):
        self.homePage=Homepage(self.driver)
        self.homePage.selectfrom("29/11/2022")
        self.homePage.selectto("29/11/2022")

