#pip install customtkinter
import customtkinter
import tkinter.messagebox
euro_result = []

# Function that takes a string x, then multiplies each element by a rate y
def poundconverter(x, y):
    poundlist = []
    poundstring = x.split(',')
    for i in poundstring:
        num = float(i)
        num = num * float(y)
        num = round(num, 2)
        poundlist.append(num)
    return poundlist

#function to make the buttons function with the conversion function
def calculate_conversion():
    global euro_result
    pound_input = euroconvert_entry1.get()
    exchange_rate = euroconvert_entry2.get()
    try:
        euro_result = poundconverter(pound_input, exchange_rate)

        # Create a new window to display the table
        conversion_window = customtkinter.CTk()
        conversion_window.geometry("400x300")
        conversion_window.title("Conversion Results")

        # Create a Label widget to display the table header
        header_label = customtkinter.CTkLabel(conversion_window, text="| Sterling ---> Euro |")
        header_label.pack()

        # Loop to display the rows in the table
        for i in range(len(euro_result)):
            row_label = customtkinter.CTkLabel(conversion_window, text=f"| {pound_input.split(',')[i]} ---> {euro_result[i]} Euros |")
            row_label.pack()

        conversion_window.mainloop()
    except ValueError:
        # Handle invalid input or conversion errors in a pop-up dialog
        tkinter.messagebox.showerror("Error", "Invalid input or conversion error. Please check your inputs.")

def retailpricehandler():
    global euro_result
    tickonoff = checkbox_1.get()
    try:
        if tickonoff == 1:
            retailinput = euro_result  # Use the global euro_result from previous sterling conversion instead of the new entry
        else:
            retailinput = retailconvert_entry1.get()
            retailinput = retailinput.split(',')
            euro_result = retailinput
        x2_list = retailprice(retailinput, 'A')
        x3_list = retailprice(retailinput, 'B')

        # Create a new window to display the table
        retail_window = customtkinter.CTk()
        retail_window.geometry("400x300")
        retail_window.title("Retail Prices")

        # Create a Label widget to display the table header
        header_label = customtkinter.CTkLabel(retail_window, text="| Original ---> x2 + VAT ---> x3 |")
        header_label.pack()

        # Loop to display the rows in the table
        for i in range(len(euro_result)):
            row_label = customtkinter.CTkLabel(retail_window, text=f"| {euro_result[i]} ---> {x2_list[i]} ---> {x3_list[i]} |")
            row_label.pack()

        retail_window.mainloop()
    except ValueError:
        tkinter.messagebox.showerror("Error", "Invalid input. Please check your inputs.")

# Function that takes a list x, then if y is A it doubles all numbers + VAT, or if y is B it triples all numbers
def retailprice(x, y):
    retaillist = []
    if (y == 'a') or (y == 'A'):
        for i in x:
            num = float(i)
            num2 = num * 2
            num3 = num * (0.23)
            num4 = num2 + num3
            num4 = round(num4, 2)
            retaillist.append(num4)
        return retaillist
    if (y == 'b') or (y == 'B'):
        for i in x:
            num = float(i)
            num = num * 3
            num = round(num, 2)
            retaillist.append(num)
        return retaillist

#setting up basic window
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("800x550")

#adding small frame inside
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

#header text
header = customtkinter.CTkLabel(master= frame, text="Hardware Store Utility Tool", font=("Roboto", 40))
header.pack(pady=12, padx=10)

#tabs
tabview = customtkinter.CTkTabview(master= frame, width=750, height=500)
tabview.pack(pady = 10, padx = 10)
tabview.add("EURO Converter")
tabview.add("Retail Pricing")
tabview.add("About")
tabview.tab("EURO Converter").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
tabview.tab("Retail Pricing").grid_columnconfigure(0, weight=1)
tabview.tab("About").grid_columnconfigure(0, weight=1)

#euroconverter tab
euro_convert_frame = customtkinter.CTkFrame(tabview.tab("EURO Converter"))
euro_convert_frame.pack(fill="both", expand=True)
euro_descrip_label = customtkinter.CTkLabel(euro_convert_frame, font=("Roboto", 25), text="Please input your list of comma-separated numbers")
euro_descrip_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
euroconvert_entry1 = customtkinter.CTkEntry(euro_convert_frame, placeholder_text="Here!", width=300)
euroconvert_entry1.grid(row=1, column=0, padx=10, pady=10)
euro_descrip_label2 = customtkinter.CTkLabel(euro_convert_frame, font=("Roboto", 25), text="Please input the current STERLING to EURO rate")
euro_descrip_label2.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
euroconvert_entry2 = customtkinter.CTkEntry(euro_convert_frame, placeholder_text="Here!", width=300)
euroconvert_entry2.grid(row=3, column=0, padx=10, pady=10)
convert_button = customtkinter.CTkButton(euro_convert_frame, fg_color="black", border_width=2, text_color=("white"), text="CALCULATE", hover_color="grey", width=300, height=50)
convert_button.grid(row=4, column=0, padx=10, pady=10)
convert_button.configure(command=calculate_conversion) #start the process going to the calculate conversion function

#retailprice tab
retail_price_frame = customtkinter.CTkFrame(tabview.tab("Retail Pricing"))
retail_price_frame.pack(fill="both", expand=True)
retail_descrip_label = customtkinter.CTkLabel(retail_price_frame, font=("Roboto", 25), text="Please input your list of comma-separated numbers")
retail_descrip_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
retailconvert_entry1 = customtkinter.CTkEntry(retail_price_frame, placeholder_text="Here!", width=300)
retailconvert_entry1.grid(row=1, column=0, padx=10, pady=10)
retail_descrip_label2 = customtkinter.CTkLabel(retail_price_frame, font=("Roboto", 25), text="Or")
retail_descrip_label2.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
checkbox_1 = customtkinter.CTkCheckBox(retail_price_frame, text="Tick this box to use list of previously converted EURO values", font=("Roboto", 24), hover_color="grey", onvalue=1, offvalue=0)
checkbox_1.grid(row=3, column=0, padx=10, pady=10)
convert_button2 = customtkinter.CTkButton(retail_price_frame, fg_color="black", border_width=2, text_color=("white"), text="CALCULATE", hover_color="grey", width=300, height=50)
convert_button2.grid(row=4, column=0, padx=10, pady=10)
convert_button2.configure(command= retailpricehandler)

#about tab
about_frame = customtkinter.CTkFrame(tabview.tab("About"))  # Create a frame for the About tab
about_frame.pack(fill="both", expand=True)  # Make the frame fill the tab
abouttext = customtkinter.CTkTextbox(about_frame, font=("Roboto", 25), wrap="word")
abouttext.insert(1.0, text="This is a utility tool made by Luke Molony, for the Hardware Store. It attempts to make the process of pricing new stock easier!\nPlans for the future:\n1)Add input validation (COMPLETE)\n2)Add OCR for price input.\n3)Create an app for android.\n4)Port the app over to apple")
abouttext.pack(fill="both", expand=True)
abouttext.configure(state="disabled")

#menubutton1 = customtkinter.CTkButton(master= frame, text="STERLING to EURO", command=poundconverter)

root.mainloop()