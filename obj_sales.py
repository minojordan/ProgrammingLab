class CSVFile():
    def __init__(self,name):
        self.name = name
    
    def get_data(self):
        values=[]
        try:    
            mio_file = open(self.name)
            for line in mio_file:
                elements = line.split(',')
                if elements[0] != 'Date':
                    values.append(elements)
            mio_file.close()
            return values
        except Exception as e:
            print('stai cercando di aprire un file non esistente')
            print('ed ho avuto questo errore:"{}"'.format(e))

 


mio_file = CSVFile("shampoo_sales.txt")
print (mio_file.get_data())

class NumericalCSVFile(CSVFile):
    pass
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
mino = NumericalCSVFile("shampoo_sales.txt")
print (mio_file.get_data())
