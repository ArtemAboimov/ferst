D2 = ["Lera","Maks","Artem","Daniil","Pasha"]
D2.append(Nina)
Days = {
"Mondey": ["Maths",]
,"Tuesday": ["Maths",]
,"Wednesday": ["Maths",]
,"Thursday": ["Maths",]
,"Friday": ["Maths",]
}
def delete_class(): 
    global D2
    for i in D2: 
        print(i,end=", ")
    print()
    print("выбири кого удалить: ")
    name = input("-")
    if name in D2: 
        D2.remove(name)
        print("удален",name)
    else:
        print("Таково нет!")

delete_class()

























































