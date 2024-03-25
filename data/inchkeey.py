from rdkit import Chem
from rdkit.Chem import inchi

# Convert the InChI string to a standard InChI format
standard_inchi = inchi.MolToInchi(Chem.MolFromInchi("(BLGXFZZNTVWLAY-SCYLSFHTSA-N"))

# Generate the InChIKey from the standard InChI format
inchi_key = inchi.InchiToInchiKey(standard_inchi)

print(inchi_key)