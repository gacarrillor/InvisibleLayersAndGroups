"""
/***************************************************************************
 InvisibleLayersAndGroups
                             A QGIS plugin
 Make some layers and groups invisible in the QGIS Layer Tree (aka ToC).
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
import os

from qgis.core import ( QgsProject, QgsLayerTreeLayer, QgsLayerTreeGroup, 
                        QgsMapLayer )
from PyQt4.QtGui import QIcon, QAction

# Initialize Qt resources from file resources.py
import resources_rc

class InvisibleLayersAndGroups:

    def __init__( self, iface ):
        self.iface = iface
        self.ltv = self.iface.layerTreeView()
        self.model = self.ltv.model()
        self.root = QgsProject.instance().layerTreeRoot()
        QgsProject.instance().readProject.connect( self.readHiddenNodes )

    def initGui( self ):
        self.actionHide = QAction( QIcon(":/plugins/InvisibleLayersAndGroups/hide.png"), u"Make selected layers and groups invisible", self.iface.mainWindow() )
        self.actionHide.triggered.connect( self.runHide )
        self.actionShow = QAction( QIcon(":/plugins/InvisibleLayersAndGroups/show.png"), u"Show invisible layers and groups", self.iface.mainWindow() )
        self.actionShow.triggered.connect( self.runShow )

        self.iface.addToolBarIcon( self.actionHide )
        self.iface.addToolBarIcon( self.actionShow )
        self.iface.addPluginToMenu( u"&Invisible layers and groups", self.actionHide )
        self.iface.addPluginToMenu( u"&Invisible layers and groups", self.actionShow )

    def unload( self ):
        QgsProject.instance().readProject.disconnect( self.readHiddenNodes )
        self.iface.removePluginMenu( u"&Invisible layers and groups", self.actionHide )
        self.iface.removePluginMenu( u"&Invisible layers and groups", self.actionShow )
        self.iface.removeToolBarIcon( self.actionHide )
        self.iface.removeToolBarIcon( self.actionShow )

    def runHide( self ):
        selectedNodes = self.ltv.selectedNodes( True )
        for node in selectedNodes:
            self.hideNode( node )

    def runShow( self ):
        self.showHiddenNodes( self.root )

    def hideNode( self, node, bHide=True ):
        if type( node ) in ( QgsLayerTreeLayer, QgsLayerTreeGroup ):
            index = self.model.node2index( node )
            self.ltv.setRowHidden( index.row(), index.parent(), bHide )
            node.setCustomProperty( 'nodeHidden', 'true' if bHide else 'false' )
            self.ltv.setCurrentIndex( self.model.node2index( self.root ) )

    def showHiddenNodes( self, group ):
        for child in group.children():
            if child.customProperty( "nodeHidden" ) == 'true': # Node is currently hidden
                self.hideNode( child, False )
            if isinstance( child, QgsLayerTreeGroup ): # Continue iterating
                self.showHiddenNodes( child )

    def hideNodesByProperty( self, group ):
        for child in group.children():
            if child.customProperty( "nodeHidden" ) == 'true': # Node should be hidden
                self.hideNode( child )
            if isinstance( child, QgsLayerTreeGroup ): # Continue iterating
                self.hideNodesByProperty( child )

    def readHiddenNodes( self ):
        """ SLOT """
        self.hideNodesByProperty( self.root )


    def hideLayer( self, mapLayer ):
        if isinstance( mapLayer, QgsMapLayer ):
            self.hideNode( self.root.findLayer( mapLayer.id() ) )

    def hideGroup( self, group ):
        if isinstance( group, QgsLayerTreeGroup ):
            self.hideNode( group )
        elif isinstance( group, ( str, unicode ) ):
            self.hideGroup( self.root.findGroup( group ) )

