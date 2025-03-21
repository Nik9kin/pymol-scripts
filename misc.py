from pymol import cmd


def focus_on(selection="interface"):
    cmd.set("cartoon_transparency", 0.7)
    cmd.hide("wire", selection)
    cmd.show("licorice", selection)
    cmd.zoom(selection, complete=1, animate=-1)

cmd.extend("focus_on", focus_on)
