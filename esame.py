from datetime import datetime

class ExamException(Exception):
    pass

class CSVFile():
    #in questo punto inizializzo la classe
    def __init__(self,name):
        self.name = name

        #qui controllo che sia una stringa
        if not isinstance(self.name, str):
            raise ExamException('TypeError, il nome del file "{}" non è una stringa'.format(self.name))

    def get_data(self):
        #qui inizializzo la futura lista di liste
        lista_futura = []

        #qui apro il file        
        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException('NotFoundError, il file non esiste o non è leggibile')

        for line in my_file:
            #split gli elementi
            elements = line.split(',')

            #elimino il carattere '\n'
            elements[-1] = elements[-1].strip()
       
            #aggiungo ogni lista nella lista finale
            if elements[0] != 'date':
                lista_futura.append(elements)

        #chiudo il file e return la lista di liste
        my_file.close()
        return lista_futura

class CSVTimeSeriesFile(CSVFile):

    def get_data(self):
        #inizializzo la futura lista di liste
        lista_prec = super().get_data()
        lista_corretta = []

        for element in lista_prec:
            #controllo i dati passeggero
            #controlo che ci siano
            if len(element) < 2:
                #altrimenti li aggiungo come None
                element.append(None)
            
            #controllo che si possano trasformare in intero
            elif not element[1].isdigit():
                element[1] = None
            
            #trasformo tutti i dati accettabili del passeggeri in int
            else:
                element[1] = int(element[1])
            
            try:
                date1 = datetime.strptime(element[0], '%Y-%m')
            except:
                continue

            lista_corretta.append(element)

        return lista_corretta

def compute_avg_monthly_difference(lista, first_y, last_y):
    #faccio controlli sull'anno iniziale (first_y) e finale (last_y)

    #controllo che siano una stringa
    if not isinstance(first_y, str):
        raise ExamException('TypeError, l\' anno iniziale non è una stringa')
    
    if not isinstance(last_y, str):
        raise ExamException('TypeError, l\' anno finale non è una stringa')

    #controllo che siano una stringa di soli numeri
    if not first_y.isdigit():
        raise ExamException('Error, l\' anno iniziale non è un numero intero')
    
    if not last_y.isdigit():
        raise ExamException('Error, l\' anno finale non è un numero intero')

    #faccio iniziare la funzione
    first_y = int(first_y)
    last_y = int(last_y)

    lista_media = []
    
    t = last_y - first_y
    temporanea = []
    somma = 0
        
    for i in range (t+1):
        list_anno = [None, None, None, None, None, None, None, None, None, None, None, None]
        list_anno.append(first_y + i)
        temporanea.append(list_anno)
        
    
    for list_y in temporanea:
        for el in lista:
            elem = el[0].split('-')
        
            if int(elem[0]) == list_y[-1]:
                list_y[int(elem[1])] = el[1]

    m = 1
    while m <= 12:
        for j in range(t):
            if temporanea[j + 1][m]==None or temporanea[j][m] == None:
                sottr = 0
            else:    
                sottr = temporanea[j + 1][m] - temporanea[j][m]
            somma += sottr
        lista_media.append(somma/t)
        somma = 0
        m += 1

    return lista_media


time_series_file = CSVTimeSeriesFile (name='data.csv')
time_series = time_series_file.get_data() 
print(time_series)

media = compute_avg_monthly_difference(time_series, '1949', '1951')
print(media)





    