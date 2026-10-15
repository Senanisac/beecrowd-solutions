
#Leitura dos numeros e conversao 
n1, n2, n3, n4 = map(float, input().split())

#Calcular media
m = (n1 *2) + (n2 *3) + (n3 *4) + n4
media = m / 10

#Condicoes e saidas
if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
else:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    
    valor = float(input())
    print(f"Nota do exame: {valor:.1f}")
    
    mediaf = (media + valor) / 2
    
    if mediaf >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {mediaf:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {mediaf:.1f}")

