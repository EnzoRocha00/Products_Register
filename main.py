import sqlite3
import os

# Limpar tela OK
def Clear():
    input('Digite qualquer tecla...')
    os.system('cls')

# Listar estoque OK
def listar_Estoque(db):
    cont=0
    for _ in db.execute("SELECT * FROM estoque"):
        cont+=1
    if cont != 0:
        print('Estoque'.center(25))
        print('------------------------')
        print('id   nome   qtd   preço')
        print('------------------------')
        for n, row in enumerate(db.execute("SELECT * FROM estoque")):
            print(str(n+1)+'    '+str(row[0])+'   '+str(row[1])+'   '+str(f'{row[2]:.2f}'))
        print('------------------------')
    else:
        print('------------------------')
        print('Estoque Vazio'.center(25))
        print('------------------------')
             
# Adicionar item OK
def adicionar_Item(db):
    try: 
        item = [str(input('Nome: ')), int(input('Quantidade: ')), float(input('Preço: '))]
        db.execute(
        f'''
            INSERT INTO estoque VALUES
                ('{item[0]}', {item[1]}, {item[2]})
        '''
        )
        item.clear()
    except:
        print('Algo deu errado... Operação cancelada...')
         
# Remover item OK
def remover_Item(db):
    listar_Estoque(db)
    try:
        infoId = int(input('Digite o ID do item a ser removido: '))
        for n, row in enumerate(db.execute("SELECT * FROM estoque")):
            if (n+1) == infoId: 
                db.execute(f'''
                    DELETE FROM estoque WHERE nome = '{row[0]}';
                ''')
    except:
        print('Algo deu errado... Operação cancelada...')

# Atualizar item OK
def atualizar_Item(db):
    listar_Estoque(db)
    try:
        infoId = int(input('Digite o ID do item a ser editado: '))
        for n, row in enumerate(db.execute("SELECT * FROM estoque")):
            if (n+1) == infoId: 
                print('1 - Nome\n2 - Quantidade\n 3 - Preço\n')
                opcChange = int(input('Digite: '))
                if opcChange == 1:
                    new = str(input('Novo nome: '))
                    db.execute(f'''
                        UPDATE estoque SET nome = '{new}' WHERE nome = '{row[0]}'
                    ''')
                elif opcChange == 2:
                    new = int(input('Nova quantidade: '))
                    db.execute(f'''
                        UPDATE estoque SET quantidade = {new} WHERE nome = '{row[0]}'
                    ''')
                elif opcChange == 3:
                    new = float(input('Novo preço: '))
                    db.execute(f'''
                        UPDATE estoque SET preco = {new} WHERE nome = '{row[0]}'
                    ''')
                else:
                    pass
    except:
        print('Algo deu errado...')

# Realizar compra ?
def realizar_Compra():
    return True

# Mostra menu OK
def showMenu():
    print('-'*25)
    print('Menu'.center(25))
    print('-'*25, end='')
    print('''
0 - Sair
1 - Listar estoque
2 - Adicionar item
3 - Remover item
4 - Atualizar item
5 - Realizar compra
''')
    print('-'*25)
    try:
        opc = int(input('Opção: '))
        return opc
    except: 
        print('Algo deu errado... Digite uma opção válida')
        return 999

if __name__ == '__main__':
    os.system('cls')
    run = True
    connection = sqlite3.connect("dados.db")
    cursor = connection.cursor()

    exist = cursor.execute("SELECT name FROM sqlite_master WHERE name='estoque'")

    if exist.fetchone() is None:
        cursor.execute("CREATE TABLE estoque(nome, quantidade, preco)")
        
    connection.commit()
    while run:
        match(showMenu()):
            case 0:
                run = False
                connection.close()
                print('Encerrando...')
                break
            case 1:
                listar_Estoque(cursor)
            case 2:
                adicionar_Item(cursor)  
            case 3:
                remover_Item(cursor)
            case 4:
                atualizar_Item(cursor)
            case _ :
                pass
                
        connection.commit()   
        Clear()       