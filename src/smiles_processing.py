import numpy as np
from rdkit import Chem
from standardiser import standardise


def standardise_smiles(smiles):
    mols = []
    for smi in smiles:
        try:
            mol = Chem.MolFromSmiles(smi)
        except:
            mol=np.nan
        mols += [mol]
    st_mols = []
    for mol in mols:
        if mol is not None:
            try:
                st_mol = standardise.run(mol)
            except:
                st_mol = np.nan
        else:
            st_mol = np.nan
        st_mols += [st_mol]
    st_smiles = []
    for st_mol in st_mols:
        if st_mol is not None:
            try:
                st_smi = Chem.MolToSmiles(st_mol)
            except:
                st_smi=np.nan
        else:
            st_smi = np.nan
        st_smiles += [st_smi]
    return st_smiles