from tkinter import *
import time
import random


root = Tk()
root.geometry("1600x700+0+0")
root.title("Bakasur")


def reset():
    rand.set("")
    fries.set("")
    large_fries.set("")
    burger.set("")
    cheese_burger.set("")
    fillet.set("")
    drinks.set("")
    tax.set("")
    sub_total.set("")
    total.set("")
    service_ch.set("")
    cost.set("")


def q_exit():
    root.destroy()


def price():
    roo = Tk()
    roo.geometry("600x220")
    roo.title("Price List")
    x = Frame(roo, width=600, height=220, relief=SUNKEN)
    x.pack(side=TOP)

    label_item = Label(x, font=("arial", 15, "bold"), text="Item", fg="red",
                       anchor="w")
    label_item.grid(row=0, column=0)
    label_price = Label(x, font=("arial", 15, "bold"), text="Price", fg="red",
                        anchor="w")
    label_price.grid(row=0, column=5)

    label_fries = Label(x, font=("arial", 15, "bold"), text="Fries",
                        fg="black", anchor="w")
    label_fries.grid(row=1, column=0)
    label_fries_price = Label(x, font=("arial", 15, "bold"), text="25",
                              fg="black", anchor="w")
    label_fries_price.grid(row=1, column=5)

    label_lg_fries = Label(x, font=("arial", 15, "bold"), text="Large Fries",
                           fg="black", anchor="w")
    label_lg_fries.grid(row=2, column=0)
    label_lg_fries_price = Label(x, font=("arial", 15, "bold"), text="40",
                                 fg="black", anchor="w")
    label_lg_fries_price.grid(row=2, column=5)

    label_burger = Label(x, font=("arial", 15, "bold"), text="Burger",
                         fg="black", anchor="w")
    label_burger.grid(row=3, column=0)
    label_burger_price = Label(x, font=("arial", 15, "bold"), text="35",
                               fg="black", anchor="w")
    label_burger_price.grid(row=3, column=5)

    label_ch_burger = Label(x, font=("arial", 15, "bold"), text="Cheese "
                                                                "Burger",
                            fg="black", anchor="w")
    label_ch_burger.grid(row=4, column=0)
    label_ch_burger_price = Label(x, font=("arial", 15, "bold"), text="45",
                                  fg="black", anchor="w")
    label_ch_burger_price.grid(row=4, column=5)

    label_fillet = Label(x, font=("arial", 15, "bold"), text="Fillet",
                         fg="black", anchor="w")
    label_fillet.grid(row=5, column=0)
    label_fillet_price = Label(x, font=("arial", 15, "bold"), text="20",
                               fg="black", anchor="w")
    label_fillet_price.grid(row=5, column=5)

    label_drinks = Label(x, font=("arial", 15, "bold"), text="Drinks",
                         fg="black", anchor="w")
    label_drinks.grid(row=6, column=0)
    label_drinks_price = Label(x, font=("arial", 15, "bold"), text="15",
                               fg="black", anchor="w")
    label_drinks_price.grid(row=6, column=5)

    roo.mainloop()


# Creating the top frame of the billing system page
tops = Frame(root, width=1600, height=500, relief=SUNKEN)
tops.pack(side=TOP)


local_time = time.asctime(time.localtime(time.time()))
label_info = Label(tops, font=('arial', 30, 'bold'), text="Billing System",
                   fg='blue', bd=10, anchor='w')
label_info.grid(row=0, column=0)

label_info = Label(tops, font=('arial', 30, 'bold'), text=local_time,
                   fg='red', bd=10, anchor='w')
label_info.grid(row=1, column=0)

operator = ""
text_Input = StringVar()


def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def equals():
    global operator
    sump_up = str(eval(operator))
    text_Input.set(sump_up)
    operator = ""


def clr_display():
    global operator
    operator = ""
    text_Input.set("")


