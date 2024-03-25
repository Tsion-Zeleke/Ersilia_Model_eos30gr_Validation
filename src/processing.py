import numpy as np
import pandas as pd
from rdkit import Chem
from standardiser import standardise

def validate_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return mol is not None and mol.GetNumAtoms() > 0

def validate_smiles_in_csv(csv_file):
    df = pd.read_csv(csv_file)

    valid_count = 0
    invalid_count = 0
    for index, row in df.iterrows():
        smiles = row['smiles']
        if validate_smiles(smiles):
            valid_count += 1
        else:
            invalid_count += 1
    return valid_count, invalid_count



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

def standardise_smiles_from_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    smiles = df['smiles'].tolist()
    
    mols = []
    for smi in smiles:
        try:
            mol = Chem.MolFromSmiles(smi)
        except:
            mol = np.nan
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
                st_smi = np.nan
        else:
            st_smi = np.nan
        st_smiles += [st_smi]
    
    df['Standardized_SMILES'] = st_smiles
    df.to_csv(output_file, index=False)
    
    # Count the number of standardized smiles
    num_standardized_smiles = len([smi for smi in st_smiles if smi is not np.nan])
    print(f"Number of standardized SMILES: {num_standardized_smiles}")


