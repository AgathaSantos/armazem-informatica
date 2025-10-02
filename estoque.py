from datetime import datetime
 
 
estoque = [
    {
        "codigo": 101,
        "descricao": "Mouse",
        "quantidade": 50,
        "valor_unitario": 120.00,
        "data_movimentacao": "15/09/2025"
    },
    {
        "codigo": 102,
        "descricao": "Teclado",
        "quantidade": 30,
        "valor_unitario": 350.00,
        "data_movimentacao": "18/09/2025"
    },
    {
        "codigo": 103,
        "descricao": "Monitor",
        "quantidade": 15,
        "valor_unitario": 1200.00,
        "data_movimentacao": "20/09/2025"
    },
    {
        "codigo": 104,
        "descricao": "Headset",
        "quantidade": 45,
        "valor_unitario": 220.00,
        "data_movimentacao": "21/09/2025"
    },
    {
        "codigo": 105,
        "descricao": "Webcam",
        "quantidade": 60,
        "valor_unitario": 150.00,
        "data_movimentacao": "19/09/2025"
    }
]
 
 
def exibir_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    for item in estoque:
        valor_total = item['quantidade'] * item['valor_unitario']
        print(f"Código: {item['codigo']}")
        print(f"Descrição: {item['descricao']}")
        print(f"Quantidade: {item['quantidade']}")
        print(f"Valor Unitário: R$ {item['valor_unitario']:.2f}")
        print(f"Valor Total: R$ {valor_total:.2f}")
        print(f"Última Movimentação: {item['data_movimentacao']}")
        print("-" * 30)
 
 
def adicionar_produto():
    print("\n--- ADICIONAR NOVO PRODUTO ---")
    try:
        codigo = int(input("Código do produto: "))
        
        if any(p['codigo'] == codigo for p in estoque):
            print(" Código já existente no estoque!")
            return
        descricao = input("Descrição: ")
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: R$ "))
        data_hoje = datetime.today().strftime('%d/%m/%Y')
 
 
        novo = {
            "codigo": codigo,
            "descricao": descricao,
            "quantidade": quantidade,
            "valor_unitario": valor_unitario,
            "data_movimentacao": data_hoje
        }
 
 
        estoque.append(novo)
        print(" Produto adicionado com sucesso!")
    except ValueError:
        print("Entrada inválida. Tente novamente.")
 
 
def movimentar_estoque():
    print("\n--- MOVIMENTAR ESTOQUE ---")
    try:
        codigo = int(input("Digite o código do produto: "))
        produto = next((p for p in estoque if p['codigo'] == codigo), None)
        if not produto:
            print(" Produto não encontrado.")
            return
 
 
        print(f"Produto: {produto['descricao']}")
        print(f"Quantidade atual: {produto['quantidade']}")
 
 
        quantidade = int(input("Digite a quantidade (+ para entrada, - para saída): "))
        nova_quantidade = produto['quantidade'] + quantidade
 
 
        if nova_quantidade < 0:
            print(" Estoque insuficiente para essa retirada.")
            return
 
 
        produto['quantidade'] = nova_quantidade
        produto['data_movimentacao'] = datetime.today().strftime('%d/%m/%Y')
        print(" Estoque atualizado com sucesso!")
 
 
    except ValueError:
        print(" Entrada inválida. Tente novamente.")
 
 
# Menu do sistema
def menu():
    while True:
        print("\n===== ARMAZÉM DA INFORMÁTICA =====")
        print("1. Exibir estoque")
        print("2. Adicionar produto")
        print("3. Movimentar estoque")
        print("4. Sair")
 
 
        opcao = input("Escolha uma opção: ")
 
 
        if opcao == "1":
            exibir_estoque()
        elif opcao == "2":
            adicionar_produto()
        elif opcao == "3":
            movimentar_estoque()
        elif opcao == "4":
            print(" Encerrando o sistema.")
            break
        else:
            print(" Opção inválida.")
 
 
 
menu()
