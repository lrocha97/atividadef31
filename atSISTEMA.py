usuarios = [{
     'LOGIN': 'adm', 'EMAIL': 'adm@adm.com', 'SENHA': '123',
}]
estoque = [{
     'Produto': 'Camiseta', 'Quantidade': 50, 'Valor': 25}, {'Produto': 'Arroz', 'Quantidade': 20, 'Valor': 27}]
carrinho = []
historico = []

def adicionar_user():
     p = {}
     print("Vamos dar inicio ao Cadastro :) ")
     p["LOGIN"] = input("Digite um nome de Usuário: ")
     p["EMAIL"] = input("Digite um E-MAIL válido: ")
     p["SENHA"] = input("Digite uma senha com 6 caracteres: ")
     usuarios.append(p)
     print("Conta criada com Sucesso!")

def adicionar_prod():
        p = {}
        print('Adicione um produto:')
        p["Produto"] = (input('Digite o Nome do Produto: '))
        p["Quantidade"] = (int(input('Digite a quantidade do Produto: ')))
        p["Valor"] = int(input('Digite o valor do produto: '))
        estoque.append(p)
        

def atualizar_est():
        print("Atualize um produto: ")
        at = input("Deseja atualizar ou remover?")
        if at == 'adicionar':
            for i in range(len(estoque)):
                  print(f"Selecione o produto {i+1}")
                  entrada = int(input("Digite a quantidade que irá entrar: "))
                  i["Quantidade"] += entrada
        if at == 'remover':
              for i in range(len(estoque)):
                  print(f"Selecione o produto {i+1}")
                  saida = int(input("Digite a quantidade que irá sair: "))
                  i["Quantidade"] += saida
                        
def consulta():
     print(estoque)


def ad_carrinho():
    p = {}
    print(estoque)
    a = input("Digite o nome do Produto que deseja: ")
    b = int(input("Digite a quantidade de Produto: "))

    for item in estoque:
          if item['Produto'] == a:
              p["Produto"] = a
              p['Quantidade'] = b
              p['Valor'] = item['Valor']
              carrinho.append(p)
          else:
               print("produto nao existe")

def visu_carrinho():
     print('Seu carrinho está no valor de R$: ', subtotal())

def remov_carrinho():
     a = input("Qual produto deseja retirar? ")
     if a in carrinho:
          carrinho.remove(a)
     else:
          print("Produto não está no carrinho")

def fin_compra():
     a = input("Deseja finalizar a compra? Sim ou Não")
     if a == "Sim":
          b = input("Qual a forma de pagamento?")
          if b == "credito":
                print("Compra Finalizada")
                historico.append(carrinho)
                for item in carrinho:
                     for item2 in estoque:
                         if item['Produto'] == item2['Produto']:
                              item2['Quantidade'] = item2['Quantidade'] - item['Quantidade']

                carrinho.clear()
          elif b == "dinheiro":
                print("Compra Finalizada")
                historico.append(carrinho)
                for item in carrinho:
                     for item2 in estoque:
                         if item['Produto'] == item2['Produto']:
                              item2['Quantidade'] = item2['Quantidade'] - item['Quantidade']
                carrinho.clear()
     else:
          print("Continue a comprar")

def subtotal():
     total = 0
     print(carrinho)
     for item in carrinho:
          total += item['Valor'] * item['Quantidade']
     return total



print('Olá Seja bem vindo ao Mercado Rocha!')
while True:
     a = input("Você já tem Cadastro no sistema? Responda somente com Sim ou Não. ")
     if a == 'Sim' or a == 'sim':
          b = input("Digite seu USUÁRIO: ")
          c = input("Digite seu E-MAIL: ")
          d = input("Digite sua SENHA: ")
          for usuario in usuarios:
               if usuario["LOGIN"] == b and c == usuario["EMAIL"] and d == usuario["SENHA"]:    
                    while True:
                         print(f'Olá {b}, seja bem vindo!!!')   
                         print("Opções do Estoque")
                         print("Opção 1: Adicionar Produto")
                         print("Opção 2: Atualizar Estoque")
                         print("Opção 3: Consultar Estoque")
                         print("Opção 4: Realizar uma Compra")
                         print("Opção 5: Visualizar seu Carrinho de Compras")
                         print("Opção 6: Remover item do Carrinho de Compras")
                         print("Opção 7: Finalizar Compra")
                         print("Opção 8: Listar Estoque")
                         print("Opção 9: Sair")

                         op=int(input("Digite uma opção acima: "))
                         
                         if op == 1:
                              adicionar_prod()

                         if op == 2:
                              atualizar_est()
                              
                         if op == 3:
                              consulta()

                         if op == 4:
                              ad_carrinho()

                         if op == 5:
                              visu_carrinho()

                         if op == 6:
                              remov_carrinho()

                         if op == 7:
                              fin_compra()
  

     else:
          adicionar_user()