from pymol import cmd


def create_ab_ag_selections(
		cplx="all",
		ab_chains="HL",
		ag_chains="A",
):
	if len(ab_chains) == 1:
		cmd.select("vhh", f"{cplx} and c. {ab_chains}", enable=0)
	elif len(ab_chains) == 2:
		cmd.select("vh", f"{cplx} and c. {ab_chains[0]}", enable=0)
		cmd.select("vl", f"{cplx} and c. {ab_chains[1]}", enable=0)
	else:
		raise ValueError(f"Incorrect ab_chains: {ab_chains}")

	cmd.select("ag", f"{cplx} and c. {'+'.join(ag_chains)}", enable=0)

cmd.extend("create_ab_ag_selections", create_ab_ag_selections)


def find_interface(
		ab="vh or vl",
		ag="ag",
		cutoff=6.0,
		sel_prefix="",
):
	if sel_prefix and sel_prefix[-1] != "_":
		sel_prefix += "_"

	epitope = sel_prefix + "epitope"
	paratope = sel_prefix + "paratope"
	interface = sel_prefix + "interface"
	cmd.select(epitope, f"byres ({ag}) within {cutoff} of ({ab})", enable=0)
	cmd.select(paratope, f"byres ({ab}) within {cutoff} of ({ag})", enable=0)
	cmd.select(interface, f"{epitope} or {paratope}", enable=1)

cmd.extend("find_interface", find_interface)
