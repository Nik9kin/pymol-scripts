from pymol import cmd


PALE_DARK_PALETTE = {
    "vh": "lightblue",
    "vhh": "lightblue",
    "vl": "deepsalmon",
    "ag": "palegreen",
    "acidic": "ruby",
    "basic": "skyblue",
    "polar": "violetpurple",
}

PALETTES = {
    "pale_dark": PALE_DARK_PALETTE,
}


def color_ab_ag(
        vh="vh",
        vl="vl",
        vhh="vhh",
        ag="ag",
        palette="pale_dark"
):
    """
    Colors antibody-antigen complexes using predefined chain selections and palette.

    Requires pre-existing selections created by create_ab_ag_selections. Colors
    carbon atoms in specified chains according to the selected color palette.

    Parameters:
        vh (str): Selection name for VH chain. Default "vh".
        vl (str): Selection name for VL chain. Default "vl".
        vhh (str): Selection name for single-domain VHH chain. Default "vhh".
        ag (str): Selection name for antigen chain(s). Default "ag".
        palette (str): Color scheme from PALETTES dictionary. Default "pale_dark".

    Notes:
        - Only colors existing selections (vh/vl/vhh/ag)
        - Affects only carbon atoms (e. C)
        - Available palettes: "pale_dark"
    """

    palette = PALETTES[palette]
    sel_names = cmd.get_names("selections")
    for key, value in [("vh", vh), ("vl", vl), ("vhh", vhh), ("ag", ag)]:
        if key in sel_names:
            cmd.color(palette[key], f"({value}) and e. C")

cmd.extend("color_ab_ag", color_ab_ag)


def color_acidic_basic_polar(selection="all", palette="pale_dark"):
    """
    Colors sidechains by chemical property: acidic, basic, or polar residues.

    Parameters:
        selection (str): Atoms to color. Default "all".
        palette (str): Color scheme from PALETTES dictionary. Default "pale_dark".

    Notes:
        - Only colors sidechain carbon atoms (e. C)
    """

    palette = PALETTES[palette]
    cmd.color(palette["acidic"], f"({selection}) and sidechain and resn ASP+ASH+GLU and e. C")
    cmd.color(palette["basic"], f"({selection}) and sidechain and resn ARG+ARH+LYS+HIS+HID+HIE and e. C")
    cmd.color(palette["polar"], f"({selection}) and sidechain and resn SER+THR+ASN+GLN+TYR and e. C")

cmd.extend("color_acidic_basic_polar", color_acidic_basic_polar)
