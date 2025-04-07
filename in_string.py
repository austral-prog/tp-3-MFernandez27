def check_vowels():
    nombre = input()
    nombremin = nombre.lower()
    print("Contiene a:" , "a" in nombremin)
    print("Contiene e:" , "e" in nombremin)
    print("Contiene i:" , "i" in nombremin)
    print("Contiene o:" , "o" in nombremin)
    print("Contiene u:" , "u" in nombremin)


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
