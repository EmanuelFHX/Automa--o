# passo 1
import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o navegador (edge)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa no código
time.sleep(3)

# passo 2
pyautogui.click(x=544, y=387)
pyautogui.write("pythonbom@gmail.com")

# escrever senha
pyautogui.press("tab")
pyautogui.write("soumuitogostoso")

# clicar no botão de logar
pyautogui.click(x=659, y=558)
time.sleep(3)


# passo 3
import pandas
tabela = pandas.read_csv("produtos.csv")


# passo 4
for linha in tabela.index:


    pyautogui.click(x=428, y=279)

    # codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    #str()
    #str() string -> texto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# passo 5



