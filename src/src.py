# define standarise_smiles function to convert smiles to standardised smile 1format


from rdkit import Chem

def standardise_smiles(molecule):
    """
    Convert a molecule to standard SMILES format.

    Parameters:
    molecule (str): The input molecule in SMILES format.

    Returns:
    str: The molecule converted to standard SMILES format.
    """
    # Attempt to parse the input molecule
    mol = Chem.MolFromSmiles(molecule)
    if mol is None:
        raise ValueError("Invalid input molecule")

    # Generate the canonical SMILES
    standardized_smiles = Chem.MolToSmiles(mol)

    return standardized_smiles





from rdkit import Chem

def get_inchikey(smiles):
    """
    Convert a SMILES string to InChIKey representation.

    Parameters:
    smiles (str): The input SMILES string.

    Returns:
    str: The InChIKey representation of the molecule.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("Invalid input SMILES")
    
    inchi_key = Chem.inchi.InchiToInchiKey(Chem.MolToInchi(mol))
    return inchi_key
