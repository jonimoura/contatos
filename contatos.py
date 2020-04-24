import sqlite3
import time
import os
import winsound

class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""

    def add(self):
        running = True
        while running :
            os.system("cls")
            print("______Adicione um novo contato________")
            print("Pressione a tecla Shift + Q para cancelar")
            print()

           
            temp_name = input("Name: ")
            if len(temp_name) != 0 and temp_name != "Q".upper():
                db = sqlite3.connect("connection")
                cursor = db.cursor()
                cursor.execute("SELECT name FROM contacts")
                results = cursor.fetchall()
                for i in results:
                    if temp_name in i:
                        print("Este contato já existe")
                        time.sleep(2)
                        self.add()
                self.name = temp_name
                temp_name = ""

                time.sleep(0.2)
                self.phone = input("Telefone :") 
                time.sleep(0.2)    
                self.address = input("Endereço :")

                cursor.execute(""" INSERT INTO  contacts\
                                (Name, Phone, Address) VALUES(?,?,?)""",\
                                (self.name, self.phone, self.address))
                db.commit()
                add_more = input("Deseja adicionar outro contato? (y/n): ")
                if add_more == "y".lower():
                    continue
                else:
                    db.close()
                    running = False
                    print("A fechar o menu")
                    time.sleep(2)
                    winsound.Beep(2000,50)
                    self.menu()
            elif temp_name == "Q".upper():
                print("Saindo do menu principal")
                time.sleep(2)
                self.menu()
            else:
                winsound.Beep(3000,100)
                winsound.Beep(3000,100)
                print("Preencher todos os campos")
                time.sleep(1)
                self.add



    def update(self):
        print("_________Atualizar cdastros__________")
        print()
        name= input("Digite o nome do cliente para atualizar: ")
        time.sleep(1)
        confirm = input("Tem certeza? (Y/N): ")
        if confirm == "y".lower():
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            phone_update = input("Atualizar telefone? (Y/N): ")
            if phone_update == "y".lower():
                phone = input("Digite o número de telefone: ")
                cursor.execute("UPDATE contacts SET Phone= ? WHERE Name = ?",(phone, name))
                db.commit
                print("Cadastro atualizado com sucesso")
                time.sleep(3)
            address_update = input("Atualizar endereço? (Y/N): ")
            if address_update == "y".lower():
                address = input("Digite o endereço: ")
                cursor.execute("UPDATE contacts SET Address= ? WHERE Name = ?",(address, name))
                db.commit
                time.sleep(3)

            if phone_update != "y".lower() and address_update != "y".lower():
                print("Voltando ao menu sem fazer atualizações")
                time.sleep(2)
                self.menu()
            print("Endereço atualizado com sucesso")
            db.close()
            self.menu()
        else:
            print("Voltando ao menu sem fazer atualizações")
            time.sleep(2)
            self.menu()

    def remove(self):
        print("_________Deletar Cadastros__________")
        print()
        name= input("Digite o nome do cliente para deletar: ")
        time.sleep(1)
        confirm = input("Tem certeza? (Y/N): ")
        if confirm == "y".lower():
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute("DELETE FROM contacts WHERE Name= ?", (name,))
            db.commit
            print("Cadastro deletado com sucesso")
            time.sleep(3)
            self.menu()
        else:
            print("Saindo do menu principal")
            time.sleep(1)
            self.menu()

    
    def get_list(self):
        count = 0
        count_2 = 0
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        os.system("cls")
        print("_______Contatos________")
        
        time.sleep(0.50)
        cursor.execute("SELECT Name, Phone, Address FROM contacts")
        results = cursor.fetchall()
        for row in results:
            time.sleep(0.50)
            count += 1
            count_2 += 1
            print(count_2, row)
            if count == 5:
                count = 0
                
        print()
        print("Final dos resultados")
            
        option = input("Aperte (A) para atualizar, (D) para Deletar, (M) para Menu: ")
        if option == "a".lower():
            self.update()
        elif option == "d".lower():
            self.remove()
        elif option == "m".lower():
            self.menu()
            

        time.sleep(0.100)

    def terminate(self):
        confirm = input("Deseja realmente sair do sistema? (Y/N):")
        if confirm == "y".lower():
            print("Saindo do sistema")
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            winsound.Beep(3000,50)
            time.sleep(0.5)
            print("-")
            time.sleep(0.02)
            print("--")
            time.sleep(0.02)
            print("---")
            time.sleep(0.02)
            print("-----")
            time.sleep(0.02)
            print("-------")
            time.sleep(0.02)
            print("---------")
            time.sleep(0.02)
            print("-----------")
            time.sleep(0.02)
            print("------------")
            time.sleep(0.02)
            print("**********hmm kk bjs*********")
            exit()
        else:
            print("Retornando ao menu principal")
            time.sleep(0.05)
            self.menu

    def menu(self):
        os.system("cls")
        winsound.Beep(2000, 50)
        print("________________MENU________________")

        time.sleep(0.05)
        print("1  :) Adicionar")
        time.sleep(0.05)
        
        print("2  :) Remover")
        time.sleep(0.05)

        print("3  :) Atualizar")
        time.sleep(0.05)

        print("4  :) Listar")
        time.sleep(0.05)

        print("5  :) Finalizar")

        option = input("Selecione uma ação :")
        if option == "1":
            self.add()

        elif option== "2":
            self.remove()

        elif option== "3":
            self.update()

        elif option== "4":
            self.get_list()

        elif option== "5":
            self.terminate()
        
        else:
            winsound.Beep(2500,100)
            print("Error, Try again the options 1-5")
            time.sleep(2)
            self.menu()

        

    def main(self):
        os.system("cls")
        if os.path.isfile("connection"):
            db= sqlite3.connect("connection")
            time.sleep(3)
            winsound.Beep(2000,50)
            print()
            print("Conectado ao banco de dados")
            time.sleep(3)

        else:
            print("Esta Conexão não existe")
            print()
            time.sleep(3)
            winsound.Beep(2000,50)

            print("Criando nova conexão com o banco de dados")
            time.sleep(3)
            db= sqlite3.connect("connection")

            cursor = db.cursor()
            cursor.execute(""" CREATE TABLE contacts
                            (Name TEXT, Phone TEXT, Address TEXT)""")



            winsound.Beep(2000,50)
            print()
            print("Conexão criada com sucesso")
            print("Conectado com sucesso")
            time.sleep(3)
            self.menu()


        self.menu()

contacts_manager = Manager()
contacts_manager.main()

      

    
    