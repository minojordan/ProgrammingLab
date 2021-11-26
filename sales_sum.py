def somma_valori(input_file):
    values=[]
    somma = 0
    my_file = open(input_file ,'r')
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            dates = elements[0] 
            value = elements[1]
            values.append(float(value))
            somma += float(elements[1]) #Mi assicuro che l'elemento sommato sia un numero e non una stringa

    #Una volta uscita dal ciclo for chiudo il fime
    my_file.close()
    print("Somma : {}".format(somma))
    return somma

somma_valori("shampoo_sales.txt") #l'argomento chiamato dalla funzione deve essere direttamente una stringa



