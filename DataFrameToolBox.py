import pandas as pd



def Valeurs_manquantes(DataFrame, mode, valeur = 0):
    """
    Recherche les valeurs manquantes du dataframe, et execute une action 
    sur les cellules concernées, selon le mode choisi :
        - 'suppr' : Suppression des lignes concernées
        - 'remplir : Remplissage des valeurs manquantes par une valeur donnée
    
    Paramètres : 
        param DataFrame: DataFrame qui contient des valeurs nulles
        type file: DataFrame
        param mode: méthode à choisir parmi les deux possibles
        type mode: String
        param valeur: Valeur pour remplacer les valeurs nulles si on a 
                        choisi le mode 'remplir'
        type valeur: objet
        
    Returns:
        DataFrame:  DataFrame nettoyé
        type : DataFrame
    
    """

    if mode == 'suppr':
        return(DataFrame.dropna())
    
    elif mode == 'remplir':
        df = DataFrame.fillna(valeur)
        df.replace('',valeur)
        return(df)





def Jointure(DataFrame1, DataFrame2, key):
    """
    Crée un DataFrame résultant de la jointure entre les deux paramètres
        d'entrée, en prenant pour clé de jointure le paramètre key
    
    Paramètres : 
        param DataFrame1: 1er DataFrame à joindre
        type DataFrame1: DataFrame
        param DataFrame2: 2ème DataFrame à joindre
        type DataFrame2: DataFrame
        param key: Colonne de référence pour joindre les deux DataFrames, il
                    est impératif d'avoir cette même colonne dans les deux 
                    DataFrames
        type key: string
        
    Returns:
        DataFrame:  DataFrame résultat de la jointure
        type : DataFrame
    
    """
    return(DataFrame1.join(DataFrame2.set_index(key), on=key))





def Binarise_colonne(DataFrame, Colonne):
    """
    Binarise une colonne d'un DataFrame : on ajoute à ce DataFrame une colonne
        par modalité de la colonne choisie 
        Exemple, pour une colonne 'couleur' qui prend pour valeurs 'bleu', 
                'rouge' et 'vert', on obtient 3 colonnes résultantes 
                'couleur_rouge', 'couleur_vert' et 'couleur_bleu' contenant
                1 ou 0, selon la valeure initiale de la couleur sur cette ligne
    
    Paramètres : 
        param DataFrame: DataFrame contenant la colonne à binariser
        type DataFrame: DataFrame
        param Colonne: Nom de la colonne à modifier
        type Colonne: string
        
    Returns:
        DataFrame:  DataFrame résultat avec les colonnes supplémentaires
        type : DataFrame
    
    """
    series = pd.get_dummies(DataFrame[Colonne])
    for col in list(series):
        DataFrame[str(Colonne) + '_' +  str(col)] = series[str(col)]
    return(DataFrame)





def Transforme_DataFrame_fichier(DataFrame, extension, chemin = None):
    """
    Transforme un dataframe en le format selectionné, c'est à dire :
        - csv
        - json
        - array
    Pour l'option csv, on précisera un chemin permettant d'enregistrer le
        fichier. Pour les autres, on obtiendra des objets du type voulu.
    
    Paramètres : 
        param DataFrame: DataFrame à transformer
        type DataFrame: DataFrame
        param extension: Nom du type voulu
        type extension: string
        param extension: Chemin où enregister le csv (avec un nom terminant 
                                                      par.csv)
        type extension: string
        
    Returns:
        - Dans le cas csv
            Rien
        - Dans le cas json
            une variable format json (dictionnaire)
            type : string pour python
        - Dans le cas array
            un numpy array
    
    """
    if extension == 'csv':
        DataFrame.to_csv(chemin)
        
    elif extension == 'json':
        return(DataFrame.to_json())
    
    elif extension == 'array':
        return(DataFrame.to_numpy())
