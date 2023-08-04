import pyvista as pv
from pathlib import Path
import os
import numpy as np


def split_with_multiple_textures(obj_path, mtl_path=None, texture_dir=None):
    obj_mesh = pv.read(obj_path.as_posix())
    if mtl_path is None:
        # parse the obj file for mtl_path if the mtl_path is not set.
        pass
    if texture_dir is None:
        texture_dir = os.path.dirname(obj_path.as_posix())

    texture_paths = []
    mtl_names = []

    # parse the mtl file
    with open(mtl_path.as_posix()) as mtl_file:
        for line in mtl_file.readlines():
            parts = line.split()
            if len(parts) < 2:
                continue
            if parts[0] == 'map_Kd':
                combined_name=line[len(parts[0])+1 :-1]
                texture_paths.append(texture_dir.joinpath(combined_name))
            elif parts[0] == 'newmtl':
                mtl_names.append(parts[1])

    plotter = pv.Plotter()
    material_ids = obj_mesh.cell_data['MaterialIds']
    actor=plotter.add_mesh(obj_mesh)
    
    # This part is not working.
    #for i in np.unique(material_ids):
    #    actor.texture[mtl_names[i]] = pv.read_texture(texture_paths[i])
        #obj_mesh.textures[mtl_names[i]] = pv.read_texture(texture_paths[i])
    # plotter.add_mesh(obj_mesh)
    
    # This one do.
    for i in np.unique(material_ids):
        mesh_part = obj_mesh.extract_cells(material_ids == i)
        mesh_part.save("mesh{}.vtu".format(i))
        #actor.texture = pv.read_texture(texture_paths[i])
        

    plotter.view_xz(negative=True)
    #plotter.show()
    plotter.show(screenshot='redfortunegreyscale.png')

AirshipOBJ=Path("./Airship Assets/02_trawlew ue4.obj")
AirshipMTL=Path("./Airship Assets/02_trawlew ue4.mtl")
texture_dir=Path("./Airship Assets/")
#mesh=pv.read(Airship.as_posix())
#pl=pv.Plotter()
#pl.add_mesh(mesh)
#pl.show_axes()
#pl.show()
split_with_multiple_textures(AirshipOBJ, mtl_path=AirshipMTL, texture_dir=texture_dir)