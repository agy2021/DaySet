from django.shortcuts import render, redirect
from .forms import *
import requests
import yfinance as yf
import wikipedia
import datetime

def index(response):
    print("home")
    return render(response, "app/index.html")

def weather(response):
    print("weather!")
    if response.method == "POST":
        if response.POST.get("go"):
            form = Weather(response.POST)
            if form.is_valid():
                print("valid form")
                city = form.cleaned_data["city"]
                get = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fe8428be8be41b51cb6eaebddba23e22").json()
                main = get["main"]

                with open("weather_data", "w") as f:
                    f.write("Temperature: " + str((main["temp"]-273.15)*(9/5)+32)[:4] + "\n")
                    f.write("Min Temperature: " + str((main["temp_min"] - 273.15) * (9 / 5) + 32)[:4] + "\n")
                    f.write("Max Temperature: " + str((main["temp_max"] - 273.15) * (9 / 5) + 32)[:4] + "\n")
                    f.write("Humidity: %" + str((main["humidity"])) + "\n")

                with open("weather_data", "r") as f:
                    return render(response, "app/weather_data.html", {"data":f.readlines()})
            else:
                print("Invalid form.")
    else:
        new_form = Weather()

    return render(response, "app/weather.html", {"form":new_form})

def covid(response):
    get = requests.get("https://api.covidactnow.org/v2/country/US.json?apiKey=1159a7cc6447438a9c9e21601479924a").json()
    main = get["actuals"]

    with open("covid_data", "w") as f:
        f.write(str("Cases: " + str(main["cases"]) + "\n"))
        f.write(str("Deaths: " + str(main["deaths"]) + "\n"))
        f.write(str("New Cases: " + str(main["newCases"]) + "\n"))
        f.write(str("New Deaths: " + str(main["newDeaths"]) + "\n"))
        f.write(str("Vaccines Administered: " + str(main["vaccinesAdministered"]) + "\n"))

    with open("covid_data", "r") as f:
        return render(response, "app/covid.html", {"data":f.readlines()})

global bmi_logged_in
bmi_logged_in = False

def bmi(response):
    print("bmi")
    if response.method == "POST":
        if response.POST.get("go"):
            form = Bmi(response.POST)
            if form.is_valid():
                print("valid form")
                weight = form.cleaned_data["weight"]
                height = form.cleaned_data["height"]

                global bmi
                bmi = weight/height ** 2 * 703

                global status

                if bmi < 18:
                    status = "underweight"
                    color = "yellow"
                elif bmi > 18 and bmi < 25:
                    status = "healthy"
                    color = "green"
                elif bmi < 25 and bmi < 30:
                    status = "overweight"
                    color = "yellow"
                elif bmi > 30:
                    status = "obese"
                    color = "red"
                else:
                    status = "invalid"

                global bmi_logged_in
                bmi_logged_in = True

                return render(response, "app/bmi_data.html", {"bmi":bmi, "status":status, "color":color})
            else:
                print("Invalid form.")
    else:
        new_form = Bmi()

    return render(response, "app/bmi.html", {"form": new_form})

global logged_in
logged_in = False

def print_bmi(response):
    global bmi_logged_in
    global bmi
    global status

    if bmi_logged_in:
        return render(response, "app/print_bmi.html", {"bmi":bmi, "status":status, "date":datetime.datetime.now().strftime("%d/%m/%Y")})
    else:
        return redirect("/bmi")

def notes(response):
    global logged_in
    logged_in = True
    print("notes!")
    if response.method == "POST":
        if response.POST.get("save"):
            form = Notes(response.POST)
            if form.is_valid():
                print("valid form")
                data = form.cleaned_data["data"]

                with open("data", "a") as f:
                    f.write(data)

                return redirect("/notes_data")
            else:
                print("Invalid form.")
    else:
        global new_form1
        new_form1 = Notes()

    return render(response, "app/notes.html", {"form": new_form1})

def notes_data(response):
    global logged_in
    if logged_in:
        with open("data", "r") as f:
            return render(response, "app/notes_data.html", {"data": f.readlines()})
    else:
        return redirect("/notes/")

def del_notes(response):
    with open("data", "w") as f:
        f.write("")

    return render(response, "app/notes_deleted.html", {})

def stocks(response):
    print("stocks")
    if response.method == "POST":
        if response.POST.get("go"):
            form = Stocks(response.POST)
            if form.is_valid():
                print("valid form")
                label = form.cleaned_data["label"]
                company = yf.Ticker(label.upper())

                history = company.history(period="max")

                with open("stocks", "w") as f:
                    f.write(str(str(history) + "\n")[:-25])

                with open("stocks", "r") as f:
                    return render(response, "app/stock_data.html", {"data":f.readlines(), "label":label})
            else:
                print("Invalid form.")
    else:
        global new_form2
        new_form2 = Stocks()

    return render(response, "app/stocks.html", {"form":new_form2})

def wiki(response):
    print("wikipedia")
    if response.method == "POST":
        if response.POST.get("go"):
            form = Wikipedia(response.POST)
            if form.is_valid():
                print("valid form")
                search = form.cleaned_data["search"]
                result = wikipedia.search(search)

                with open("wiki_data", "w") as f:
                    f.write(wikipedia.page(result).summary)

                with open("wiki_data", "r") as f:
                    return render(response, "app/wiki_data.html", {"data": f.readlines(), "search": search})
            else:
                print("Invalid form.")
    else:
        global new_form3
        new_form3 = Wikipedia()

    return render(response, "app/wiki.html", {"form": new_form3})

def favorite(response):
    if response.method == "POST":
        if response.POST.get("save"):
            form = Favorite(response.POST)
            if form.is_valid():
                print("valid form")
                favorite = form.cleaned_data["link"]

                print("writing...")

                with open("favorites", "a") as f:
                    f.write(str(favorite) + "\n")

                print("wrote to file. redirecting...")

                return redirect("/favorites/")
            else:
                print("Invalid form.")
    else:
        global new_form4
        new_form4 = Favorite()

    return render(response, "app/new_favorite.html", {"form": new_form4})

def my_favorite(response):
    with open("favorites", "r") as f:
        if f == "":
            return render(response, "app/favorite.html", {"links":f.readlines(), "favs":False})
        else:
            return render(response, "app/favorite.html", {"links": f.readlines(), "favs":True})

def del_favs(response):
    with open("favorites", "w") as f:
        f.write("")

    return render(response, "app/favorites_deleted.html", {})

def calc(response):
    if response.method == "POST":
        if response.POST.get("save"):
            form = Calc(response.POST)
            if form.is_valid():
                print("valid form")
                expression = form.cleaned_data["expression"]

                print("evaluating and rendering")

                try:
                    return render(response, "app/answer.html", {"expression": expression, "answer":eval(expression)})
                except Exception:
                    return render(response, "app/error.html", {})
            else:
                print("Invalid form.")
    else:
        global new_form5
        new_form5 = Calc()

    return render(response, "app/calculate.html", {"form": new_form5})

def about(response):
    return render(response, "app/about.html", {})

def tools(response):
    return render(response, "app/tools.html", {})