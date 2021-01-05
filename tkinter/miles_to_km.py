from tkinter import *
X_PADDING = 20
Y_PADDING = 20
ENTRY_WIDTH = 10
#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=300)

# Labels
is_equal_to_label = Label(text="Is equal to")
is_equal_to_label.grid(row=1, column = 0)
is_equal_to_label.config(padx=X_PADDING, pady = Y_PADDING)

miles_label = Label(text="miles")
miles_label.grid(row=0, column = 2)
miles_label.config(padx=X_PADDING, pady = Y_PADDING)

km_label = Label(text="km")
km_label.grid(row=1, column = 2)
km_label.config(padx=X_PADDING, pady = Y_PADDING)

number_of_km_label = Label(text="Is equal to")
number_of_km_label.grid(row=1, column = 1)
number_of_km_label.config(padx=X_PADDING, pady = Y_PADDING)

# Button
def convert_miles_to_km():
    miles_to_km_conversion_factor = 1.609344
    number_of_miles = float(entry.get())
    number_of_km = number_of_miles * miles_to_km_conversion_factor
    number_of_km_label.config(text="{:0.2f}".format(number_of_km))


# Calls convert_miles_to_km() when pressed
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row = 2, column = 1)
calculate_button.config(padx=50, pady= 50)


#Entries
entry = Entry(width=ENTRY_WIDTH)
entry.grid(row = 0, column = 1)

#Add some text to begin with
entry.insert(END, string="# of Miles")
window.mainloop()