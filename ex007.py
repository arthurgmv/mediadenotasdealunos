nome = str(input("Digite o nome do(a) aluno(a) "))
nota1 = float(input ("Digite a primeira nota do(a) aluno(a) "))
nota2 = float(input ("Digite a segunda nota do(a) aluno(a) "))

media = (nota1 + nota2)/2 

print ("A média do(a) aluno(a) é {}".format(media))
if media >= 7: print ("Aluno(a): {} \nSituação: Aprovado(a)".format(nome))
else: print ("Aluno(a): {} \nSituação: Reprovado(a)".format(nome))
input ("Presione alguma tecla para sair do sistema ")

