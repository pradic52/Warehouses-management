def validate_parameters(mot: str, mode: str) -> None:
    """
    Valide les paramètres d'entrée.
    
    Parameters:
        mot (str): Le motif à rechercher dans les noms des variables.
        mode (str): La méthode de correspondance, qui doit être 'startswith' ou 'endswith'.
    
    Raises:
        TypeError: Si 'mot' n'est pas une chaîne de caractères.
        ValueError: Si 'mode' n'est ni 'startswith' ni 'endswith'.
    """
    if not isinstance(mot, str):
        raise TypeError(f"Le paramètre 'mot' doit être une chaîne de caractères, or {type(mot).__name__} a été fourni.")
    if mode not in ["startswith", "endswith"]:
        raise ValueError("Le paramètre 'mode' doit être 'startswith' ou 'endswith'.")


def get_matched_variables(mot: str, mode: str) -> dict:
    """
    Récupère les variables globales dont le nom correspond au motif donné.
    
    Parameters:
        mot (str): Le motif à rechercher dans les noms des variables.
        mode (str): La méthode de correspondance ('startswith' ou 'endswith').
    
    Returns:
        dict: Un dictionnaire contenant {nom_variable: valeur} pour chaque variable correspondante.
    """
    matched_vars = {
        key: value for key, value in globals().items()
        if isinstance(key, str) and getattr(key, mode)(mot)
    }
    return matched_vars


def verify_same_type(variables: dict) -> type:
    """
    Vérifie que toutes les valeurs dans le dictionnaire ont le même type.
    
    Parameters:
        variables (dict): Dictionnaire des variables trouvées.
    
    Returns:
        type: Le type commun des valeurs.
    
    Raises:
        TypeError: Si une des valeurs diffère du type des autres, en indiquant le nom de la variable fautive.
    """
    # Si aucune variable n'a été trouvée, on ne peut déterminer de type commun.
    if not variables:
        return None

    # On récupère le type de la première variable
    common_type = type(next(iter(variables.values())))
    
    for var_name, value in variables.items():
        if type(value) is not common_type:
            raise TypeError(
                f"La variable '{var_name}' est de type {type(value).__name__} "
                f"alors que le type attendu est {common_type.__name__}."
            )
    return common_type


def prepare_output(variables: dict, common_type: type):
    """
    Combine les valeurs des variables trouvées en respectant leur type.
    
    Pour les types supportant l'addition (par exemple, list, str, tuple), on retourne
    la combinaison de toutes les valeurs. Pour les autres types, on retourne une liste des valeurs.
    
    Parameters:
        variables (dict): Dictionnaire des variables trouvées.
        common_type (type): Le type commun des valeurs.
    
    Returns:
        La valeur combinée avec le même type que celles des variables, ou une liste si le type
        ne supporte pas la combinaison par addition.
    """
    # S'il n'y a aucune variable trouvée, on retourne une "valeur vide" cohérente.
    if common_type is None:
        return None

    # Si aucune variable n'est présente, on retourne une valeur vide selon le type attendu.
    if not variables:
        if common_type is list:
            return []
        elif common_type is str:
            return ""
        elif common_type is tuple:
            return ()
        else:
            return None

    values = list(variables.values())
    
    # Pour les types qui supportent l'addition (list, str, tuple)
    if common_type in (list, str, tuple):
        result = values[0]
        for value in values[1:]:
            result += value
        return result
    else:
        # Pour les autres types, on retourne une liste des valeurs
        return values


def find_value(mot: str, mode: str = "endswith"):
    """
    Recherche dans les variables globales celles dont le nom correspond au motif donné,
    vérifie que toutes leurs valeurs sont du même type et prépare une sortie combinée respectant ce type.
    
    L'objectif est de pouvoir configurer séparément chaque "app" installée de sorte que,
    si besoin, il suffit de supprimer son importation sans avoir à chercher toutes les références.
    
    Parameters:
        mot (str): Le motif à rechercher dans les noms des variables.
        mode (str): Méthode de correspondance, 'startswith' ou 'endswith'. Par défaut 'endswith'.
    
    Returns:
        La valeur combinée des variables trouvées, du même type que ces valeurs, ou None s'il n'y a aucune variable correspondante.
    
    Raises:
        TypeError, ValueError: En cas de problème de paramètres ou d'incohérence des types des variables trouvées.
    """
    # Vérifier que les paramètres d'entrée sont valides.
    validate_parameters(mot, mode)
    
    # Extraire les variables globales correspondantes.
    matched_vars = get_matched_variables(mot, mode)
    
    # Si aucune variable n'a été trouvée, on retourne None (ou une valeur vide selon le besoin).
    if not matched_vars:
        return None

    # Vérifier que toutes les valeurs ont le même type.
    common_type = verify_same_type(matched_vars)
    
    # Préparer et retourner la sortie combinée.
    return prepare_output(matched_vars, common_type)


# Exemple d'utilisation :
if __name__ == "__main__":
    # Définition de quelques variables globales pour le test
    app_data_1 = [1, 2, 3]
    app_data_2 = [4, 5, 6]
    other_var = "non concerné"

    # Recherche de variables dont le nom se termine par 'data_1'
    # Ici, par exemple, on pourrait appeler avec mot="data" et mode="endswith"
    result = find_value("app_data", mode="startswith")
    print("Résultat de find_value :", result)

