from pymol import cmd


def cute_hinged_model(selection="all"):
    cmd.set_bond("stick_radius", 0.14, selection)
    cmd.set("sphere_scale", 0.25, selection)
    cmd.show("sticks", selection)
    cmd.show("spheres", selection)

cmd.extend("cute_hinged_model", cute_hinged_model)
