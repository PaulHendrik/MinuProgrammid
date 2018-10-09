from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import scrolledtext
import csv
from datetime import datetime
from tkinter import messagebox

filename = "mi_band_2.csv"
rowNr = (0, 1, 2, 3, 4, 5)
data = []
datesList = []
monthYearList = []
yearList = []
sep = ','

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def getFileContents():
    global data, monthYearList, yearList
    counter = 0
    with open(filename, "r", encoding="utf-8") as csvFile:
        lines = csv.reader(csvFile, delimiter=sep)
        for line in lines:
            if counter == 0:
                header = [row for idx, row in enumerate(line) if idx in rowNr]
            else:
                fileData = [row for idx, row in enumerate(line) if idx in rowNr]
                data.append(fileData)
                datesList.append(fileData[0])
                monthYear = fileData[0][0:7]
                monthYearList.append(monthYear)
                year = fileData[0][0:4]
                yearList.append(year)
            counter += 1
        monthYearList = list(set(monthYearList))
        monthYearList.sort()
        yearList = list(set(yearList))
        yearList.sort()
    csvFile.close()

def showData():
    clearData()
    scrltxtData.insert(INSERT, data)

def getDatesData(event):
    clear = selected1.get()
    if clear == 1:
        clearData()
        clearTable()
    date = cmbDay.get()
    for i in range(len(data)):
        if date in str(data[i]):
            dateFormatted = datetime.strptime(date, '%Y-%m-%d').strftime('%d.%m.%Y')
            scrltxtData.insert(INSERT, "---------------" + dateFormatted + "----------------" + "\n")
            scrltxtData.insert(INSERT, "Samme tehtud:              " + data[i][2] + "\n")
            scrltxtData.insert(INSERT, "Distants läbi käidud (m):  " + data[i][3] + "\n")
            scrltxtData.insert(INSERT, "Kaloreid kulutatud:        " + data[i][5] + "\n")
            scrltxtData.insert(INSERT, "Muudetud:             " + datetime.utcfromtimestamp(int(data[i][1])).strftime('%d.%m.%Y %H:%M:%S') + "\n")
            scrltxtData.insert(INSERT, "-----------------------------------------" + "\n")
            table.unbind("<Double-1>")
            table.insert("", 0, values=(data[i][0], data[i][2], data[i][3], data[i][5]))
            createTable()

def clearData():
    scrltxtData.delete('1.0', END)

def clearTable():
    table.delete(*table.get_children())

def clearDataAndTable():
    for i in table.get_children():
        table.delete(i)
    scrltxtData.delete('1.0', END)

def onDoubleClick(event):
    item = table.selection()
    info = table.item(item, 'values')
    messagebox.showinfo('Rea info', info[0] + "\n" + "\n" + "Samme kokku: " + info[1] + "\n" + "Käidud distants kokku: "
                         + info[2] + " meetrit" + "\n" + "Kaloreid kulutatud kokku: " + info[3] + " kalorit")

def createTable():
    table.pack(side=LEFT, padx=15, pady=5, anchor=W)

