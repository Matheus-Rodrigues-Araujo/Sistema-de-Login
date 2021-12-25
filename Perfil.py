def seu_perfil(email):
    import tkinter as tk
    import mysql.connector
    con = mysql.connector.connect(host="localhost",user="root",password="",database="usuarios")
    # con = mysql.connector.connect(host="localhost",user="root",password="matheus.rodrigues.araujo.083",database="usuarios")
    cursor = con.cursor()
    root = tk.Tk()
    root.geometry('500x220+450+100')
    root.title('After Login')
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    root['background'] = '#222222'
    info = tk.Label(root, text='Perfil', bg='#114488', fg='white', font=('Heveltica', 20))
    info.grid(ipadx=200, columnspan=2, row=0, ipady=8)

    cursor.execute(f"select * from informacoes where email = '{email}' ")
	# cursor.execute("select * from user_information where username ='"+ email.get() + "'")
    dados = cursor.fetchall()

    for dado in dados:
        boas_vindas = tk.Label(root, text=f"Bem-vindo(a) {dado[1]}", font=('Heveltica', 12), bg='#222222', fg='white')
        boas_vindas.grid(column=0, row=2, sticky=tk.W, padx=10)

        ver_perfil = tk.Button(root, text=f"Informacoes", font=('Heveltica', 15), bg='#114488', fg='white')
        ver_perfil.grid(column=0, row=3, sticky=tk.W, pady=10, padx=10)

        agendar = tk.Button(root, text=f"Agendar viagem", font=('Heveltica', 15), bg='#114488', fg='white')
        agendar.grid(column=1, row=3, sticky=tk.E, pady=10, padx=10)

        atualizar = tk.Button(root, text=f"Atualizar dados", font=('Heveltica', 15), bg='#114488', fg='white')
        atualizar.grid(column=0, row=4, sticky=tk.W, pady=10, padx=10)

        viagens = tk.Button(root, text=f"Suas viagens", font=('Heveltica', 15), bg='#114488', fg='white')
        viagens.grid(column=1, row=4, sticky=tk.E, pady=10, padx=10)