import customtkinter as ctk 
import sqlite3
import pandas as pd
import openpyxl

def cadastro_cliente():
    conexao = sqlite3.connect('Clientes.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)',
                {
                    'nome':entrynome.get(),
                    'sobrenome':entrysobrenome.get(),
                    'email':entryemail.get(),
                    'telefone':entrytelefone.get()
                }
                )
    conexao.commit()
    conexao.close()

    entrynome.delete(0, 'end')
    entrysobrenome.delete(0, 'end')
    entryemail.delete(0, 'end')
    entrytelefone.delete(0, 'end')

def exportar_cliente():
    conexao = sqlite3.connect('Clientes.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT *, oid FROM clientes')

    clientes_cadastrados = cursor.fetchall()

    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['Nome','Sobrenome', 'Email', 'Tefelone', 'Id_Dados'])

    clientes_cadastrados.to_excel ('Clientes.xlsx')

    conexao.commit()

    conexao.close()




janela = ctk.CTk()
janela.title('Cadastro')
janela.minsize(340, 410)
janela.maxsize(340, 410)

nome = ctk.CTkLabel(janela, text='Nome')
nome.grid(row=0, column=0, padx=20, pady=20)

entrynome = ctk.CTkEntry(janela, placeholder_text='Nome', width=200)
entrynome.grid(row=0, column=1, padx=20, pady=20)

sobrenome = ctk.CTkLabel(janela, text=('Sobrenome'))
sobrenome.grid(row=1, column=0, padx=20, pady=20)

entrysobrenome = ctk.CTkEntry(janela, placeholder_text='Sobrenome', width=200)
entrysobrenome.grid(row=1, column=1, padx=20, pady=20)

email = ctk.CTkLabel(janela, text='Email')
email.grid(row=2, column=0, padx=20, pady=20)

entryemail = ctk.CTkEntry(janela, placeholder_text='ex: python123@gmail.com', width=200)
entryemail.grid(row=2, column=1, padx=20, pady=20)

telefone = ctk.CTkLabel(janela, text='Telefone')
telefone.grid(row=3, column=0, padx=20, pady=20)

entrytelefone = ctk.CTkEntry(janela, placeholder_text='ex: 00999999999', width=200)
entrytelefone.grid(row=3, column=1, padx=20, pady=20)

botcadastrar = ctk.CTkButton(janela, text='Cadastrar clientes', command=cadastro_cliente)
botcadastrar.grid(row=4, column=0, padx=20, pady=20, columnspan = 2, ipadx = 80)

botexportar = ctk.CTkButton(janela, text='Exportar clientes', command=exportar_cliente)
botexportar.grid(row=5, column=0, padx=20, pady=20, columnspan = 2, ipadx = 80)


janela.mainloop()