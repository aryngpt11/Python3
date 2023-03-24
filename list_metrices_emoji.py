r1=["😘","🥰","😍"]
r2=["😁","😀","😂"]
r3=["😉","😊","😎"]
map=[r1,r2,r3]
print(f"{r1}\n{r2}\n{r3}") 
position=input("Where o you want to put the treasure? ")
row=int(position[0])
column=int(position[1])
map[column-1][row-1]="ARYAN"
print(f"{r1}\n{r2}\n{r3}") 