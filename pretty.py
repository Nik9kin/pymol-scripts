from pymol import cmd


def cute_hinged_model(selection="all"):
    """
    Configures visual styling for a hinged molecular model representation.

    Sets bond and sphere properties to create a simplified view. Sticks are shown
    with reduced thickness and spheres scaled down to emphasize overall structure.

    Parameters:
        selection (str, optional): Atom selection to apply styling. Defaults to "all".
    """

    cmd.set_bond("stick_radius", 0.14, selection)
    cmd.set("sphere_scale", 0.25, selection)
    cmd.show("sticks", selection)
    cmd.show("spheres", selection)

cmd.extend("cute_hinged_model", cute_hinged_model)
