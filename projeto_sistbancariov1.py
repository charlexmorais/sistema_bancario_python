

menu =""""
[d]Deposito
[s]Saque
[e]Extrato
[q]Sair

=>"""
deposito =0
saldo =0
limite =500
extrato=""
numeros_saques=0
LIMITE_SAQUES=3

while True:
 opcao =input(menu)
 if opcao == "d":
    valor = float(input("informe o valor do deposito!"))
    if valor > 0:
      saldo == valor
      extrato += f"Deposito:R$ {valor:.2f}\n"
      print("deposito concluido com sucesso!!!")
    else :
      print("Operação invalida! insira um valor")

 elif opcao == "s":
      valor =float(input("informe valor de saque!"))
    
      excedeu_saldo = valor > saldo
      excedeu_limite = valor > limite
      excedeu_saques = numeros_saques >LIMITE_SAQUES
     
      if excedeu_saldo:
        print("operação invalida!você não possui esse saldo em conta")
      if excedeu_limite:
        print("operação invalida!valor excedeu limite")
      if excedeu_saques:
        print("operação invalida!voçê ultrapassou o limite de saques diarios")
      elif valor > 0:
         valor -= saldo
         extrato +=f"Saque:R${valor:.2f}\n"
         numeros_saques += 1
      else: 
         print("Operação falhou! O valor informado é inválido.")

 elif opcao == "e":
         print("\n================ EXTRATO ================")
         print("Não foram realizadas movimentações." if not extrato else extrato)
         print(f"\nSaldo: R$ {saldo:.2f}")
         print("==========================================")

 elif opcao == "q":
  break

 else :
    print("Operação inválida, por favor selecione novamente a operação desejada.")