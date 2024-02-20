import tkinter as tk
from tkinter import *

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def predict_house_price(area_income, house_age, num_rooms, num_bedrooms, population):
    data = pd.read_csv(r"C:\Users\dell xps\Downloads\usa_dataset\USA_Housing.csv")
    data = data.drop(['Address'], axis=1)

    X = data.drop('Price', axis=1)
    Y = data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.30)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    input_data = np.array([[area_income, house_age, num_rooms, num_bedrooms, population]])
    price_prediction = model.predict(input_data)

    return price_prediction[0]

def calculate_price():
    try:
        area_income = float(entry_income.get())
        house_age = float(entry_house_age.get())
        num_rooms = float(entry_num_rooms.get())
        num_bedrooms = float(entry_num_bedrooms.get())
        population = float(entry_population.get())

        price = predict_house_price(area_income, house_age, num_rooms, num_bedrooms, population)

        result_label.config(text=f"Predicted Price: ${price:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numeric values")


fe = Tk()
fe.title("House Pricing Prediction")
fe.geometry("400x250+400+200")#widthxheight+starfenetrex+startfenetrey
fe.configure(bg='#7ACFB0')

#grid dyali feha 2 columns:0 dyal llabels w 1 dyal entries donc column=1 donc 7etou hda entries 0 hetou hda labels
#grid feha 7 rows kaybdaw men 0 tal 6 donc row = o zeama hetou f ster lewel row =5 donc ster 4...


label_income =Label(fe, text="Avg. Area Income:", fg='#00BDC8',bg='#1C5588' )
label_income.grid(row=0, column=0, padx=50, pady=5)
entry_income =Entry(fe)
entry_income.grid(row=0, column=1, padx=10, pady=5)

label_house_age =Label(fe, text="Avg. Area House Age:", fg='#00BDC8',bg='#1C5588' )
label_house_age.grid(row=1, column=0, padx=10, pady=5)
entry_house_age =Entry(fe)
entry_house_age.grid(row=1, column=1, padx=10, pady=5)

label_num_rooms =Label(fe, text="Avg. Area Number of Rooms:", fg='#00BDC8',bg='#1C5588' )
label_num_rooms.grid(row=2, column=0, padx=10, pady=5)
entry_num_rooms =Entry(fe)
entry_num_rooms.grid(row=2, column=1, padx=10, pady=5)

label_num_bedrooms =Label(fe, text="Avg. Area Number of Bedrooms:", fg='#00BDC8',bg='#1C5588' )
label_num_bedrooms.grid(row=3, column=0, padx=10, pady=5)
entry_num_bedrooms =Entry(fe)
entry_num_bedrooms.grid(row=3, column=1, padx=10, pady=5)

label_population = Label(fe, text="Avg. Population:", fg='#00BDC8',bg='#1C5588' )
label_population.grid(row=4, column=0, padx=10, pady=5)
entry_population =Entry(fe)
entry_population.grid(row=4, column=1, padx=10, pady=5)


calculate_button =Button(fe, text="Calculate Price",fg='#00BDC8',bg='#1C5588', command=calculate_price)
calculate_button.grid(row=5, column=0, padx=70, pady=20)

result_label =Label(fe, text="",bg='#00BDC8',fg='#1C5588')
result_label.grid(row=6, column=0, pady=10)




fe.mainloop()
