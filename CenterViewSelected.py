#########################################################################
# Centers the view to selected item(s)                                  #
# License: GPL v3                                                       #
#########################################################################

############# Add-on description (used by Blender) ######################
bl_info = {
    "name": "Center View to Selected",
    "description": 'Centers the 3D View to Selected',
    "author": "hatterer raoul",
    "version": (0, 1),
    "blender": (3, 00, 0),
    "location": "View > Align View > Center View to Selected",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"}

#########################################################################
import bpy

class CentereViewSelected(bpy.types.Operator):
    """Center the 3D viewport on the selected item(s)"""
    bl_idname = "view3d.view_center_selected"
    bl_label = "Center View to Selected"
   
    def execute(self, context):
        # store the current cursor location
        cursor_location = context.scene.cursor.location.copy()
        # center the cursor on the active item
        bpy.ops.view3d.snap_cursor_to_selected()
        # center the view on the cursor
        bpy.ops.view3d.view_center_cursor()
        # reset the cursor location
        context.scene.cursor.location = cursor_location
        return {'FINISHED'}


def menu_func(self,context):
    # self.layout.separator()     
    self.layout.operator(CentereViewSelected.bl_idname)

addon_keymaps = []

def register():
    bpy.utils.register_class(CentereViewSelected)
    bpy.types.VIEW3D_MT_view_align.prepend(menu_func)

    # Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new(CentereViewSelected.bl_idname, type='NUMPAD_PERIOD', value='PRESS', shift=True)
        addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(CentereViewSelected)
    bpy.types.VIEW3D_MT_view_align.remove(menu_func)

    # Remove the hotkey
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()    
    
if __name__ == "__main__":
    register()
