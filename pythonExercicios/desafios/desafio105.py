def notas(* nota, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(nota)
    dados['maior'] = max(nota)
    dados['menor'] = min(nota)
    soma = 0
    for n in nota:
        soma += n
    dados['media'] = soma/len(nota)

    if sit:
        if dados['media'] >= 7:
            dados['situacao'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situacao'] = 'RAZOAVEL'
        else:
            dados['situacao'] = 'RUIM'
    return dados


print('-'*30)
resp = notas(5.5, 9.5, 10, 6.5)
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
# resp = notas(5.5, sit=True)
# resp = notas(4, sit=True)
print(resp)
help(notas)