def getMonthYearStats(event):
    clearTable()
    statType = selected2.get()
    date = cmbMonthYear.get()
    month = date[5:7]
    year = date[0:4]
    monthSteps = 0
    monthDistance = 0
    monthCalories = 0
    avarageMonthSteps = 0
    avarageMonthDistance = 0
    avarageMonthCalories = 0
    yearSteps = 0
    yearDistance = 0
    yearCalories = 0
    avarageYearSteps = 0
    avarageYearDistance = 0
    avarageYearCalories = 0
    monthCounter = 0
    yearCounter = 0
    if statType == 1:
        clearData()
        if month == "01":
            monthYear = "--------------Jaanuar" + " " + year + "---------------"
        elif month == "02":
            monthYear = "--------------Veebruar" + " " + year + "--------------"
        elif month == "03":
            monthYear = "---------------Märts" + " " + year + "----------------"
        elif month == "04":
            monthYear = "---------------Aprill" + " " + year + "---------------"
        elif month == "05":
            monthYear = "----------------Mai" + " " + year + "-----------------"
        elif month == "06":
            monthYear = "---------------Juuni" + " " + year + "----------------"
        elif month == "07":
            monthYear = "---------------Juuli" + " " + year + "----------------"
        elif month == "08":
            monthYear = "---------------August" + " " + year + "---------------"
        elif month == "09":
            monthYear = "-------------September" + " " + year + "--------------"
        elif month == "10":
            monthYear = "--------------Oktoober" + " " + year + "--------------"
        elif month == "11":
            monthYear = "--------------November" + " " + year + "--------------"
        else:
            monthYear = "-------------Detsember" + " " + year + "--------------"
        for i in range(len(data)):
            if date in str(data[i]):
                monthSteps += int(data[i][2])
                monthDistance += int(data[i][3])
                monthCalories += int(data[i][5])
                monthCounter += 1
        avarageMonthSteps = int(monthSteps / monthCounter)
        avarageMonthDistance = int(monthDistance / monthCounter)
        avarageMonthCalories = int(monthCalories / monthCounter)
        scrltxtData.insert(INSERT, monthYear + "\n")
        scrltxtData.insert(INSERT, "Keskmine sammude arv:       " + str(avarageMonthSteps) + "\n")
        scrltxtData.insert(INSERT, "Keskmine distants (m):      " + str(avarageMonthDistance) + "\n")
        scrltxtData.insert(INSERT, "Keskmine kalorite kulu:     " + str(avarageMonthCalories) + "\n")
        scrltxtData.insert(INSERT, "Samme kokku:                " + str(monthSteps) + "\n")
        scrltxtData.insert(INSERT, "Käidud distants kokku (m):  " + str(monthDistance) + "\n")
        scrltxtData.insert(INSERT, "Kaloreid kulutatud kokku:   " + str(monthCalories) + "\n")
        scrltxtData.insert(INSERT, "Päevade arv:                " + str(monthCounter) + "\n")
        scrltxtData.insert(INSERT, "-----------------------------------------" + "\n")
        clearTable()
        for i in range(len(data)):
            if date in str(data[i]):
                table.insert("", monthCounter, values=(data[i][0], data[i][2], data[i][3], data[i][5]))
        table.bind("<Double-1>", onDoubleClick)
        createTable()
        #deleteFrame()
    elif statType == 2:
        clearData()
        for i in range(len(data)):
            if date in str(data[i]):
                yearSteps += int(data[i][2])
                yearDistance += int(data[i][3])
                yearCalories += int(data[i][5])
                yearCounter += 1
        avarageYearSteps = int(yearSteps / yearCounter)
        avarageYearDistance = int(yearDistance / yearCounter)
        avarageYearCalories = int(yearCalories / yearCounter)
        scrltxtData.insert(INSERT, "------------------" + year + "-------------------" + "\n")
        scrltxtData.insert(INSERT, "Keskmine sammude arv:       " + str(avarageYearSteps) + "\n")
        scrltxtData.insert(INSERT, "Keskmine distants (m):      " + str(avarageYearDistance) + "\n")
        scrltxtData.insert(INSERT, "Keskmine kalorite kulu:     " + str(avarageYearCalories) + "\n")
        scrltxtData.insert(INSERT, "Samme kokku:                " + str(yearSteps) + "\n")
        scrltxtData.insert(INSERT, "Käidud distants kokku (m):  " + str(yearDistance) + "\n")
        scrltxtData.insert(INSERT, "Kaloreid kulutatud kokku:   " + str(yearCalories) + "\n")
        scrltxtData.insert(INSERT, "Päevade arv:                " + str(yearCounter) + "\n")
        scrltxtData.insert(INSERT, "-----------------------------------------" + "\n")
        clearTable()
        for i in range(len(data)):
            if date in str(data[i]):
                table.insert("", monthCounter, values=(data[i][0], data[i][2], data[i][3], data[i][5]))
        table.bind("<Double-1>", onDoubleClick)
        createTable()

