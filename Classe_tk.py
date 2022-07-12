from tkinter import *
import posiciona
#======================================================================================================================
#Janela
janela = Tk()
janela.bind('<Button-1>', posiciona.inicio_place)
janela.bind('<ButtonRelease-1>', lambda arg: posiciona.fim_place(arg,janela))
janela.bind('<Button-2>', lambda arg: posiciona.para_geometry(janela))
janela.geometry('800x500')
#======================================================================================================================
#Todas as cores
red = '#E01E37'
white = '#FFFFFF'
black = '#000000'
Dark_Blue = '#0B1B2A'
#======================================================================================================================
#Todos os frames
frame_principal = Frame(janela)
frame_bemvindo = Frame(janela)
frame_telaopcoes = Frame(janela)
frame_cadastrofabri = Frame(janela)
frame_opcoespro = Frame(janela)
frame_cadastropro = Frame(janela)
frame_alterarpro = Frame(janela)
frame_comprar = Frame(janela)
frame_venda = Frame(janela)
frame_listar = Frame(janela)
#======================================================================================================================
#Frames principais
frame_principal.pack()
frame_bemvindo.pack()
#======================================================================================================================
#Todas as Fotos usadas
img_principal = PhotoImage(file='Fotos/Pagina principal.png')
img_bemvindo = PhotoImage(file='Fotos/bem vindo.png')
img_telaopcoes = PhotoImage(file='Fotos/tela de opções.png')
img_cadastrofabri = PhotoImage(file='Fotos/cadastro_fabri.png')
img_opcoespro = PhotoImage(file='Fotos/Opções_produtos.png')
img_cadastropro = PhotoImage(file='Fotos/cadastro_produtos.png')
img_alterarpro = PhotoImage(file='Fotos/alterar_produto.png')
img_comprar = PhotoImage(file='Fotos/Comprar.png')
img_venda = PhotoImage(file='Fotos/Venda.png')
img_setavoltar = PhotoImage(file='Fotos/seta voltar.png')
img_listar = PhotoImage(file='Fotos/listar.png')
#======================================================================================================================
#Primeirp Frame (Controle de estoque)
lb_principal = Label(frame_principal, image=img_principal, border=0)
lb_principal.pack()

#======================================================================================================================
#Segundo Frame (Bem-vindo)
#labels e pack
lb_bemvindo = Label(frame_bemvindo, image=img_bemvindo, border=0)
lb_bemvindo.pack()
#buttons
bt_fabri = Button(frame_bemvindo, text='Fabricantes', bg=red, font='Palatino  15 bold', bd=0, fg=white,activebackground=red,activeforeground=white,
                  command=lambda:[frame_telaopcoes.pack(), frame_bemvindo.forget()])
bt_pro = Button(frame_bemvindo, text='Produtos', bg=white, font='Palatino 15 bold', bd=0, fg=black,activebackground=white,
                command=lambda:[frame_opcoespro.pack(),frame_bemvindo.forget()])
bt_listar = Button(frame_bemvindo, text='Listar', bg=red, font='Palatino 15 bold', bd=0, fg=white,activebackground=red,activeforeground=white,
                   command=lambda:[frame_listar.pack(),frame_bemvindo.forget()])
bt_encerrar = Button(frame_bemvindo, text='Encerrar', bg=white, font='Palatino 15 bold', bd=0, fg=black,activebackground=white,
                     command= lambda:janela.destroy())
#places
bt_fabri.place(width=187, height=44, x=142, y=152)
bt_pro.place(width=191, height=48, x=141, y=230)
bt_listar.place(width=194, height=45, x=137, y=311)
bt_encerrar.place(width=194, height=48, x=137, y=387)
#======================================================================================================================
#Terceiro Frame (opções do Fabricante)
#labels e pack
lb_telaopcoes = Label(frame_telaopcoes, image=img_telaopcoes, border=0)
lb_telaopcoes.pack()
#buttons
bt_cadastrarfabri = Button(frame_telaopcoes, text='Cadastrar Fabricante', bg=red, font='Palatino 13 bold', bd=0, fg=white,activebackground=red,activeforeground=white,
                           command=lambda:[frame_cadastrofabri.pack(), frame_telaopcoes.forget()])
