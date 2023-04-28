import sqlite3
import os

# Limpar tela OK
def Clear():
    input('Digite qualquer tecla...')
    os.system('cls')

# Listar estoque OK
def listar_Estoque(db):
    cont=0
    for aux in db.execute("SELECT * FROM estoque"):
        cont+=1
    if cont != 0:
        print('Estoque'.center(25))
        print('------------------------')
        print('id   nome   qtd   preço')
        print('------------------------')
        for row in db.execute("SELECT * FROM estoque ORDER BY id"):
            print(str(row[0])+'    '+str(row[1])+'   '+str(row[2])+'   '+str(f'{row[3]:.2f}'))
        print('------------------------')
    else:
        print('------------------------')
        print('Estoque Vazio'.center(25))
        print('------------------------')
             
# Adicionar item OK
def adicionar_Item(db):
    item = [int(input('ID: ')), str(input('Nome: ')), int(input('Quantidade: ')), float(input('Preço: '))]
    db.execute(
        f'''
            INSERT INTO estoque VALUES
                ({item[0]}, '{item[1]}', {item[2]}, {item[3]})
        '''
    )
    item.clear()
    
# Remover item OK
def remover_Item(db):
    listar_Estoque(db)
    infoId = int(input('Digite o ID do item a ser removido: '))
    db.execute(f'''
    DELETE FROM estoque WHERE id = {infoId};
    ''')

# Atualizar item ?
def atualizar_Item():
    return True

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
5 - Realizar compra''')
    print('-'*25)
    opc = int(input('Opção: '))
    return opc

if __name__ == '__main__':
    os.system('cls')
    run = True
    connection = sqlite3.connect("dados.db")
    cursor = connection.cursor()

    exist = cursor.execute("SELECT name FROM sqlite_master WHERE name='estoque'")

    if exist.fetchone() is None:
        cursor.execute("CREATE TABLE estoque(id, nome, quantidade, preco)")
        
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
            case _ :
                print('Valor inválido...')
                
        connection.commit()   
        Clear()       