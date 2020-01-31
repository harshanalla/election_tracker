'''
a class called QgsMapTool that already has a lot of things we want.
For example, it allows us to program on the events such as mouse down or up.
We don't want to modify the original class (which will require making changes
to the source code installed on the computer), but we can easily extend the
original class into a new one that is our own and we write our code there.
This technique is called inherit in Python object-oriented programming.
The following is the new class of our own, extending the existing class of QgsMapTool.
'''
from qgis.core import *
from datetime import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QCursor
from qgis.gui import *

class PointTool(QgsMapTool):
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
    def canvasPressEvent(self, event):
        #Get the click (button down)
        print('down:', event.mapPoint(), event.pixelPoint())
    def canvasReleaseEvent(self, event):
        #Get the click (button up)
        print('up:', event.mapPoint(), event.pixelPoint())
    def canvasMoveEvent(self, event):
        pass
    def activate(self):
        print('Maptool activated')
    def deactivate(self):
        print('Maptool deactivated')
    def isZoomTool(self):
        return False
    def isTransient(self):
        return False
    def isEditTool(self):
        return True
#
# tool = PointTool(iface.mapCanvas())
# iface.mapCanvas().setMapTool(tool)
# to re-activate tool, run the above line again


class SelectTool(QgsMapToolIdentify):
    def __init__(self, canvas):
        QgsMapToolIdentify.__init__(self, canvas)
        self.canvas = canvas
        self.selected = [] # keep a record of all features clicked upon
        self.setCursor(Qt.ArrowCursor)
    def canvasReleaseEvent(self, event): # mouse release
        l = iface.activeLayer()
        if l is not None:
            results = self.identify(event.x(), event.y(), [l], QgsMapToolIdentify.TopDownStopAtFirst)
            if len(results) > 0:
                for r in results:
                    id = r.mFeature.id()
                    if not id in self.selected:
                        self.selected.append(id)
                    else:
                        self.selected.remove(id)
            else:
                self.selected = []
            l.selectByIds(self.selected)
            self.updateAttr(l)
    # def updateAttr(self, layer):
    #     selection = layer.selectedFeatures()
    #     # for f in selection:
    #     #     print(f.attributes())
    #     if (l.dataProvider().capabilities and QgsVectorDataProvider.DeleteFeatures):
    #         for f in selection:
    #             fid = f.attributes()[0]
    #             if ( 'Won' is pressed ):
    #                 attr = { 7 : 1 } #Change the values of the attributes based on their indexes, 1=Won
    #             elif ( 'Lost' ...):
    #                 attr = { 7 : 0 }
    #             elif ( 'Undecided' ...):
    #                 attr = { 7 : -1 }
    #             l.dataProvider().changeAttributeValues({ fid : attr})


