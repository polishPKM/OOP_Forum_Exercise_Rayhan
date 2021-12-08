class fancyRR:
    #initializer
    def __init__(self,nama,amt):
        self._name = nama
        self._amount = amt
        self._standard_price = 0.00
        self.__PRCLSTRR()
        self._total_cost = self.CALCRR()
        
    #setting the standard prices
    def __PRCLSTRR(self):
        if self._name == "Dry Cured Iberian Ham":
            self._standard_price = 177.80
        elif self._name == "Wagyu Steaks":
            self._standard_price = 450.00
        elif self._name == "Matsutake Mushrooms":
            self._standard_price = 272.00
        elif self._name == "Kopi Luwak Coffee":
            self._standard_price = 306.50
        elif self._name == "Moose Cheese":
            self._standard_price = 487.20
        elif self._name == "White Truffles":
            self._standard_price = 3600.00
        elif self._name == "Blue Fin Tuna":
            self._standard_price = 3603.00
        elif self._name == "Le Bonnotte Potatoes":
            self._standard_price = 270.81
            
    #calculating total costs
    def CALCRR(self):
        return self._amount * self._standard_price
    
    #overriding str
    def __str__(self):
        return "\nName: " + str(self._name) + "\n" + \
            "Price per pound: " + str(self._standard_price) + "\n" + \
            "Order Amount: " + str(self._amount) + "\n" + \
            "Total Order Cost: " + str(self._total_cost)