def getTotalStats():
    clearDataAndTable()
    totalSteps = 0
    totalDistance = 0
    totalCalories = 0
    avarageTotalSteps = 0
    avarageTotalDistance = 0
    avarageTotalCalories = 0
    counter = 0
    statType = selected2.get()
    if statType == 1:
        cmbMonthYear.configure(state='readonly')
        cmbMonthYear['values'] = (monthYearList)
    elif statType == 2:
        cmbMonthYear.configure(state='readonly')
        cmbMonthYear['values'] = (yearList)
    else:
        cmbMonthYear.configure(state=DISABLED)
        for i in range(len(data)):
            totalSteps += int(data[i][2])
            totalDistance += int(data[i][3])
            totalCalories += int(data[i][5])
            counter += 1
        avarageTotalSteps = int(totalSteps / counter)
        avarageTotalDistance = int(totalDistance / counter)
        avarageTotalCalories = int(totalCalories / counter)
        scrltxtData.insert(INSERT, "------------Kõik andmed kokku------------" + "\n")
        scrltxtData.insert(INSERT, "Keskmine sammude arv:       " + str(avarageTotalSteps) + "\n")
        scrltxtData.insert(INSERT, "Keskmine distants (m):      " + str(avarageTotalDistance) + "\n")
        scrltxtData.insert(INSERT, "Keskmine kalorite kulu:     " + str(avarageTotalCalories) + "\n")
        scrltxtData.insert(INSERT, "Samme kokku:                " + str(totalSteps) + "\n")
        scrltxtData.insert(INSERT, "Käidud distants kokku (m):  " + str(totalDistance) + "\n")
        scrltxtData.insert(INSERT, "Kaloreid kulutatud kokku:   " + str(totalCalories) + "\n")
        scrltxtData.insert(INSERT, "Päevade arv:                " + str(counter) + "\n")
        scrltxtData.insert(INSERT, "-----------------------------------------" + "\n")
        clearTable()
        #table.bind("<Double-1>", onDoubleClickTotal)
        table.bind("<Double-1>", onDoubleClick)
        createTable()
        #table.insert("", 0, text=data[0][0] + " kuni " + data[-1][0], values=(data[0][0] + " kuni " + data[-1][0], avarageTotalSteps, avarageTotalDistance,
        #                                                                      avarageTotalCalories, totalSteps, totalDistance, totalCalories))
        table.insert("", 0, values=(data[0][0] + " kuni " + data[-1][0], totalSteps, totalDistance, totalCalories))

window = Tk()
window.title("Xioami Mi Band 2")
window.geometry("860x550")
center(window)
window.resizable(False, False)
getFileContents()

# Faili sisu
scrltxtData = scrolledtext.ScrolledText(window, width=41, height=21)
scrltxtData.grid(column=0, row=0, padx=10, pady=10)

btnShowData = Button(window, text="Näita terve CSV faili sisu", width=25, command=showData)
btnShowData.grid(column=0, row=1, padx=10, pady=5, sticky='w')

# Kuupäev
dateFrame = Frame(window)
dateFrame.grid(column=0, row=2, sticky='news', columnspan=4, padx=10, pady=5)

lbl1 = Label(dateFrame, text="Vali kuupäev: ", font=10).pack(side=LEFT)

cmbDay = ttk.Combobox(dateFrame, state='readonly', width=10)
cmbDay.bind('<<ComboboxSelected>>', getDatesData)
cmbDay['values'] = (datesList)
cmbDay.current(0)
cmbDay.pack(side=LEFT)

selected1 = IntVar(value=1)
radClear = Radiobutton(dateFrame, text="Üks päev korraga", value=1, variable=selected1, command=clearDataAndTable).pack(anchor=W, padx=5)
radAdd = Radiobutton(dateFrame, text="Mitu päeva korraga", value=2, variable=selected1, command=clearDataAndTable).pack(anchor=W, padx=5)

# Statistika
monthYearFrame = Frame(window)
monthYearFrame.grid(column=0, row=3, sticky='nw', padx=10, pady=10)

lbl2 = Label(monthYearFrame, text="Vali kuu ja aasta: ", font=10).pack(side=LEFT)

cmbMonthYear = ttk.Combobox(monthYearFrame, state='readonly', width=10)
cmbMonthYear.bind('<<ComboboxSelected>>', getMonthYearStats)
cmbMonthYear['values'] = (monthYearList)
cmbMonthYear.current(0)
cmbMonthYear.pack(side=LEFT)

selected2 = IntVar(value=1)
radMonthStats = Radiobutton(monthYearFrame, text="Kuu aja andmed", value=1, variable=selected2, command=getTotalStats).pack(anchor=W, padx=5)
radYearStats = Radiobutton(monthYearFrame, text="Aasta andmed", value=2, variable=selected2, command=getTotalStats).pack(anchor=W, padx=5)
radAlltimeStats = Radiobutton(monthYearFrame, text="Kogu aja andmed", value=3, variable=selected2, command=getTotalStats).pack(anchor=W, padx=5)

# Tabel
tableFrame = Frame(window)
tableFrame.grid(column=1, row=0, sticky='nw', padx=10, pady=10)

table = ttk.Treeview(tableFrame)

table["columns"]=("date", "totalSteps", "totalDistance", "totalCalories")
table['show'] = 'headings'
table.column("date", minwidth=170, width=170, anchor='center')
table.column("totalSteps", minwidth=90, width=90, anchor='center')
table.column("totalDistance", minwidth=100, width=100, anchor='center')
table.column("totalCalories", minwidth=90, width=90, anchor='center')
table.heading("date", text="Kuupäev")
table.heading("totalSteps", text="Sammud")
table.heading("totalDistance", text="Distants (m)")
table.heading("totalCalories", text="Kalorid")

window.mainloop()
