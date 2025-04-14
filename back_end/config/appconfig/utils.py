from typing import Any, Dict, Optional, Type, Union

def validate_parameters(mot: str, mode: str, variables: Dict[str, Any]) -> None:
    """
    Valide les paramètres d'entrée de find_value.
    
    Parameters:
        mot (str): Le motif à rechercher dans les noms des variables.
        mode (str): 'startswith' ou 'endswith'.
        variables (Dict[str, Any]): Le mapping (par ex. globals()) à parcourir.
    
    Raises:
        TypeError: Si 'mot' n'est pas une str, ou si 'variables' n'est pas un dict.
        ValueError: Si 'mode' n'est ni 'startswith' ni 'endswith'.
    """
    if not isinstance(mot, str):
        raise TypeError(f"Le paramètre 'mot' doit être une str, pas {type(mot).__name__}.")
    if mode not in ("startswith", "endswith"):
        raise ValueError("Le paramètre 'mode' doit être 'startswith' ou 'endswith'.")
    if not isinstance(variables, dict):
        raise TypeError(f"Le paramètre 'variables' doit être un dict, pas {type(variables).__name__}.")


def get_matched_variables(mot: str, mode: str, variables: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extrait du mapping toutes les paires nom→valeur dont le nom correspond au motif.
    
    Parameters:
        mot (str): motif de recherche.
        mode (str): 'startswith' ou 'endswith'.
        variables (Dict[str, Any]): mapping à filtrer.
    
    Returns:
        Dict[str, Any]: sous‑ensemble de variables dont les clés matche(nt).
    """
    return {
        name: val
        for name, val in variables.items()
        if isinstance(name, str) and getattr(name, mode)(mot)
    }


def verify_same_type(variables: Dict[str, Any]) -> Optional[Type]:
    """
    Vérifie que toutes les valeurs du dict sont du même type « haut niveau ».
    
    Parameters:
        variables (Dict[str, Any])
    
    Returns:
        Type commun, ou None si dict vide.
    
    Raises:
        TypeError: si un type diffère, avec indication de la variable fautive.
    """
    if not variables:
        return None
    iterator = iter(variables.items())
    first_name, first_val = next(iterator)
    common_type = type(first_val)
    
    for name, val in iterator:
        if type(val) is not common_type:
            raise TypeError(
                f"Type mismatch: variable '{name}' est {type(val).__name__}, "
                f"alors qu'on attend {common_type.__name__}."
            )
    return common_type


def verify_list_contents(variables: Dict[str, Any]) -> Optional[Type]:
    """
    Si les valeurs sont des listes ou tuples, vérifie que tous les éléments à l'intérieur
    sont du même type, et retourne ce type.
    
    Parameters:
        variables (Dict[str, Any])
    
    Returns:
        Type des éléments, ou None si non applicable.
    
    Raises:
        TypeError: si un contenu diffère de son type attendu, en pointant la variable et l'index.
    """
    # On suppose que verify_same_type a déjà validé que tout est list (ou tuple).
    if not variables:
        return None
    # Prendre le premier conteneur pour déterminer le type d'éléments
    first_container = next(iter(variables.values()))
    if not isinstance(first_container, (list, tuple)):
        return None
    
    # Déterminer le type d'éléments
    try:
        first_elem = first_container[0]
    except IndexError:
        return None  # liste vide => on ne peut rien dire
    
    elem_type = type(first_elem)
    
    for name, container in variables.items():
        if not isinstance(container, (list, tuple)):
            continue  # pas notre cas ici
        for idx, elem in enumerate(container):
            if type(elem) is not elem_type:
                raise TypeError(
                    f"Contenu mismatch: dans '{name}' à l'indice {idx}, "
                    f"on trouve {type(elem).__name__} au lieu de {elem_type.__name__}."
                )
    return elem_type


def prepare_output(
    variables: Dict[str, Any],
    common_type: Optional[Type],
    elem_type: Optional[Type]
) -> Any:
    """
    Construit la sortie finale :
    - si common_type est list/tuple/str, on concatène ;
    - sinon on renvoie une liste des valeurs.
    
    Parameters:
        variables (Dict[str, Any])
        common_type (Type | None)
        elem_type (Type | None)
    
    Returns:
        Union[list, tuple, str, Any]: la valeur combinée ou la liste brute.
    """
    if common_type is None:
        return None
    
    values = list(variables.values())
    
    if common_type in (list, tuple, str):
        result = values[0]
        for v in values[1:]:
            result += v
        # Pour les tuple, on s'assure bien d'en renvoyer un
        if common_type is tuple:
            return tuple(result)
        return result
    
    # Pour tout autre type, on retourne la liste brute
    return values


def find_value(
    mot: str,
    mode: str = "endswith",
    variables: Dict[str, Any] = None
) -> Any:
    """
    Recherche et agrège les variables dont le nom matche le motif.
    
    Parameters:
        mot (str): motif ('data', '_APP', etc.).
        mode (str): 'startswith' ou 'endswith'.
        variables (dict): mapping à scanner (par ex. globals()).
    
    Returns:
        Any: combinaison des valeurs trouvées, ou None si aucune.
    
    Raises:
        TypeError, ValueError: sur paramètres ou incohérences de type.
    """
    if variables is None:
        variables = globals()
    
    # 1) Validation
    validate_parameters(mot, mode, variables)
    
    # 2) Extraction
    matched = get_matched_variables(mot, mode, variables)
    if not matched:
        return None
    
    # 3) Vérification des types
    common_type = verify_same_type(matched)
    elem_type = verify_list_contents(matched)
    
    # 4) Préparation de la sortie
    return prepare_output(matched, common_type, elem_type)


# Exemple d’utilisation :
if __name__ == "__main__":
    # Simuler quelques variables globales
    foo_data = [1, 2]
    bar_data = [3, 4]
    baz_data = [5, 6]
    other = "ignore me"
    
    # On récupère toutes les variables finissant par '_data'
    res = find_value("_data", mode="endswith", variables=globals())
    print(res)  # [1,2,3,4,5,6]
