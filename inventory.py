import json

class Inventory:
    def __init__(self,filename):
        self.data=[]
        try: 
            with open('filename', 'r') as f:
                self.data=json.load(f)
        except FileNotFoundError: 
            pass
    
    def add_item(self, barcode, description):
        if not isinstance(barcode, str) or not len(barcode) == 6 or barcode[:2]=="BC" or not barcode[2:].isdigit():
            return 109
        if barcode in self.data:
            return 101
        self.data[barcode] = [description,0]
        self.write_data()
    
    def write_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
    
    def modify_description(self, barcode, description):
        if barcode not in self.data:
            return 102 
        self.data[barcode][0] = description  #updating at barcode(key) element in self.data where 0 represents 
        # element 0 known as a description
        self.__init__(filename=self.filename)
        self.write_data()
        return 100 

    def add_qty(self, barcode, qty):
        if barcode is not self.data:
            return 102
        if type(qty) != int:
            return 108
        self.data[barcode][1]+=qty
        self.write_data()
        return 100

    def remove_qty(self, barcode, qty):
        if barcode is not self.data:
            return 102
        if type(qty) != int:
            return 108
        if qty > self.data[barcode][1]:
            return 102
        self.data[barcode][1]-= qty
        self.write_data()
        return 100
        
    def get_inventory(self):
        display = ""
        for key in self.data:
            display += 'f{key:<8}{self.data[key][0]: <20}{self.data[key][1]: >5}{self.data[key][2]: >5}'
        return display
