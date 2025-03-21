from pymol import cmd


def focus_on(selection="interface"):
    """
    Highlights a selection with focused visualization settings.

    Parameters:
        selection (str): Selection to emphasize. Default "interface".

    Actions:
        - Sets cartoon transparency to 70% opaque
        - Hides wire representation for selection
        - Shows licorice representation for selection
        - Zooms to fully contain selection with animation
    """

    cmd.set("cartoon_transparency", 0.7)
    cmd.hide("wire", selection)
    cmd.show("licorice", selection)
    cmd.zoom(selection, complete=1, animate=-1)

cmd.extend("focus_on", focus_on)
