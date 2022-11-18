con = int(input("Quantas pessoas serão convidadas?  "))

nome = [ ]
i = 0
for i in range(con):
    nome.append (str(input("Digite o nome do convidado: ")))
    i += 1

print(f"{con} pessoas foram convidadas para essa festa, são elas:")
print(f"{nome}")