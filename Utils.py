import re

def formatar_cpf(cpf):
    cpf_numerico = re.sub(r'\D', '', cpf)

    if len(cpf_numerico) != 11:
        raise ValueError("CPF deve conter 11 dígitos")

    cpf_formatado = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf_numerico)
    
    return cpf_formatado

def formatar_cnpj(cnpj):
    cnpj_numerico = re.sub(r'\D', '', cnpj)

    if len(cnpj_numerico) != 14:
        raise ValueError("CNPJ deve conter 14 dígitos")

    cnpj_formatado = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', cnpj_numerico)
    
    return cnpj_formatado



