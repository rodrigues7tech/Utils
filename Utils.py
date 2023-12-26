import re
import os
import zipfile


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

def formatar_cnj(cnj):
    cnj_numerico = re.sub(r'\D', '', cnj)

    if len(cnj_numerico) != 20:
        raise ValueError("CNJ deve conter 20 dígitos")

    cnj_formatado = re.sub(r'(\d{7})(\d{2})(\d{4})(\d{1})(\d{2})(\d{4})', r'\1-\2.\3.\4.\5.\6', cnj_numerico)
    
    return cnj_formatado

def descompactar_arquivo_zip(diretorio: str):
    list_arquivos_zip = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.zip'):
            list_arquivos_zip.append(arquivo)

    if len(list_arquivos_zip) > 0:
        for arquivo_zip in list_arquivos_zip:
            caminho_arquivo_zip = os.path.join(diretorio, arquivo_zip)

            with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_ref:
                pasta_destino = os.path.join(diretorio, arquivo_zip.split('.')[0])
                os.makedirs(pasta_destino, exist_ok=True)
                zip_ref.extractall(pasta_destino)
            
            os.unlink(caminho_arquivo_zip)
    else:
        raise Exception('Nenhum arquivo .zip foi encontrado!')