bt_jatenhofabri = Button(frame_telaopcoes, text='Ja tenho Fabricante', bg=white, font='Palatino 13 bold', bd=0, fg=black,activebackground=white,
                         command=lambda:[frame_bemvindo.pack(), frame_telaopcoes.forget()])
#places
bt_cadastrarfabri.place(width=194, height=48, x=144, y=176)
bt_jatenhofabri.place(width=198, height=47, x=140, y=297)
#======================================================================================================================
#Quarto Frame (Cadastro do Fabricante)
#labels e pack
lb_cadastrofabri = Label(frame_cadastrofabri, image=img_cadastrofabri, border=0)
lb_cadastrofabri.pack()
#Entry
en_cadaFabri = Entry(frame_cadastrofabri, font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
#Buttons
bt_confirma = Button(frame_cadastrofabri,text='Confirmar', font='Palatino 15 bold', bd=0, bg=red, fg=white,activebackground=red,activeforeground=white)
bt_setavoltar = Button(frame_cadastrofabri, image=img_setavoltar,bd=0,command=lambda:[frame_telaopcoes.pack(),frame_cadastrofabri.forget()])
#Places
bt_setavoltar.place(width=33, height=37, x=10, y=11)
bt_confirma.place(width=195, height=49, x=164, y=343)
en_cadaFabri.place(width=323, height=25, x=78, y=214)
#======================================================================================================================
#Quinto Frame (Opções do Produto)
#Labels e Pack
lb_opcoespro = Label(frame_opcoespro,image=img_opcoespro, bd=0)
lb_opcoespro.pack()
#Buttons
bt_Cadapro = Button(frame_opcoespro,text='Cadastrar Produto', font='Palatino 13 bold', bd=0,bg=red,fg=white,activebackground=red,activeforeground=white,
                    command=lambda:[frame_cadastropro.pack(), frame_opcoespro.forget()])
bt_alterpro = Button(frame_opcoespro,text='Alterar Nome', font='Palatino 13 bold', bd=0,bg=white,fg=black,activeforeground=white,
                     command=lambda:[frame_alterarpro.pack(),frame_opcoespro.forget()])
bt_Compra = Button(frame_opcoespro,text='Comprar', font='Palatino 13 bold', bd=0,bg=red,fg=white,activebackground=red,activeforeground=white,
                   command=lambda:[frame_comprar.pack(),frame_opcoespro.forget()])
bt_Venda = Button(frame_opcoespro,text='Vender', font='Palatino 13 bold', bd=0,bg=white,fg=black,activeforeground=white,
                  command=lambda:[frame_venda.pack(),frame_opcoespro.forget()])
bt_setavoltar = Button(frame_opcoespro, image=img_setavoltar,bd=0,command=lambda:[frame_bemvindo.pack(), frame_opcoespro.forget()])
#Places
bt_Cadapro.place(width=200, height=46, x=126, y=107)
bt_alterpro.place(width=183, height=39, x=135, y=193)
bt_Compra.place(width=196, height=48, x=128, y=270)
bt_Venda.place(width=190, height=42, x=131, y=355)
bt_setavoltar.place(width=36, height=39, x=10, y=9)
#======================================================================================================================
#Sexto Frame (Cadastro do Produto)
#Labels e Pack
lb_cadastropro = Label(frame_cadastropro,image=img_cadastropro, bd=0)
lb_cadastropro.pack()
#Entrys
en_Codpro = Entry(frame_cadastropro,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
en_Desc = Entry(frame_cadastropro,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
en_quant = Entry(frame_cadastropro,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
en_codFabri = Entry(frame_cadastropro,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
#Buttons
bt_confirma = Button(frame_cadastropro,text='Confirmar', font='Palatino 15 bold', bd=0, bg=red, fg=white,activebackground=red,activeforeground=white)
bt_setavoltar = Button(frame_cadastropro, image=img_setavoltar,bd=0,command=lambda:[frame_opcoespro.pack(),frame_cadastropro.forget()])
#Places
en_Codpro.place(width=326, height=21, x=77, y=183)
en_Desc.place(width=327, height=29, x=77, y=305)
en_quant.place(width=325, height=27, x=444, y=305)
en_codFabri.place(width=327, height=19, x=444, y=182)
bt_confirma.place(width=190, height=46, x=528, y=416)
bt_setavoltar.place(width=35, height=38, x=10, y=9)
#======================================================================================================================
#Sétimo Frame (Alterar o Produto)
#Labels e Pack
lb_alterpro = Label(frame_alterarpro,image=img_alterarpro,bd=0)
lb_alterpro.pack()
#Button
bt_confirma = Button(frame_alterarpro,text='Confirmar', font='Palatino 15 bold', bd=0, bg=red, fg=white,activebackground=red,activeforeground=white)
bt_setavoltar = Button(frame_alterarpro, image=img_setavoltar,bd=0,command=lambda:[frame_opcoespro.pack(), frame_alterarpro.forget()])
#Entry
en_Codpro = Entry(frame_alterarpro,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
en_Novo_nome = Entry(frame_alterarpro,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
#Places
en_Codpro.place(width=326, height=24, x=79, y=180)
en_Novo_nome.place(width=325, height=21, x=79, y=307)
bt_confirma.place(width=195, height=41, x=152, y=412)
bt_setavoltar.place(width=36, height=38, x=10, y=9)
#======================================================================================================================
#Oitavo Frame (Comprar o Produto)
#Labels e Pack
lb_comprar = Label(frame_comprar,image=img_comprar,bd=0)
lb_comprar.pack()
#Buttons
bt_confirma = Button(frame_comprar,text='Confirmar', font='Palatino 15 bold', bd=0, bg=red, fg=white,activebackground=red,activeforeground=white)
bt_setavoltar = Button(frame_comprar, image=img_setavoltar,bd=0,command=lambda:[frame_opcoespro.pack(),frame_comprar.forget()])
#Entrys
en_Codpro = Entry(frame_comprar,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
en_Nova_quant = Entry(frame_comprar,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
#Places
bt_confirma.place(width=191, height=45, x=155, y=410)
bt_setavoltar.place(width=36, height=39, x=10, y=9)
en_Codpro.place(width=327, height=18, x=76, y=184)
en_Nova_quant.place(width=329, height=31, x=77, y=302)
#======================================================================================================================
#Nono Frame (Vender o Produto)
#Labels e Pack
lb_vender = Label(frame_venda,image=img_venda,bd=0)
lb_vender.pack()
#buttons
bt_confirma = Button(frame_venda,text='Confirmar', font='Palatino 15 bold', bd=0, bg=red, fg=white,activebackground=red,activeforeground=white)
bt_setavoltar = Button(frame_venda, image=img_setavoltar,bd=0,command=lambda:[frame_opcoespro.pack(),frame_venda.forget()])
#entrys
en_Codpro = Entry(frame_venda,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
en_Nova_quant = Entry(frame_venda,font='Palatino 15 bold', bd=0, bg=Dark_Blue, fg=white)
#places
en_Codpro.place(width=327, height=23, x=78, y=183)
en_Nova_quant.place(width=326, height=22, x=76, y=309)
bt_confirma.place(width=198, height=43, x=150, y=411)
bt_setavoltar.place(width=36, height=40, x=10, y=8)
#======================================================================================================================
#Décima Frame (Listar Todos)
#Labels e Pack
lb_listar = Label(frame_listar,image=img_listar,bd=0)
lb_listar.pack()
#Button
bt_setavoltar = Button(frame_listar, image=img_setavoltar,bd=0,command=lambda:[frame_bemvindo.pack(),frame_listar.forget()])
#places
bt_setavoltar.place(width=36, height=40, x=10, y=8)
#======================================================================================================================
#Temporizador da tela principal e executa a janela
janela.after(1000,frame_principal.forget)
janela.mainloop()