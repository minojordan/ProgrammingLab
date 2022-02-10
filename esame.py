#prendo datetime da una libreria e la inserisco nel mio codice
from datetime import datetime

#creo una sottoclasse di Exception per l'esame
class ExamException(Exception):
    pass

#creo la classe madre CSVFile
class CSVFile():
    #in questo punto creo una funzione per inizializzare la classe
    def __init__(self,name):
        self.name = name

        #qui controllo che sia una stringa
        if not isinstance(self.name, str):
            raise ExamException('TypeError, il nome del file "{}" non è una stringa'.format(self.name))

    #creo un metodo get_data
    def get_data(self):
        #qui inizializzo la futura lista di liste
        lista_futura = []

        #qui apro il file self.name e in caso di errore alzo un' eccezione
        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException('NotFoundError, il file "{}" non esiste o non è leggibile'.format(self.name))
        
        #scorro ogni riga del file
        for line in my_file:
            #divido gli elementi creando una lista composta da 'data' e 'passeggeri'
            elements = line.split(',')

            #elimino il carattere '\n' dall'elemento passeggeri
            elements[-1] = elements[-1].strip()
       
            #aggiungo ogni elemento della lista nella lista finale, saltando l'intestazione
            if elements[0] != 'date':
                lista_futura.append(elements)

        #chiudo il file e returno la lista di liste
        my_file.close()
        return lista_futura

#creo una sottoclasse di CSVFile
class CSVTimeSeriesFile(CSVFile):
    
    #aggiorno il metodo get_data della classe madre
    def get_data(self):
        lista_prec = super().get_data()
        #inizializzo la lista che conterrà le liste dopo che avranno superato i controlli
        lista_corretta = []
        
        for element in lista_prec:
            #controllo i dati passeggero
            #controllo che siano presenti almeno due dati
            if len(element) < 2:
                #altrimenti li aggiungo come None
                element.append(None)
            
            #controllo che si possano trasformare in un numero intero
            elif not element[1].isdigit():
                element[1] = None
            
            #trasformo tutti i dati accettabili dei passeggeri in numeri interi
            else:
                element[1] = int(element[1])
            
            #controllo che tutti gli element[0] siano delle date nel formato corretto
            try:
                date1 = datetime.strptime(element[0], '%Y-%m')
            except:
                continue
            
            #aggiungo alla nuova lista tutti gli elementi corretti
            lista_corretta.append(element)

        return lista_corretta

def compute_avg_monthly_difference(lista, first_y, last_y):
    #faccio controlli sull'anno iniziale e finale 

    #controllo che siano del formato corretto cioè str
    if not isinstance(first_y, str):
        raise ExamException('TypeError, l\' anno iniziale non è una stringa')
    
    if not isinstance(last_y, str):
        raise ExamException('TypeError, l\' anno finale non è una stringa')

    #controllo le str siano formate da soli numeri
    if not first_y.isdigit():
        raise ExamException('Error, l\' anno iniziale non è un numero intero')
    
    if not last_y.isdigit():
        raise ExamException('Error, l\' anno finale non è un numero intero')

    #trasformo le stringhe in numeri interi
    first_y = int(first_y)
    last_y = int(last_y)

    #controllo che l'ordine degli anni sia corretto
    if first_y > last_y:
        raise ExamException('Error, attenzione il primo anno non può essere maggiore dell\' ultimo')
    
    #creo la lista che conterrà le medie dei passeggeri
    lista_media = []
    # t è la fascia di anni che ci interessano
    t = last_y - first_y
    #creo una lista che conterrà le liste con i dati passeggeri
    temporanea = []
    sommatoria = 0

    #creo una lista con gli anni del lasso di tempo considerato 
    for i in range (t+1):
        list_anno = [None, None, None, None, None, None, None, None, None, None, None, None]
        #aggiungo alla lista l'anno di riferimento in modo da poterlo riconoscere
        list_anno.append(first_y + i)
        temporanea.append(list_anno)
        
    #aggiungo alle liste i dati dei passeggeri
    for list_y in temporanea:
        for el in lista:
            elem = el[0].split('-')
            
            #confronta l'anno della lista del get_data con l'anno nella lista temporanea e se sono uguali vengono aggiunti i dati dei passeggeri
            if int(elem[0]) == list_y[-1]:
                list_y[int(elem[1])] = el[1]
    
    #m corrisponde al mese e all'indice che useremo
    m = 1
    while m <= 12:
        for j in range(t):
            #se uno dei dati è uguale a None, la sottrazione sarà uguale a zero
            if temporanea[j + 1][m]==None or temporanea[j][m] == None:
                sottr = 0
            else:    
                sottr = temporanea[j + 1][m] - temporanea[j][m]
            #
            sommatoria += sottr
        lista_media.append(sommatoria/t)
        sommatoria = 0
        m += 1

    return lista_media






    