import re

def formatar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf_numerico = re.sub(r'\D', '', cpf)

    # Verificar se o CPF possui 11 dígitos
    if len(cpf_numerico) != 11:
        raise ValueError("CPF deve conter 11 dígitos")

    cpf_formatado = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf_numerico)
    
    return cpf_formatado


