"""
/***************************************************************************
 InvisibleLayersAndGroups
                             A QGIS plugin
 Make some layers and groups invisible in the QGIS Layer Tree (aka Layers panel).
                             -------------------
        begin                : 2017-03-01
        copyright            : (C) 2017 by German Carrillo, GeoTux
        email                : gcarrillo@linuxmail.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
def classFactory(iface):
    from .invisibleLayersAndGroups import InvisibleLayersAndGroups
    return InvisibleLayersAndGroups(iface)
