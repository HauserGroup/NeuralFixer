# %%
from Bio.PDB import PDBParser, PDBIO
import numpy as np
import argparse


def main(pdb_file, plddt_file, output_file):
    # Path to the PDB file
    # pdb_file = "../../test_run/out/prot_all.pdb"
    # plddt_file = "../../test_run/out/plddt_struct.npy"

    # Create a PDB parser object
    parser = PDBParser()
    structure = parser.get_structure("receptors", pdb_file)
    print(f"Number of models: {len(structure)}")

    # Load the pLDDT scores
    plddt = np.load(plddt_file)
    print(f"pLDDT scores shape: {plddt.shape}")

    # Loop over models
    for model in structure:
        # Loop over chains
        for chain in model:
            # Loop over residues
            for residue in chain:
                # Set the B factor to the custom value
                residue["CA"].set_bfactor(plddt[model.id, int(residue.get_id()[1]) - 1])

    # Save the annotated structure to a new file
    # structure_file = "../../test_run/out/prot_all_annotated.pdb"
    io = PDBIO()
    io.set_structure(structure)
    io.save(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Annotate a PDB file with pLDDT scores"
    )
    parser.add_argument("pdb_file", type=str, help="Path to the PDB file")
    parser.add_argument("plddt_file", type=str, help="Path to the pLDDT scores file")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    args = parser.parse_args()

    main(args.pdb_file, args.plddt_file, args.output_file)
