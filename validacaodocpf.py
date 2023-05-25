def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    
    if len(set(cpf)) == 1:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    
    # Verifica se os dígitos calculados são iguais aos dígitos informados
    return cpf[-2:] == str(digito1) + str(digito2)

cpf = input("Escreva o cpf: ")
if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")