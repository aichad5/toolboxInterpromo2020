def min_max_scale(X_train):
    '''
    Transform les données pour qu'elle soit normalisées par le min et
    le max.
    :param X_train: données à scale par min max
    :return: X_train_minmax : retour les données scale avec le min et
    le max
    '''

    from sklearn.preprocessing import MinMaxScaler
    min_max_scaler = MinMaxScaler()
    X_train_minmax = min_max_scaler.fit_transform(X_train)
    return X_train_minmax


def string_to_int_class(class_array_like):
    '''
    Transforme les classes écrite en string en classes numériques
    Exemple : print(string_to_int_class(["Première classe", "Seconde classe", "Economique"]))

    -> [1,2,0]
    :param class_array_like: array like qui contient la liste des classes
    :return: onehotencoded : array like qui contient la liste des classes
    en numérique
    '''
    from sklearn.preprocessing import LabelEncoder

    enc = LabelEncoder()
    encodedLabel = enc.fit_transform(class_array_like)

    return encodedLabel
