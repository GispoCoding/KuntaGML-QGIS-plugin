#  Gispo Ltd., hereby disclaims all copyright interest in the program KuntaGML-QGIS-plugin
#  Copyright (C) 2020 Gispo Ltd (https://www.gispo.fi/).
#
#
#  This file is part of KuntaGML-QGIS-plugin.
#
#  KuntaGML-QGIS-plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  KuntaGML-QGIS-plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with KuntaGML-QGIS-plugin.  If not, see <https://www.gnu.org/licenses/>.

import pytest

from ..core.kuntagml2layers import KuntaGML2Layers


def test_turku_opaskartta(new_project):
    url = "https://opaskartta.turku.fi/TeklaOGCWeb/WFS.ashx"

    converter = KuntaGML2Layers(url, '2.1.6', '2.1.1', '1.1.0')
    converter.populate_features()
    assert len(converter.feature_types) == 90
    layers = converter.convert_feature_types(['akaava:Kaava'])
    assert len(layers['akaava:Kaava']) == 5


def test_riihimaki_opaskartta(new_project):
    url = "https://kartta.riihimaki.fi/teklaogcweb/WFS.ashx?request=GetCapabilities"

    converter = KuntaGML2Layers(url, '2.1.6', '2.1.1', '1.1.0')
    converter.populate_features()
    print(converter.feature_types)
    assert len(converter.feature_types) == 72
    layers = converter.convert_feature_types(['kanta:Kevyenliikenteenvayla'])
    assert len(layers['kanta:Kevyenliikenteenvayla']) == 3


@pytest.mark.skip("Host requires authentication")
def test_lahti_opaskartta(new_project):
    url = "https://kartta.lahti.fi/TeklaOGCWeb/WFS.ashx"

    converter = KuntaGML2Layers(url, '2.1.6', '2.1.1', '1.1.0')
    converter.populate_features()
    assert len(converter.feature_types) == 97
    converter.convert_feature_types(['kanta:Kevyenliikenteenvayla'])


@pytest.mark.skip("Host requires authentication")
def test_jkyla_opaskartta(new_project):
    url = "https://kartta.jkl.fi/TeklaOgcWeb/WFS.ashx?request=GetCapabilities"

    converter = KuntaGML2Layers(url, '2.1.6', '2.1.1', '1.1.0')
    converter.populate_features()
    assert 88 == len(converter.feature_types)
    print(converter.feature_types)
    converter.convert_feature_types(['kanta:Kevyenliikenteenvayla'])
