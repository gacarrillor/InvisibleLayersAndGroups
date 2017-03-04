# Invisible layers and groups
QGIS plugin to make some layers and groups invisible in the QGIS Layer Tree (aka ToC). E.g., lookup tables.

**Invisible layers/groups will not appear in the Layers Panel, but they can still be seen in the canvas or used in joins/relations with other layers.**

This plugin allows you to:


 - Make selected layers/groups invisible (plugin button).
 - Make layers/groups (that are invisible) visible again (plugin button).
 - Store layers/groups visibility in your QGIS project.
 - Recreate layers/groups visibility when you open your QGIS project.
 - Make a particular layer invisible (by code).
 - Make a particular group invisible (by code).


*NOTE: There is an issue you should be aware of. If you make a layer invisible and then move its parent group, the invisible layer will be visible again (I don't know why!). My recommendation is to make only top-level layers/groups invisible (after all, you cannot move the root).*

For example, you could have a 'black hole' group where you put all layers/groups that should be invisible. 

    root
       |.. layer 1
       |.. layer 2
       |.. Black-hole-group  # Make this group invisible (all its children will be invisible too)
           |.. layer 3
           |.. layer 4
           |.. sub-group
               |-- sub-layer
             
You could even keep adding layers/groups programatically to the Black-hole-group after invisible:

    root = QgsProject.instance().layerTreeRoot()
    blackHole = root.findGroup('Black-hole-group')
    QgsMapLayerRegistry.instance().addMapLayer( myLayer, False )
    blackHole.insertLayer( 0, myLayer ) # myLayer will be invisible too!


###Making a layer invisible (by code):

    if 'InvisibleLayersAndGroups' in qgis.utils.plugins:
        ilg = qgis.utils.plugins['InvisibleLayersAndGroups']
        ilg.hideLayer( layer )    # layer is a QgsMapLayer

###Making a group invisible (by code):

    if 'InvisibleLayersAndGroups' in qgis.utils.plugins:
        ilg = qgis.utils.plugins['InvisibleLayersAndGroups']
        ilg.hideGroup( group )    # group is a QgsLayerTreeGroup
        ilg.hideGroup( 'group2' ) # You can also pass a group name

