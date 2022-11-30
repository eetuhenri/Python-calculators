# module imports
   from tkinter import *
   from tkinter.ttk import *
   from tkinter import ttk
   import matplotlib.pyplot as plt
   import numpy as np
    
    # creates menu window
    master = Tk()
   master.title("Menu")
   # sets the size of the menu window
   master.geometry("200x200")
   
   
   def openNewWindow_A():  # A part
       # defining terms and printing headline
       portion_down_payment = 0.25
       current_savings = 0
       r = 0.04
       print("Down payment calculator")
   
       # asking needed information
       def inputs():
           total_cost = float(input("What is the total cost of your future home? :"))
           annual_salary = float(input("What is your annual salary? :"))
           portion_saved = float(input("How much you want to be saved? (in decimals) :"))
           print("Your current savings are", current_savings, "€")
           print("Down payment will be", "{0:.0f} %".format(portion_down_payment * 100), "of your whole loan")
           print("Annual interest rate is", "{0:.0f} %".format(r * 100))
           month_calc(portion_down_payment, current_savings, r, total_cost, annual_salary,
                      portion_saved)  # sending inputs to calculator
   
       # calculator function
       def month_calc(portion_down_payment, current_savings, r, total_cost, annual_salary, portion_saved):
           months = 0
           while current_savings < (
                   portion_down_payment * total_cost):  # looping until savings are bigger than the buying price
               monthly_salary = annual_salary / 12  # calculations
               monthly_savings = portion_saved * monthly_salary
               current_savings += (current_savings * r / 12) + monthly_savings
               months += 1
           print("To get the needed savings you will need", months, "months")  # final answer
   
       inputs()  # input function runs always first
   
   
   def openNewWindow_B():  # B-part
       # defining terms and printing headline
       portion_down_payment = 0.25
       current_savings = 0
       r = 0.04
       print("Down payment calculator with pay raise")
   
       # asking needed information
       def inputs():
          total_cost = float(input("What is the total cost of your future home? :"))
          annual_salary = float(input("What is your annual salary? :"))
          semi_annual_raise = float(input("How much does your salary will raise? (in decimals) :"))
          portion_saved = float(input("How much you want to be saved? (in decimals) :"))
          print("Your current savings are", current_savings, "€")
          print("Down payment will be", "{0:.0f} %".format(portion_down_payment * 100), "of your whole loan")
          print("Annual interest rate is", "{0:.0f} %".format(r * 100))
          month_calc(portion_down_payment, current_savings, r, total_cost, annual_salary, semi_annual_raise,
                     portion_saved)  # sending inputs to calculator
  
      # list of the savings
      current_savings_list = []
  
      # function to display graph
      def graph(current_savings_list):
          ypoints = np.array(current_savings_list)
          plt.plot(ypoints)  # plotting the savings to the graph
          plt.xlabel("duration/time (Months)")  # x axis
          plt.ylabel("Savings (€)")  # y axis
          plt.title("Graph for down payment saving")
  
      # calculator function
      def month_calc(portion_down_payment, current_savings, r, total_cost, annual_salary, semi_annual_raise,
                     portion_saved):
          months = 0
          while current_savings < (
                  portion_down_payment * total_cost):  # looping until savings are bigger than the buying price
              monthly_salary = annual_salary / 12  # calculations
              monthly_savings = portion_saved * monthly_salary
              current_savings += (current_savings * r / 12) + monthly_savings
              months += 1
              current_savings_list.append(
                  current_savings)  # adds savings to a list for the graph every time the function loops
              graph(current_savings_list)  # sending the list to the graph function
              if months % 6 == 0:  # salary rise possibility
                  annual_salary = annual_salary + (annual_salary * semi_annual_raise)  # calculation
          print("To get the needed savings you will need", months, "months")  # final answer
  
      inputs()  # input function runs always first
      plt.show()  # shows the graph
  
  
  def openNewWindow_C():  # C-part
      # creating window for the c-part and its name
      root = Tk()
      root.title("Loan calculator")
  
      # calculations for the monthly payment
      def loan_calc():
          if amount_entry.get() and intrest_entry.get() and number_of_years_entry.get() and down_payment_entry.get():
              years = int(number_of_years_entry.get())
              months = years * 12
              intrest = float(intrest_entry.get())
              loan = int(amount_entry.get())
              down_payment = int(down_payment_entry.get())
              price_after_down = loan - down_payment
              monthly_rate = intrest / 100 / 12
              payment = (monthly_rate / (1 - (1 + monthly_rate) ** (-months))) * price_after_down
              payment = f"{payment:,.2f}"  # reformation of the answer
              payment_label.config(text=f"Monthly Payment: {payment} €")  # text showing the answer
          else:
              payment_label.config(text="Something is missing")  # if inputs aren't correct this will display
  
      # size of the program and headline
      my_label_frame = LabelFrame(root, text="Loan calculator")
      my_label_frame.pack(pady=30)
      my_frame = Frame(my_label_frame)
      my_frame.pack(pady=20, padx=20)
      # buttons and their text
      loan_amount = Label(my_frame, text="How big is the loan you want?")
      amount_entry = Entry(my_frame, font=("Helvetica", 16))
  
      annual_intrest = Label(my_frame, text="What is the annual intrest rate you want? (input in %)")
      intrest_entry = Entry(my_frame, font=("Helvetica", 16))
  
      number_of_years = Label(my_frame, text="How many years you want to pay the loan?")
      number_of_years_entry = Entry(my_frame, font=("Helvetica", 16))
  
      down_payment = Label(my_frame, text="How much is the down payment?")
      down_payment_entry = Entry(my_frame, font=("Helvetica", 16))
      # placements for all the buttons
      loan_amount.grid(row=0, column=0)
      amount_entry.grid(row=0, column=1)
  
      annual_intrest.grid(row=1, column=0)
      intrest_entry.grid(row=1, column=1, pady=20)
  
      number_of_years.grid(row=2, column=0)
      number_of_years_entry.grid(row=2, column=1)
  
      down_payment.grid(row=3, column=0)
      down_payment_entry.grid(row=3, column=1, pady=20)
      # placement for the button and it's command after being pressed
      my_button = Button(my_label_frame, text="Calculate loan", command=loan_calc)
      my_button.pack(pady=20)
  
      payment_label = Label(root, text="", font=("Helvetica", 18))
      payment_label.pack(pady=20)
  
      payment_label = Label(root, text="", font=("Helvetica", 18))
      payment_label.pack(pady=20)
  
  
  def openNewWindow_D():  # D-part
      root = Tk()  # creates window
      root.title("How big loan I can afford?")  # window name
      # program name and size of the window
      my_label_frame = LabelFrame(root, text="How big loan I can afford?")
      my_label_frame.pack(pady=5)
      my_frame = Frame(my_label_frame)
      my_frame.pack(pady=5, padx=60)
  
      # different outcomes for the selections that have been made
      def selected():
          if salary.get() == "Under 40 000" and saved.get() == "Under 5 000 €":
              amount_label.config(text="You will be able to take loan of: 30 000 - 30 500 €")
          elif salary.get() == "Under 40 000" and saved.get() == "5 000-10 000 €":
              amount_label.config(text="You will be able to take loan of: 45 000 - 50 00 €")
          elif salary.get() == "Under 40 000" and saved.get() == "Over 10 000 €":
              amount_label.config(text="You will be able to take loan of: 60 000 - 73 000 €")
          elif salary.get() == "40 000-60 000" and saved.get() == "Under 5 000 €":
              amount_label.config(text="You will be able to take loan of: 30 000 - 30 500 €")
          elif salary.get() == "40 000-60 000" and saved.get() == "5 000-10 000 €":
              amount_label.config(text="You will be able to take loan of: 45 000 - 53 000 €")
          elif salary.get() == "40 000-60 000" and saved.get() == "Over 10 000 €":
              amount_label.config(text="You will be able to take loan of: 60 000- 73 000 €")
          elif salary.get() == "Over 60 000" and saved.get() == "Under 5 000 €":
              amount_label.config(text="You will be able to take loan of: 30 000- 30 500 €")
          elif salary.get() == "Over 60 000" and saved.get() == "5 000-10 000 €":
              amount_label.config(text="You will be able to buy take loan of: 45 000- 53 000 €")
          elif salary.get() == "Over 60 000" and saved.get() == "Over 10 000 €":
              amount_label.config(text="You will be able to take loan of: 60 000- 73 000 €")
          elif salary.get() == "Under 40 000" and saved.get() == "Under 5 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 5 000 €")
          elif salary.get() == "Under 40 000" and saved.get() == "5 000-10 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 5 000 - 8 000 €")
          elif salary.get() == "Under 40 000" and saved.get() == "Over 10 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 10 000 - 11 000 €")
          elif salary.get() == "40 000-60 000" and saved.get() == "Under 5 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 25 000 - 27 000 €")
          elif salary.get() == "40 000-60 000" and saved.get() == "5 000-10 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 25 000 - 30 000 €")
          elif salary.get() == "40 000-60 000" and saved.get() == "Over 10 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to 30 000 - 33 000")
          elif salary.get() == "Over 60 000" and saved.get() == "Under 5 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 30 000 - 33 000")
          elif salary.get() == "Over 60 000" and saved.get() == "5 000-10 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 45 000 - 53 000€")
          elif salary.get() == "Over 60 000" and saved.get() == "Over 10 000 €" and kids.get() == "Over 4 kids":
              amount_label.config(text="You will be able to take loan of: 60 000 - 73 000 €")
  
      # drop down boxes to choose the right selection
      people = Label(my_frame, text="One or Two people?")  # text that the user see on the program
      people.grid(row=1, column=0)  # placement of the text
      options = ["1", "2"]  # options of which to choose
      people = ttk.Combobox(my_frame, values=options, width=25)  # size of the drop down box
      people.current(0)  # preset selection
      people.grid(row=1, column=1)  # placement
      people.bind("<<ComboboxSelected>>")
  
      monthly_salary = Label(my_frame, text="How big is your yearly salary?")
      monthly_salary.grid(row=2, column=0)
      options = ["Under 40 000", "40 000-60 000", "Over 60 000"]
      salary = ttk.Combobox(my_frame, values=options, width=25)
      salary.current(0)
      salary.grid(row=2, column=1)
      salary.bind("<<ComboboxSelected>>", selected)  # command to the selected function
  
      home_type = Label(my_frame, text="What type of house you want to buy?")
      home_type.grid(row=3, column=0)
      options = ["Detached house", "Condominium", "Summer house"]
      home = ttk.Combobox(my_frame, values=options, width=25)
      home.current(0)
      home.grid(row=3, column=1)
      home.bind("<<ComboboxSelected>>", selected)
  
      home_site = Label(my_frame, text="In which region is your new home going to be?")
      home_site.grid(row=4, column=0)
      options = ["Joensuu", "Hattula", "Imatra", "Kuopio", "Mäntsälä", "Pyhäjoki"]
      site = ttk.Combobox(my_frame, values=options, width=25)
      site.current(0)
      site.grid(row=4, column=1)
      site.bind("<<ComboboxSelected>>")
  
      amount_saved = Label(my_frame, text="How much savings you have?")
      amount_saved.grid(row=5, column=0)
      options = ["Under 5 000 €", "5 000-10 000 €", "Over 10 000 €"]
      saved = ttk.Combobox(my_frame, values=options, width=25)
      saved.current(0)
      saved.grid(row=5, column=1)
      saved.bind("<<ComboboxSelected>>", selected)
  
      kid_count = Label(my_frame, text="How many kids you have?")
      kid_count.grid(row=6, column=0)
      options = ["No kids", "1-4", "Over 4 kids"]
      kids = ttk.Combobox(my_frame, values=options, width=25)
      kids.current(0)
      kids.grid(row=6, column=1)
      kids.bind("<<ComboboxSelected>>", selected)
  
      car_count = Label(my_frame, text="How many cars you have?")
      car_count.grid(row=7, column=0)
      options = ["No cars", "1-2", "Over 2 cars"]
      cars = ttk.Combobox(my_frame, values=options, width=25)
      cars.current(0)
      cars.grid(row=7, column=1)
      cars.bind("<<ComboboxSelected>>", selected)
      # button to calculate the loan and its placement
      my_button = Button(my_label_frame, text="Calculate loan", command=selected)
      my_button.pack(pady=20)
      # answer text and its position
      amount_label = Label(root, text="", font=("Helvetica", 18))
      amount_label.pack(pady=20)
  
      root.mainloop()  # runs the window creation line first
  
  
  # buttons to choose which part to open
  btn = Button(master, text="Part A (No UI)", command=openNewWindow_A)
  btn.pack(pady=10)
  btn = Button(master, text="Part B (No UI)", command=openNewWindow_B)
  btn.pack(pady=10)
  btn = Button(master, text="Part C (UI)", command=openNewWindow_C)
  btn.pack(pady=10)
  btn = Button(master, text="Part D (UI)", command=openNewWindow_D)
  btn.pack(pady=10)
  
  # runs the menu window first
  mainloop()
  
  # made by group 2