'''
We override some methods ourselves. We also make a new class by subclassig the
QgsMapToolIdentify class that comes with some convenient methods. Overriding mainly
this one called canvasReleaseEvent to program action for the mouse release event.
Within the overrriding, we use the method called identify from the class to retrieve
the features that touch the mouse point. The identify method returns a list of the
IdentifyResult objects, where the member called mFeature is a QgsFeature object,
which is the actual feature being clicked upon.
'''
# class SelectTool(QgsMapToolIdentify):
#     def __init__(self, canvas, iface, layer):
#
#         QgsMapToolIdentify.__init__(self, canvas)
#
#         self.canvas = canvas
#         self.selected = [] # keep a record of all features clicked upon
#         self.setCursor(Qt.PointingHandCursor)
#         self.layer = layer
#         self.iface = iface
#         self.exportProgress("Done with __init__")
#     def canvasReleaseEvent(self, event): # mouse release
#         self.exportProgress("Start event")
#         l = self.iface.activeLayer()
#         if l is not None:
#             results = self.identify(event.x(), event.y(), [l], QgsMapToolIdentify.TopDownStopAtFirst)
#             if len(results) > 0:
#                 for r in results:
#                     id = r.mFeature.id()
#                     if not id in self.selected:
#                         self.selected.append(id)
#                     else:
#                         self.selected.remove(id)
#             else:
#                 self.selected = []
#             l.selectByIds(self.selected)
#             self.printFeatures(l)
#     def exportProgress(self, textmsg):
#         text_file = open("C:/Users/Jhonny/Desktop/Test/Test2.txt", "w")
#         now = datetime.now()
#         time = now.strftime("%H_%M_%S")
#         textmsg += " "+time
#         text_file.write(textmsg)
#         text_file.close()
#
#         return
#
#     def printFeatures(self, layer):
#         text_file = open("C:/Users/Jhonny/Desktop/Test/Test1.txt", "w")
#         selection = layer.selectedFeatures()
#         textmsg = 'Attributes: \n'
#         for f in selection:
#             textmsg += str(f.attributes()) + '\n'
#         text_file.write(textmsg)
#         text_file.close()
#         return
 # '''Comment after this'''
            # self.updateAttr(l)
    # def updateAttr(self, layer):
    #     selection = layer.selectedFeatures()
    #     # for f in selection:
    #     #     print(f.attributes())
    #     if (l.dataProvider().capabilities and QgsVectorDataProvider.DeleteFeatures):
    #         for f in selection:
    #             fid = f.attributes()[0]
    #             if ( 'Won' is pressed ):
    #                 attr = { 7 : 1 } #Change the values of the attributes based on their indexes, 1=Won
    #             elif ( 'Lost' ...):
    #                 attr = { 7 : 0 }
    #             elif ( 'Undecided' ...):
    #                 attr = { 7 : -1 }
    #             l.dataProvider().changeAttributeValues({ fid : attr})
    #
    #     '''
    #     HELP HARSHA: you're more familiar with the actions related to events in the
    #     widget like clicking the bulletins of 'Won', 'Lost', and 'Undecided'
    #     So if you don't mind, can you help me relating the conditions in the if's
    #     to the clicking of different bulletin buttons?
    #     '''
# 
# seltool = SelectTool(iface.mapCanvas())
# iface.mapCanvas().setMapTool(seltool)
#



'''
Now we work on the color change of the polygons that were selected and had their
status ID changed accordingly (0,1,-1). Based on what value of a polygon is in the
newly added column in the "joined" layer's attribute table, we apply a categorized
renderer.

Using library shp as a sample. In the "CITY" attribute, there are the following values:
COLUMBUS, GROVEPORT, REYNOLDSBURG, HILLIARD, DUBLIN, GAHANNA
# '''
# def colorChange(layer):
#     # layer = iface.acitiveLayer() # load the layer as you want
#
#     # define the lookup >> value : (color, label)
#     colors = {1: ('blue', 'Won'),
#             0: ('red', 'Lost'),
#             -1: ('gray', 'Undecided'),
#             2: ('black', 'Unmatched')}
#     # create a category for each item in your layer
#     categories = []
#     for unique_id, (color, label) in colors.items():
#         symbol = QgsSymbol.defaultSymbol(layer.geometryType())
#         symbol.setColor(QColor(color))
#         category = QgsRendererCategory(unique_id, symbol, label)
#         categories.append(category)
#
#     # create the renderer and assign it to the layer
#     expression = ''' THIS IS WHAT YOU NAMED THE FIELD FOR ELECT_RESULT (a string)'''
#     renderer = QgsCategorizedSymbolRenderer(expression, categories)
#
#     # for cat in ren
#     derer.categories():
#     #     print("{}: {} :: {}".format(cat.value(), cat.label(), cat.symbol()))
#     renderer = QgsCategorizedSymbolRenderer(expression, categories)
#     layer.setRenderer(renderer)
#     layer.triggerRepaint()
#
# colorChange(iface.activeLayer())
