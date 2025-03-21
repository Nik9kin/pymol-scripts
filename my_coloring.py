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
    palette = PALETTES[palette]
    sel_names = cmd.get_names("selections")
    for key, value in [("vh", vh), ("vl", vl), ("vhh", vhh), ("ag", ag)]:
        if key in sel_names:
            cmd.color(palette[key], f"({value}) and e. C")

cmd.extend("color_ab_ag", color_ab_ag)


def color_acidic_basic_polar(selection="all", palette="pale_dark"):
    palette = PALETTES[palette]
    cmd.color(palette["acidic"], f"({selection}) and sidechain and resn ASP+ASH+GLU and e. C")
    cmd.color(palette["basic"], f"({selection}) and sidechain and resn ARG+ARH+LYS+HIS+HID+HIE and e. C")
    cmd.color(palette["polar"], f"({selection}) and sidechain and resn SER+THR+ASN+GLN+TYR and e. C")

cmd.extend("color_acidic_basic_polar", color_acidic_basic_polar)
