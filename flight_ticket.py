print("Welocome to worldwide  trip")
login=input("enter the login id:")
password=int(input("enter the password:"))
def customer():
    cls=input("travelers&classs: 1.Economy, 2.premium Economy, 3.Business:")
    print("Economy=Rs.2000")
    print("Premium Economy=Rs.3000")
    print("Business=Rs.5000")
    members=int(input("Enter the number of travellers:"))
    for i in range(0,members):
        gender=input("Enter the gender:")
        name=input("Enter the first name:")
        names=input("Enter the last name:")
        age=int(input("enter the age of travellers:"))
        if (age<2):
            print("infants:")
        elif (age<=12):
            print("children:")
        elif (age<100):
            print("adults:")
        mail=input("Enter the mail id:")
def adv():
        prefernce=input("1.Armed Force, 2.Student, 3.Senior Citizen, 4.Doctore&Nurses,5.others")
        if prefernce=="1":
            print("20% discount")
        elif prefernce=="2":
            print("15% discont")
        elif prefernce=="3":
            print("10% discont")
        elif prefernce=="4":
            print("5% discount")
        else:
            print("No dicount")
def flight():
        print("show the name of flights")
        print("Air line")
        print("Indigo")
        print("SpiceJet")
        print("Air India Express")
        select=input("chosse the flights:")
        print("show the payment page")
        payment_page=input("select the options: 1.baggage policy, cancellation refund policy, traveller details:")
        if payment_page=="1":
            print("refund & baggage policy")
            baggage_policy=input("baggage details:1.baggage weight, 2.date change:")
            if baggage_policy=="1": 
                print("show the limitted weight of baggage")
            elif baggage_policy=="2":
                print("data change options")
                w=input("Enter the new date:")
                print("Your date is changed")
                print("your flight is booked")        
            print("cancellation refund policy")
            hours=int(input("Enter the time frame & Airline fee, hours:"))
            if(hours<4):
                print("Non refundable")
            elif hours==5<24:
                print("amount refund")
            elif hours==25<96:
                print("with zero cancellation")
            elif hours==96<8760:
                print("With Zero cancellation")                
            print("traveller details")
            travellers=int(input("Enter the number of travellers:"))
            for j in range(0,travellers):
                gender=input("Enter the gender:")
                name=input("Enter the name:")
                age=int(input("Enter the age:"))
            print("payment calculations")
            choice=input("travelers&classs: 1.Economy, 2.premium Economy, 3.Business:")
            mem=int(input("Enter the number of travellers:"))
            if choice=="1":
                pay=mem*2000
                print(pay)
            elif choice=="2":
                pay=mem*3000
                print(pay)
            elif choice=="3":
                pay=mem*5000
                print(pay)                
            print("show the payment method")
            payment=input(("Select the payment method:1.google pay, 2.phonepay, 3.cancel:"))
            if payment=="1" or payment=="2":
                print("Your payment is successful")
                print("Your flight is booked")
            else:
                print("your payment is pending")
                print("Your booking is cancel")    
if(login =="preethi")and (password==566):
    print("login success")
    options=input("select the options:1) oneway, 2) roundtrip, 3) multicity:")
    if(options=="1"):
        f=input("From:")
        y=input("To:")
        z=input("Departure date:")
        customer()
        adv()
        print("Search Flights")
        flight()
    elif(options=="2"):
        i=input("From:")
        j=input("To:")
        k=input("Depature date:")
        l=input("Return date:")
        customer()
        adv()
        print("Search Flights")
        flight()
    elif (options=="3"):
        m=input("From:")
        n=input("To:")
        o=input("Date:")
        add=input("Add city:")
        customer()
        adv()
        print("Search Flights")
        flight()
else:
    print("invalide user")
        
    

    
    
    
