from lib.funcao import funcao_sala, funcao_equipamento

funcao = int(input("""\nQual o setor que você quer entrar ?
      1 - Sala
      2 - Equipamento\n:"""))

if funcao == 1:
    funcao_sala()
elif funcao == 2:
    funcao_equipamento()

