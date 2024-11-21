
def wypiszKartke(paper):
    for i in range(len(paper)):
        for j in range(15):
            print(paper[i][j], end="")
        print("")

print("Program imitujący narzedzie kubelka z painta.")
print(" ")
print("Komendy wpisywania do kartki: ")
print("- x - pole zamalowane.")
print("- skip lub s - omija obecna linijke")
print("- line lub l- zamalowuje wszystkie pola w danej linijce")
#print("- del - usuwa ostania akcje")
print("- kazdy inny znak spowoduje ominiecie obecnego pola")
print(" ")
print("Enter aby kontynuowac.")
n = input()

#Tworzymy nasza kartke
paper = [["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]] 
for i in range(1, 9):
    paper.append(["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"])
paper.append(["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"])
for i in range(1, 9):
    for j in range(1,14):
        paper[i][j] = "?"
        wypiszKartke(paper)
        z =input("Podaj znak: ")
        if(z == 'x'):
            paper[i][j] = "x"
        elif(z == 'skip' or z =='s'):
            paper[i][j] = " "
            break
        elif(z == 'line' or z == 'l'):
            paper[i] = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
            break
        else:
            paper[i][j] = " "
        ''' #Funkcja del wymaga zmiany petli for na while
        elif(z == 'del'):
            if(j == 1 and i > 1):
                paper[i][j] = " "
                j = 13
                i = i-1
                paper[i][j] = " "
            elif(j > 1):
                paper[i][j] = " "
                j = j-1
                paper[i][j] = " "
        '''
        
wypiszKartke(paper)
maxHeight = 8 
maxWide = 13

def kubelek(paper, i, j):
    if(i - 1  >= 1 and i - 1 <= maxHeight):
        if(paper[i - 1][j] == " "):
            paper[i - 1][j] = "O"
            wypiszKartke(paper)  
            kubelek(paper, i -1, j)
    if(j - 1  >= 1 and j - 1 <= maxWide):
        if(paper[i][j - 1] == " "):
            paper[i][j - 1] = "O"
            wypiszKartke(paper)  
            kubelek(paper, i, j -1)
    if(i + 1  >= 1 and i + 1 <= maxHeight):
        if(paper[i + 1][j] == " "):
            paper[i + 1][j] = "O"
            wypiszKartke(paper)  
            kubelek(paper, i +1, j)
    if(j + 1  >= 1 and j + 1 <= maxWide):
        if(paper[i][j + 1] == " "):
            paper[i][j + 1] = "O"
            wypiszKartke(paper)  
            kubelek(paper, i, j +1)
print("Liczba kolumny musi miescic sie mieszy 1 a 8, natomiasta liczba wiersza miedzy 1 a 13")
while True: 
    i = input("Podaj kolumne pola ktore chcesz zamalowac: ")
    j = input("Podaj wiersz pola ktore chcesz zamalowac: ")
    if i.isnumeric() == True and j.isnumeric() == True:
        i = int(i)
        j = int(j)
        if(i >= 1 and i <= 8 and j >=1 and j <=13):
            break
        else:
            print("Liczba kolumny musi miescic sie mieszy 1 a 8, natomiasta liczba wiersza miedzy 1 a 13")
    else:
        print("Prosze wprowadzic liczbe")
kubelek(paper, i, j)
print(" ")
wypiszKartke(paper)
print("Nacisnij Enter aby zamknac.")
input("")        
