class CSVFile():
    def __init__(self,name):
        self.name = name
        if not isinstance(self.name,str):
            raise Exception('Ho avuto un errore,ecco il parametro che lo ha generato:"{}"'.format(self.name))
        #try:    
        #    mio_file = open(self.name,'r')

        #except Exception as e:
        #    print('stai cercando di aprire un file non esistente')
        #    print('ed ho avuto questo errore:"{}"'.format(e))    

    def get_data(self, start = None, end = None):
        values=[]
        try:    
            mio_file = open(self.name,'r')

        except Exception as e:
            print('stai cercando di aprire un file non esistente')
            print('ed ho avuto questo errore:"{}"'.format(e))
        
        
        for line in mio_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                values.append(elements)
    
        if(start != None and end != None ):
            values = values[start:end]
           
        mio_file.close()
        return values


mio_file = CSVFile('shampoo_sales.txt')
print (mio_file.get_data(0,None))

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        data = super().get_data()
        use = []
        for item in data:
            for x in item[1:]:
                try:
                    x = float(x)
                    use.append(x)
                except ValueError:
                    print('il tipon dell\'item è:{}'.format(type(x)))
        return use
#mino = NumericalCSVFile("shampoo_sales.txt")
#print (mino.get_data())
