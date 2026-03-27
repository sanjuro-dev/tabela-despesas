import pandas as pd
from datetime import datetime
import os

import matplotlib.pyplot as plt
import numpy as np

from tkinter import messagebox, END

columns = ["Category", "Description", "Value", "Date"]
categories = ["Energy", "Wi-Fi", "Transport", "Food", "Leisure"]
def initialize():
    if not os.path.exists("data.xlsx"):
        df = pd.DataFrame(columns=columns)
        df.to_excel("data.xlsx", index=False)

def categorysum(categoria, dados):
    s = 0
    for item in dados:
        if item["Category"] == categoria and item["Date"].month == datetime.now().month and item[
            "Date"].year == datetime.now().year:
            s += item["Value"]
    return s



def monthsum(mes, dados):
    s = 0
    for item in dados:
        if item["Date"].month == mes and item["Date"].year == datetime.now().year:
            s += item["Value"]
    return s


def spendings(value, category, description):

    if not value.get() or not category.get():
        messagebox.showerror("Error", "Fill all the inputs!")
        return None

    cat = category.get()
    desc = description.get()
    try:
        val = float(value.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input, only numbers allowed.")
        return None

    df = pd.read_excel("data.xlsx")

    date = pd.to_datetime(datetime.now().date())

    new = {
        "Category": cat,
        "Description": desc,
        "Value": val,
        "Date": date
    }

    df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.to_excel("data.xlsx", index=False)

    description.delete(0, END)
    value.delete(0, END)

    messagebox.showinfo("Success", "Spending added with success!")

    return None


def generate():
    df = pd.read_excel("data.xlsx")

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    values= list()
    monthly = list()

    data = df.to_dict(orient="records")

    for o in categories:
        s = categorysum(o, data)
        values.append(s)

    for m in range(12):
        s = monthsum(m + 1, data)
        monthly.append(s)

    # Filter null categories
    fvalues = []
    fcategories = []

    for c, v in zip(categories, values):
        if v > 0:
            fcategories.append(c)
            fvalues.append(v)

    if not fvalues:
        messagebox.showinfo("Info", "No data to display")
        return

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Pie Chart
    axs[0].pie(fvalues, labels=fcategories, autopct='%1.1f%%', startangle=140)

    axs[0].set_title("Spending's Distribution")
    axs[0].axis('equal')

    # Bar Chart
    axs[1].bar(months, monthly)

    axs[1].set_title("Month Spending's")
    axs[1].set_ylabel("Value")

    axs[1].set_xticks(range(len(months)))
    axs[1].set_xticklabels(months, rotation=45)

    # Show Graphs
    plt.tight_layout()
    plt.show()

