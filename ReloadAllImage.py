# reloads all images in file
bl_info = {
    "name": "Reload All Images",
    "author": "Savas",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Reloads all images",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from bpy.types import (Panel,Operator)

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "reload.1"
    bl_label = "Reload Images"

  
    def execute(self, context):
        for image in bpy.data.images:
            image.reload()
        return {'FINISHED'}

class ImagePanel(bpy.types.Panel):

    bl_label = "Reload Panel"
    bl_idname = "OBJECT_PT_reload"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Reload Images"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Reload All Images", icon='FILE_REFRESH')

from bpy.utils import register_class, unregister_class

_classes =  [
    ButtonOperator,
    ImagePanel
]

def register():
    for cls in _classes:
        register_class(cls)



def unregister():
    for cls in _classes:
        unregister_class(cls)

if __name__ == "__main__":
    register()
