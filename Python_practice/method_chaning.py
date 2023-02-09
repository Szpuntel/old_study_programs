class Car:

    def turn_on(self):
        print ("You start the engine my dude")
        return self

    def drive(self):
        print ("You start drivin my dude")
        return self

    def brake(self):
        print ("You start breakin my dude")
        return self

    def turn_off(self):
        print ("You turn off the engine my dude")
        return self

car = Car()

#car.turn_on()  
#              --->  car.turn_on().drive()            
#car.drive()

#car.turn_on().drive()   # --> Nie zadziała jeżeli funkcja nie zwróci self.
                        # bez self po wykonaniu funkcji car.turn_on().drive() 
                        # wykonuje sie najpierw car.turn_on() ktory nie zwróci "car."
                        # wiec kolejny etap sie nie wykona bo kod bedzie ".drive()" zamiast "car.drive()"



car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()




