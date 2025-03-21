from pymol import cmd


def create_ab_ag_selections(
		cplx="all",
		ab_chains="HL",
		ag_chains="A",
):
	"""
	Creates antibody-antigen chain selections for visualization.

	Parameters:
	    cplx (str): Parent selection containing all chains. Default "all".
	    ab_chains (str): 1-2 character antibody chain identifier(s). Default "HL".
	    ag_chains (str): Antigen chain identifier(s). Default "A".

	Creates:
	    - For single ab_chain: "vhh" selection
	    - For two ab_chains: "vh" (first) and "vl" (second) selections
	    - "ag" selection for antigen chains
	"""

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
	"""
	Identifies interacting residues between antibody and antigen.

	Parameters:
	    ab (str): Antibody selection. Default "vh or vl".
	    ag (str): Antigen selection. Default "ag".
	    cutoff (float): Interaction distance in Ångströms. Default 6.0.
	    sel_prefix (str): Prefix for output selections. Default "".

	Creates:
	    - {prefix}_epitope: Antigen residues within cutoff of antibody
	    - {prefix}_paratope: Antibody residues within cutoff of antigen
	    - {prefix}_interface: Combined epitope+paratope selection
	"""

	if sel_prefix and sel_prefix[-1] != "_":
		sel_prefix += "_"

	epitope = sel_prefix + "epitope"
	paratope = sel_prefix + "paratope"
	interface = sel_prefix + "interface"
	cmd.select(epitope, f"byres ({ag}) within {cutoff} of ({ab})", enable=0)
	cmd.select(paratope, f"byres ({ab}) within {cutoff} of ({ag})", enable=0)
	cmd.select(interface, f"{epitope} or {paratope}", enable=1)

cmd.extend("find_interface", find_interface)
