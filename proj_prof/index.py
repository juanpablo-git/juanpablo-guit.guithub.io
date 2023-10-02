import tkinter as tk
import re
conteudo = ""

 
replace_palavras = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\|]'
with open("palavroes.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.split("\n")
    for k,c in enumerate(conteudo):
        conteudo[k] = c.split(",")

   
def analisa_palavras(palavra):

    for key,palavras_iten in enumerate(conteudo):
        if len(palavras_iten) == 2:
            if palavras_iten[0] == re.sub(replace_palavras,"",palavra).capitalize():
                return palavras_iten[1].capitalize()

            

        else: 
            if palavras_iten[0] == re.sub(replace_palavras,"",palavra).capitalize():
                return  "*"*len(palavras_iten[0]) 
            

def teste(*args):
    print(args[0].keysym  )
    
    if args[0].keysym not in ["Left","Right","Up","Down","Control_L"]:
        total_palavras = campo_texto.get("1.0", "end-1c")
        total_palavras = total_palavras.split(" ")
        for key,palavra  in enumerate(total_palavras):
            palavra_analisada = analisa_palavras(palavra=palavra)
            if  palavra_analisada :
                total_palavras[key] = palavra_analisada
        total_palavras = " ".join(total_palavras)
        campo_texto.delete("1.0", "end-1c")
        campo_texto.insert("1.0",total_palavras)

root = tk.Tk()

root.title("Bloco de palavras")

label = tk.Label(root,text="Digite aqui qualquer coisa:")
label.grid(row=1,column=1)

# Crie um campo de texto
campo_texto = tk.Text(root, wrap="word")
campo_texto.grid(row=6,column=1)

# Vincule o evento de pressionamento de tecla (KeyRelease) ao campo de texto
campo_texto.bind("<KeyRelease>", teste)



root.mainloop()

