import coffe_database

cost_list={
    'Latte':180,
    'Captunio':240,
    'Espresso':210
}

actual={
    'water': 500,
    'coffee': 80,
    'milk': 200,
    'Captunio':40,
    'Espresso':10,
    'Latte':5
}
new_actual=actual

def change_actual(coffe):
    if coffe=='Captunio':
        for i in coffe_database.Captunio:
            new_actual[i]=new_actual[i]-coffe_database.Captunio[i]
    elif coffe=='Espresso':
        for i in coffe_database.Espresso:
            new_actual[i]=new_actual[i]-coffe_database.Espresso[i]
    elif coffe == 'Latte':
        for i in coffe_database.Latte:
            new_actual[i] = new_actual[i] - coffe_database.Latte[i]


def cost(f,t,tw):
    val_five=f*5
    val_ten=t*10
    val_twenty=tw*20
    total=val_ten+val_twenty+val_five
    return total


def resources(type):
    pos=0
    neg=0
    if type=='Latte':
        val=coffe_database.Latte
        for i in val:
            if val[i] <= actual[i]:
                pos+=1
            else:
                neg+=1
        if pos==4:
            return True
        else:
            return False
    elif type=='Captunio':
        val=coffe_database.Captunio
        for i in val:
            if val[i] <= actual[i]:
                pos+=1
            else:
                neg+=1
        if pos==4:
            return True
        else:
            return False
    elif type=='Espresso':
        val=coffe_database.Espresso
        for i in val:
            if val[i] <= actual[i]:
                pos+=1
            else:
                neg+=1
        if pos==4:
            return True
        else:
            return False


def coffe_machine():
    order=input("What would you like to have?(Latte/Espresso/Captunio): ")
    if order=='report' or order=='Report':
        for i in new_actual:
            print(f"i, new_actual[i]")
    elif order=='off':
        exit()
    else:
        available=resources(order)
        if available:
            print("Please insert Coins:")
            five=int(input("How many 5RS. Coins: "))
            ten=int(input("How many 10RS. Coins: "))
            twenty=int(input("How many 20RS. Coins: "))
            total=cost(five,ten,twenty)
            if total==cost_list[order]:
                print(f"Here is your {order}")
                change_actual(order)
            elif total > cost_list[order]:
                change=total-cost_list[order]
                print(f"Here is your Rs.{change} change")
                print(f"Here is your {order}")
                change_actual(order)
            else:
                print(f"Sorry with that money you can't buy {order}")
        else:
            print("Sorry Out of Stock!!..")
            print("So sorry for inconveince!! You can order another one.")
    coffe_machine()
coffe_machine()



