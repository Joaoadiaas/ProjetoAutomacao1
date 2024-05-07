import pyautogui
import time
import pandas  as pd

#Entrar no navegador
pyautogui.press("Win")
time.sleep(1)
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=849, y=456)
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=876, y=473)
pyautogui.write("joaoestacolocando@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2) 

#Copiar os dados
tabela = pd.read_csv("produto.csv")

#Automatizar os dados
for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=710, y=323)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)