def ref():
    r_num = random.randint(12000, 100000)
    r_ref = str(r_num)
    rand.set(r_ref)

    i_fries = float(fries.get()) if fries.get() != "" else 0.0
    i_lg_fries = float(large_fries.get()) if large_fries.get() != "" else 0.0
    i_burgers = float(burger.get()) if burger.get() != "" else 0.0
    i_ch_burger = float(cheese_burger.get()) if cheese_burger.get() != "" \
        else 0.0
    i_fillet = float(fillet.get()) if fillet.get() != "" else 0.0
    i_drinks = float(drinks.get()) if drinks.get() != "" else 0.0

    fries_cost = i_fries * 25
    lg_fries_cost = i_lg_fries * 40
    burger_cost = i_burgers * 35
    ch_burger_cost = i_ch_burger * 45
    fillet_cost = i_fillet * 20
    drinks_cost = i_drinks * 15

    o_cost = sum([fries_cost, lg_fries_cost, burger_cost, ch_burger_cost,
                  fillet_cost, drinks_cost])

    o_service_ch = o_cost * 0.05
    o_sub_total = o_cost + o_service_ch
    o_tax = o_sub_total * 0.18
    cost.set(str('%.2f' % o_cost))
    service_ch.set(str('%.2f' % o_service_ch))
    tax.set(str('%.2f' % o_tax))
    sub_total.set(str('%.2f' % o_sub_total))
    total.set(str('%.2f' % (o_sub_total + o_tax)))


# Creating the right frame of the billing system
f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
# Create display area of calculator

text_display = Entry(f2, font=('arial', 20, 'bold'),
                     textvariable=text_Input,
                     bd=5, bg="green", insertwidth=7, justify="right")
text_display.grid(columnspan=4)

# Create buttons of calculator
btn7 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="7", command=lambda: btn_click(7))
btn7.grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="8", command=lambda: btn_click(8))
btn8.grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="9", command=lambda: btn_click(9))
btn9.grid(row=2, column=2)

addition = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'),
                  fg="white", bg="black", text="+",
                  command=lambda: btn_click("+"))
addition.grid(row=2, column=3)

btn4 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="4", command=lambda: btn_click(4))
btn4.grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="5", command=lambda: btn_click(5))
btn5.grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="6", command=lambda: btn_click(6))
btn6.grid(row=3, column=2)

minus = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
               bg="black", text="-", command=lambda: btn_click("-"))
minus.grid(row=3, column=3)

btn1 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="1", command=lambda: btn_click(1))
btn1.grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="2", command=lambda: btn_click(2))
btn2.grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="3", command=lambda: btn_click(3))
btn3.grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'),
                  fg="white", bg="black", text="*", command=lambda: btn_click(
        "*"))
multiply.grid(row=4, column=3)

btn0 = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
              bg="black", text="0", command=lambda: btn_click(0))
btn0.grid(row=5, column=0)

clr = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
             bg="black", text="C", command=clr_display)
clr.grid(row=5, column=1)

dot = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'), fg="white",
             bg="black", text=".", command=lambda: btn_click("."))
dot.grid(row=5, column=2)

divide = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'),
                fg="white",
                bg="black", text="/", command=lambda: btn_click("/"))
divide.grid(row=5, column=3)

btn_equal = Button(f2, padx=16, pady=16, font=('arial', 20, 'bold'),
                   bg="black", fg="white", text="=", command=equals)
btn_equal.grid(columnspan=4)

# Creating the left frame of the billing system
f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)
rand = StringVar()
fries = StringVar()
large_fries = StringVar()
burger = StringVar()
fillet = StringVar()
sub_total = StringVar()
total = StringVar()
service_ch = StringVar()
drinks = StringVar()
tax = StringVar()
cost = StringVar()
cheese_burger = StringVar()

label_info = Label(f1, font=('arial', 16, 'bold'), text="Order No.r",
                   fg="black", bd=10, anchor="w")
label_info.grid(row=0, column=0)
text_info = Entry(f1, font=('arial', 17, 'bold'), textvariable=rand, bd=6,
                  insertwidth=4, bg="red", justify="right")
text_info.grid(row=0, column=1)


lbl_fries = Label(f1, font=('arial', 16, 'bold'), text="Fries", fg="black",
                  bd=10, anchor="w")
lbl_fries.grid(row=1, column=0)
text_fries = Entry(f1, font=('arial', 17, 'bold'), textvariable=fries, bd=6,
                   insertwidth=4, bg="red", justify="right")
text_fries.grid(row=1, column=1)


lbl_lg_fries = Label(f1, font=('arial', 16, 'bold'), text="Large Fries",
                     fg="black", bd=10, anchor="w")
lbl_lg_fries.grid(row=2, column=0)
text_lg_fries = Entry(f1, font=('arial', 17, 'bold'),
                      textvariable=large_fries, bd=6, insertwidth=4,
                      bg="red", justify="right")
