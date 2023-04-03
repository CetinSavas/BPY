# Create panel for fast vertex color assignment
bl_info = {
    "name": "Colorize Faces",
    "author": "Savas",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "ColorizeFaces",
    "warning": "",
    "doc_url": "",
    "category": "",
}

import bpy
import bmesh
from bpy.types import (Panel,Operator)

class ColorizeVertex(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "vertexops.colorize_vertex"
    bl_label = "Colorize Vertex"
    Rc: bpy.props.FloatProperty(default=0.0)
    Gc: bpy.props.FloatProperty(default=0.0)
    Bc: bpy.props.FloatProperty(default=1.0)
  
    def execute(self, context):
        
        face_color=[self.Rc,self.Gc,self.Bc,0.0]
        mesh = bpy.context.active_object 
        obj = bpy.context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        if not me.vertex_colors:
            me.vertex_colors.new()
        
        vertex_colors=bm.loops.layers.color['Col']
        
        selfaces=[f for f in bm.faces if f.select]


        color_table = {v : face_color
                            for v in bm.verts}
        for face in selfaces:
            for loop in face.loops:
                loop[vertex_colors] = color_table[loop.vert]

        if bm.is_wrapped:
            bmesh.update_edit_mesh(me)
        else:
            bm.to_mesh(me)
            me.update()
        return {'FINISHED'}

class ColorizePanel(bpy.types.Panel):

    bl_label = "Colorize  Panel"
    bl_idname = "OBJECT_PT_Colorize"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Colorize Faces"

    def draw(self, context):
        layout = self.layout

        row1=layout.row()
        r1b1=row1.operator(ColorizeVertex.bl_idname, text="C1V1")
        r1b1.Rc=0.64
        r1b1.Gc=0.32
        r1b1.Bc=0.00
        r1b2=row1.operator(ColorizeVertex.bl_idname, text="C1V2")
        r1b2.Rc=0.68
        r1b2.Gc=0.34
        r1b2.Bc=0.00
        r1b3=row1.operator(ColorizeVertex.bl_idname, text="C1V3")
        r1b3.Rc=0.72
        r1b3.Gc=0.36
        r1b3.Bc=0.00
        r1b4=row1.operator(ColorizeVertex.bl_idname, text="C1V4")
        r1b4.Rc=0.77
        r1b4.Gc=0.38
        r1b4.Bc=0.00
        r1b5=row1.operator(ColorizeVertex.bl_idname, text="C1V5")
        r1b5.Rc=0.81
        r1b5.Gc=0.40
        r1b5.Bc=0.00
        r1b6=row1.operator(ColorizeVertex.bl_idname, text="C1V6")
        r1b6.Rc=0.85
        r1b6.Gc=0.42
        r1b6.Bc=0.00


        row2=layout.row()
        r2b1=row2.operator(ColorizeVertex.bl_idname, text="C2V1")
        r2b1.Rc=0.64
        r2b1.Gc=0.64
        r2b1.Bc=0.00
        r2b2=row2.operator(ColorizeVertex.bl_idname, text="C2V2")
        r2b2.Rc=0.68
        r2b2.Gc=0.68
        r2b2.Bc=0.00
        r2b3=row2.operator(ColorizeVertex.bl_idname, text="C2V3")
        r2b3.Rc=0.72
        r2b3.Gc=0.72
        r2b3.Bc=0.00
        r2b4=row2.operator(ColorizeVertex.bl_idname, text="C2V4")
        r2b4.Rc=0.77
        r2b4.Gc=0.77
        r2b4.Bc=0.00
        r2b5=row2.operator(ColorizeVertex.bl_idname, text="C2V5")
        r2b5.Rc=0.81
        r2b5.Gc=0.81
        r2b5.Bc=0.00
        r2b6=row2.operator(ColorizeVertex.bl_idname, text="C2V6")
        r2b6.Rc=0.85
        r2b6.Gc=0.85
        r2b6.Bc=0.00


        row3=layout.row()
        r3b1=row3.operator(ColorizeVertex.bl_idname, text="C3V1")
        r3b1.Rc=0.32
        r3b1.Gc=0.64
        r3b1.Bc=0.00
        r3b2=row3.operator(ColorizeVertex.bl_idname, text="C3V2")
        r3b2.Rc=0.34
        r3b2.Gc=0.68
        r3b2.Bc=0.00
        r3b3=row3.operator(ColorizeVertex.bl_idname, text="C3V3")
        r3b3.Rc=0.36
        r3b3.Gc=0.72
        r3b3.Bc=0.00
        r3b4=row3.operator(ColorizeVertex.bl_idname, text="C3V4")
        r3b4.Rc=0.38
        r3b4.Gc=0.77
        r3b4.Bc=0.00
        r3b5=row3.operator(ColorizeVertex.bl_idname, text="C3V5")
        r3b5.Rc=0.40
        r3b5.Gc=0.81
        r3b5.Bc=0.00
        r3b6=row3.operator(ColorizeVertex.bl_idname, text="C3V6")
        r3b6.Rc=0.42
        r3b6.Gc=0.85
        r3b6.Bc=0.00


        row4=layout.row()
        r4b1=row4.operator(ColorizeVertex.bl_idname, text="C4V1")
        r4b1.Rc=0.00
        r4b1.Gc=0.64
        r4b1.Bc=0.00
        r4b2=row4.operator(ColorizeVertex.bl_idname, text="C4V2")
        r4b2.Rc=0.00
        r4b2.Gc=0.68
        r4b2.Bc=0.00
        r4b3=row4.operator(ColorizeVertex.bl_idname, text="C4V3")
        r4b3.Rc=0.00
        r4b3.Gc=0.72
        r4b3.Bc=0.00
        r4b4=row4.operator(ColorizeVertex.bl_idname, text="C4V4")
        r4b4.Rc=0.00
        r4b4.Gc=0.77
        r4b4.Bc=0.00
        r4b5=row4.operator(ColorizeVertex.bl_idname, text="C4V5")
        r4b5.Rc=0.00
        r4b5.Gc=0.81
        r4b5.Bc=0.00
        r4b6=row4.operator(ColorizeVertex.bl_idname, text="C4V6")
        r4b6.Rc=0.00
        r4b6.Gc=0.85
        r4b6.Bc=0.00


        row5=layout.row()
        r5b1=row5.operator(ColorizeVertex.bl_idname, text="C5V1")
        r5b1.Rc=0.00
        r5b1.Gc=0.64
        r5b1.Bc=0.32
        r5b2=row5.operator(ColorizeVertex.bl_idname, text="C5V2")
        r5b2.Rc=0.00
        r5b2.Gc=0.68
        r5b2.Bc=0.34
        r5b3=row5.operator(ColorizeVertex.bl_idname, text="C5V3")
        r5b3.Rc=0.00
        r5b3.Gc=0.72
        r5b3.Bc=0.36
        r5b4=row5.operator(ColorizeVertex.bl_idname, text="C5V4")
        r5b4.Rc=0.00
        r5b4.Gc=0.77
        r5b4.Bc=0.38
        r5b5=row5.operator(ColorizeVertex.bl_idname, text="C5V5")
        r5b5.Rc=0.00
        r5b5.Gc=0.81
        r5b5.Bc=0.40
        r5b6=row5.operator(ColorizeVertex.bl_idname, text="C5V6")
        r5b6.Rc=0.00
        r5b6.Gc=0.85
        r5b6.Bc=0.42


        row6=layout.row()
        r6b1=row6.operator(ColorizeVertex.bl_idname, text="C6V1")
        r6b1.Rc=0.00
        r6b1.Gc=0.64
        r6b1.Bc=0.64
        r6b2=row6.operator(ColorizeVertex.bl_idname, text="C6V2")
        r6b2.Rc=0.00
        r6b2.Gc=0.68
        r6b2.Bc=0.68
        r6b3=row6.operator(ColorizeVertex.bl_idname, text="C6V3")
        r6b3.Rc=0.00
        r6b3.Gc=0.72
        r6b3.Bc=0.72
        r6b4=row6.operator(ColorizeVertex.bl_idname, text="C6V4")
        r6b4.Rc=0.00
        r6b4.Gc=0.77
        r6b4.Bc=0.77
        r6b5=row6.operator(ColorizeVertex.bl_idname, text="C6V5")
        r6b5.Rc=0.00
        r6b5.Gc=0.81
        r6b5.Bc=0.81
        r6b6=row6.operator(ColorizeVertex.bl_idname, text="C6V6")
        r6b6.Rc=0.00
        r6b6.Gc=0.85
        r6b6.Bc=0.85


        row7=layout.row()
        r7b1=row7.operator(ColorizeVertex.bl_idname, text="C7V1")
        r7b1.Rc=0.00
        r7b1.Gc=0.32
        r7b1.Bc=0.64
        r7b2=row7.operator(ColorizeVertex.bl_idname, text="C7V2")
        r7b2.Rc=0.00
        r7b2.Gc=0.34
        r7b2.Bc=0.68
        r7b3=row7.operator(ColorizeVertex.bl_idname, text="C7V3")
        r7b3.Rc=0.00
        r7b3.Gc=0.36
        r7b3.Bc=0.72
        r7b4=row7.operator(ColorizeVertex.bl_idname, text="C7V4")
        r7b4.Rc=0.00
        r7b4.Gc=0.38
        r7b4.Bc=0.77
        r7b5=row7.operator(ColorizeVertex.bl_idname, text="C7V5")
        r7b5.Rc=0.00
        r7b5.Gc=0.40
        r7b5.Bc=0.81
        r7b6=row7.operator(ColorizeVertex.bl_idname, text="C7V6")
        r7b6.Rc=0.00
        r7b6.Gc=0.43
        r7b6.Bc=0.85


        row8=layout.row()
        r8b1=row8.operator(ColorizeVertex.bl_idname, text="C8V1")
        r8b1.Rc=0.00
        r8b1.Gc=0.00
        r8b1.Bc=0.64
        r8b2=row8.operator(ColorizeVertex.bl_idname, text="C8V2")
        r8b2.Rc=0.00
        r8b2.Gc=0.00
        r8b2.Bc=0.68
        r8b3=row8.operator(ColorizeVertex.bl_idname, text="C8V3")
        r8b3.Rc=0.00
        r8b3.Gc=0.00
        r8b3.Bc=0.72
        r8b4=row8.operator(ColorizeVertex.bl_idname, text="C8V4")
        r8b4.Rc=0.00
        r8b4.Gc=0.00
        r8b4.Bc=0.77
        r8b5=row8.operator(ColorizeVertex.bl_idname, text="C8V5")
        r8b5.Rc=0.00
        r8b5.Gc=0.00
        r8b5.Bc=0.81
        r8b6=row8.operator(ColorizeVertex.bl_idname, text="C8V6")
        r8b6.Rc=0.00
        r8b6.Gc=0.00
        r8b6.Bc=0.85


        row9=layout.row()
        r9b1=row9.operator(ColorizeVertex.bl_idname, text="C9V1")
        r9b1.Rc=0.32
        r9b1.Gc=0.00
        r9b1.Bc=0.64
        r9b2=row9.operator(ColorizeVertex.bl_idname, text="C9V2")
        r9b2.Rc=0.34
        r9b2.Gc=0.00
        r9b2.Bc=0.68
        r9b3=row9.operator(ColorizeVertex.bl_idname, text="C9V3")
        r9b3.Rc=0.36
        r9b3.Gc=0.00
        r9b3.Bc=0.72
        r9b4=row9.operator(ColorizeVertex.bl_idname, text="C9V4")
        r9b4.Rc=0.38
        r9b4.Gc=0.00
        r9b4.Bc=0.77
        r9b5=row9.operator(ColorizeVertex.bl_idname, text="C9V5")
        r9b5.Rc=0.40
        r9b5.Gc=0.00
        r9b5.Bc=0.81
        r9b6=row9.operator(ColorizeVertex.bl_idname, text="C9V6")
        r9b6.Rc=0.42
        r9b6.Gc=0.00
        r9b6.Bc=0.85


        row10=layout.row()
        r10b1=row10.operator(ColorizeVertex.bl_idname, text="C10V1")
        r10b1.Rc=0.64
        r10b1.Gc=0.00
        r10b1.Bc=0.64
        r10b2=row10.operator(ColorizeVertex.bl_idname, text="C10V2")
        r10b2.Rc=0.68
        r10b2.Gc=0.00
        r10b2.Bc=0.68
        r10b3=row10.operator(ColorizeVertex.bl_idname, text="C10V3")
        r10b3.Rc=0.72
        r10b3.Gc=0.00
        r10b3.Bc=0.72
        r10b4=row10.operator(ColorizeVertex.bl_idname, text="C10V4")
        r10b4.Rc=0.77
        r10b4.Gc=0.00
        r10b4.Bc=0.77
        r10b5=row10.operator(ColorizeVertex.bl_idname, text="C10V5")
        r10b5.Rc=0.81
        r10b5.Gc=0.00
        r10b5.Bc=0.81
        r10b6=row10.operator(ColorizeVertex.bl_idname, text="C10V6")
        r10b6.Rc=0.85
        r10b6.Gc=0.00
        r10b6.Bc=0.85


        row11=layout.row()
        r11b1=row11.operator(ColorizeVertex.bl_idname, text="C11V1")
        r11b1.Rc=0.64
        r11b1.Gc=0.00
        r11b1.Bc=0.32
        r11b2=row11.operator(ColorizeVertex.bl_idname, text="C11V2")
        r11b2.Rc=0.68
        r11b2.Gc=0.00
        r11b2.Bc=0.34
        r11b3=row11.operator(ColorizeVertex.bl_idname, text="C11V3")
        r11b3.Rc=0.72
        r11b3.Gc=0.00
        r11b3.Bc=0.36
        r11b4=row11.operator(ColorizeVertex.bl_idname, text="C11V4")
        r11b4.Rc=0.77
        r11b4.Gc=0.00
        r11b4.Bc=0.38
        r11b5=row11.operator(ColorizeVertex.bl_idname, text="C11V5")
        r11b5.Rc=0.81
        r11b5.Gc=0.00
        r11b5.Bc=0.40
        r11b6=row11.operator(ColorizeVertex.bl_idname, text="C11V6")
        r11b6.Rc=0.85
        r11b6.Gc=0.00
        r11b6.Bc=0.42


        row12=layout.row()
        r12b1=row12.operator(ColorizeVertex.bl_idname, text="C12V1")
        r12b1.Rc=0.64
        r12b1.Gc=0.00
        r12b1.Bc=0.00
        r12b2=row12.operator(ColorizeVertex.bl_idname, text="C12V2")
        r12b2.Rc=0.68
        r12b2.Gc=0.00
        r12b2.Bc=0.00
        r12b3=row12.operator(ColorizeVertex.bl_idname, text="C12V3")
        r12b3.Rc=0.72
        r12b3.Gc=0.00
        r12b3.Bc=0.00
        r12b4=row12.operator(ColorizeVertex.bl_idname, text="C12V4")
        r12b4.Rc=0.77
        r12b4.Gc=0.00
        r12b4.Bc=0.00
        r12b5=row12.operator(ColorizeVertex.bl_idname, text="C12V5")
        r12b5.Rc=0.81
        r12b5.Gc=0.00
        r12b5.Bc=0.00
        r12b6=row12.operator(ColorizeVertex.bl_idname, text="C12V6")
        r12b6.Rc=0.85
        r12b6.Gc=0.00
        r12b6.Bc=0.00        
        


_classes =  [
    ColorizeVertex,
    ColorizePanel
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)



def unregister():
    for cls in _classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
