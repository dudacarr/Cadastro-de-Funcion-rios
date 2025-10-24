import sqlite3
conn = sqlite3.connect("funcionarios.db")
cursor = conn.cursor()
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL       
)""")
conn.commit()
def adicionar_funcionario(nome, cargo, salario):
    cursor.execute(""
        "INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)",
        (nome, cargo, salario)
    )
    conn.commit()
    print(f"Funcionário {nome} cadastrado com sucesso")
def listar_funcionarios():
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    for funcionario in funcionarios:
        print("Nome: {}, Cargo: {}, Salário: {:.2f}".format(funcionario[1], funcionario[2], funcionario[3]))
def buscar_funcionario(nome):
    cursor.execute("SELECT * FROM funcionarios WHERE nome = ?", (nome,))
    funcionario = cursor.fetchone()
    if funcionario:
        print("Nome: {}, Cargo: {}, Salário: {:.2f}".format(funcionario[1], funcionario[2], funcionario[3]))
    else:
        print("Funcionário não encontrado")
def calcular_media_salarial():
    cursor.execute("SELECT AVG(salario) FROM funcionarios")
    media = cursor.fetchone()[0]
    if media is None:
        print("Média Salarial: 0.00")
    else:
        print("Média Salarial: {:.2f}".format(media))
def fechar_conexao():
    conn.close()

if __name__ == "__main__":
    while True:
        print("\nMenu principal: ")
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Buscar funcionário por nome")
        print("4. Calcular média salarial")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo do funcionário: ")
            try:
                salario = float(input("Salário do funcionário: "))
            except ValueError:
                print("Salário inválido.")
                continue
            adicionar_funcionario(nome, cargo, salario)
        elif escolha == "2":
            listar_funcionarios()
        elif escolha == "3":
            nome = input("Nome do funcionário a buscar: ")
            buscar_funcionario(nome)
        elif escolha == "4":
            calcular_media_salarial()
        elif escolha == "5":
            print("Saindo do programa...")
            fechar_conexao()
            break
        else:
            print("Opção inválida. Tente novamente.")