text_lg_fries.grid(row=2, column=1)


lbl_burger = Label(f1, font=('arial', 16, 'bold'), text="Burger", fg="black",
                   bd=10, anchor="w")
lbl_burger.grid(row=3, column=0)
text_burger = Entry(f1, font=('arial', 17, 'bold'), textvariable=burger,
                    bd=6, insertwidth=4, bg="red", justify="right")
text_burger.grid(row=3, column=1)


lbl_ch_burger = Label(f1, font=('arial', 16, 'bold'), text="Cheese Burger",
                      fg="black", bd=10, anchor="w")
lbl_ch_burger.grid(row=4, column=0)
text_ch_burger = Entry(f1, font=('arial', 17, 'bold'),
                       textvariable=cheese_burger, bd=6, insertwidth=4,
                       bg="red", justify="right")
text_ch_burger.grid(row=4, column=1)


lbl_drinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", fg="black",
                   bd=10, anchor="w")
lbl_drinks.grid(row=5, column=0)
text_drinks = Entry(f1, font=('arial', 17, 'bold'), textvariable=drinks,
                    bd=6,
                    insertwidth=4, bg="red", justify="right")
text_drinks.grid(row=5, column=1)


lbl_fillet = Label(f1, font=('arial', 16, 'bold'), text="Fillet", fg="black",
                   bd=10, anchor="w")
lbl_fillet.grid(row=0, column=2)
text_fillet = Entry(f1, font=('arial', 17, 'bold'), textvariable=fillet,
                    bd=6, insertwidth=4, bg="red", justify="right")
text_fillet.grid(row=0, column=3)


label_cost = Label(f1, font=('arial', 16, 'bold'), text="Cost", fg="black",
                   bd=10, anchor="w")
label_cost.grid(row=1, column=2)
text_cost = Entry(f1, font=('arial', 17, 'bold'), textvariable=cost, bd=6,
                  insertwidth=4, bg="red", justify="right")
text_cost.grid(row=1, column=3)


label_service = Label(f1, font=('arial', 16, 'bold'), text="Service Charge",
                      fg="black", bd=10, anchor="w")
label_service.grid(row=2, column=2)
text_service = Entry(f1, font=('arial', 17, 'bold'),
                     textvariable=service_ch,
                     bd=6, insertwidth=4, bg="red", justify="right")
text_service.grid(row=2, column=3)


label_sub_total = Label(f1, font=('arial', 16, 'bold'), text="Sub Total",
                        fg="black", bd=10, anchor="w")
label_sub_total.grid(row=3, column=2)
text_sub_total = Entry(f1, font=('arial', 17, 'bold'),
                       textvariable=sub_total, bd=6, insertwidth=4,
                       bg="red", justify="right")
text_sub_total.grid(row=3, column=3)


label_tax = Label(f1, font=('arial', 16, 'bold'), text="Tax", fg="black",
                  bd=10, anchor="w")
label_tax.grid(row=4, column=2)
text_tax = Entry(f1, font=('arial', 17, 'bold'), textvariable=tax, bd=6,
                 insertwidth=4, bg="red", justify="right")
text_tax.grid(row=4, column=3)


label_total = Label(f1, font=('arial', 16, 'bold'), text="Total",
                    fg="black", bd=10, anchor="w")
label_total.grid(row=5, column=2)
text_total = Entry(f1, font=('arial', 17, 'bold'), textvariable=total,
                   bd=6, insertwidth=4, bg="red", justify="right")
text_total.grid(row=5, column=3)


button_total = Button(f1, padx=16, pady=8, bd=10, fg="white",
                      font=("arial", 16, "bold"), width=10, text="TOTAL",
                      bg="black", command=ref)
button_total.grid(row=8, column=1)


button_reset = Button(f1, padx=16, pady=8, bd=10, fg="white",
                      font=("arial", 16, "bold"), width=10, text="RESET",
                      bg="black", command=reset)
button_reset.grid(row=8, column=2)


button_exit = Button(f1, padx=16, pady=8, bd=10, fg="white",
                     font=("arial", 16, "bold"), width=10, text="EXIT",
                     bg="black", command=q_exit)
button_exit.grid(row=8, column=3)


button_price = Button(f1, padx=16, pady=8, bd=10, fg="white",
                      font=("arial", 16, "bold"), width=10, text="PRICE",
                      bg="black", command=price)
button_price.grid(row=8, column=0)


root.mainloop()
