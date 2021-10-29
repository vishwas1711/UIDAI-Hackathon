import tkinter as tk
import mysql.connector as sql

def AddressScreen():
    
    MainWin.withdraw()
    AdrWin.deiconify()
    AdrWin.state("zoomed")

    AdrWin.columnconfigure((0,1,2,), weight = 1)

    AdrFrame = tk.Frame(AdrWin)
    AdrFrame.grid(row = 1, column = 1)
    
    tk.Label(AdrWin,text = "User Window",font = LFont).grid(row = 0, column = 1, pady = 10)
    tk.Label(AdrFrame,text = "Enter aadhar number of the user ",font = LFont).grid(row = 0,column = 1)
    UserAA = tk.Entry(AdrFrame,font = LFont)
    UserAA.grid(row = 0, column = 2)
    tk.Label(AdrFrame,text = "Enter phone number of the user",font = LFont).grid(row = 0,column = 3)
    UserPHNO = tk.Entry(AdrFrame,font = LFont)
    UserPHNO.grid(row=0,column=4)
    tk.Button(AdrFrame,text = "Submit your details",command = ChoiceScreen,font = LFont).grid(row=1,column = 2,sticky = "e")

def Submit():
    OTPFrame = tk.Frame(MainWin)
    OTPFrame.grid(row = 2, column = 1, pady = 15)
    tk.Label(OTPFrame, text = "Enter phone number linked to the aadhar.", font = LFont).grid(row = 0, column=1)
    OTPEntry = tk.Entry(OTPFrame, font = LFont)
    OTPEntry.grid(row=2,column=1)
    SubmitPHNO = tk.Button(OTPFrame,text = "Enter phone number",command = AddressScreen,font = LFont)
    SubmitPHNO.grid(row = 3,column=1)

def ChoiceScreen():
    AdrWin.withdraw()
    ChoiceWin.deiconify()
    ChoiceWin.state("zoomed")
    ChoiceWin.columnconfigure((0,1,2,),weight=1)
    tk.Label(ChoiceWin,text = "Select your method of proving ownership of address",font=LFont).grid(row=0,column=1,pady = 5)
    tk.Button(ChoiceWin,text = "Proceed without documentation",font = LFont,command = WithoutDoc).grid(row = 1 , column = 1,sticky = "w")
    tk.Button(ChoiceWin,text = "Proceed with documentation",font = LFont).grid(row = 1, column = 1,sticky = "e")

def WithoutDoc():
    ChoiceWin.withdraw()
    Without.deiconify()
    Without.state("zoomed")
    Without.columnconfigure((0,1,2,),weight = 1)
    FrameOne = tk.Frame(Without)
    FrameOne.grid(row = 1,column=1)
    tk.Label(Without,text = "Proceeding without documentation.",font = LFont).grid(row=0,column=1)
    tk.Label(FrameOne,text = "The address of the landlord is : ",font = LFont).grid(row=0,column=0)
    tk.Label(FrameOne,text = "Insert some address in here.",font = LFont).grid(row = 0,column = 1)
    tk.Button(FrameOne, text = "Edit address",font = LFont,command = Editscreen).grid(row = 2,column = 1)
    tk.Button(FrameOne, text = "Enter new address",font = LFont,command = NewAddress).grid(row = 2,column = 2)

def NewAddress():
    Without.withdraw()
    NewAddressscreen.deiconify()
    NewAddressscreen.state("zoomed")
    NewAddressscreen.columnconfigure((0,1,2),weight = 1)
    NewAdrFrame = tk.Frame(NewAddressscreen)
    NewAdrFrame.grid(row=1,column=1)
    tk.Label(NewAddressscreen,text = "New address screen",font = LFont).grid(row = 0, column = 1)
    tk.Label(NewAdrFrame,text = "Enter a completely new address.",font = LFont).grid(row = 0,column=0)
    EntryNewAdr = tk.Entry(NewAddressscreen,font = LFont)
    EntryNewAdr.grid(row = 1,column=0)
    

def Editscreen():
    Without.withdraw()
    EditWin.deiconify()
    EditWin.state("zoomed")
    EditWin.columnconfigure((0,1,2),weight = 1)
    AdrDetails = tk.Frame(EditWin)
    AdrDetails.grid(row=1,column=1)
    tk.Label(EditWin,text = "Edit your address here.",font = LFont).grid(row=0,column=1)
    tk.Label(AdrDetails,text = "Door Number : ",font = LFont).grid(row=1,column=1)
    tk.Label(AdrDetails,text = "Flat Number : ",font = LFont).grid(row=2,column=1)
    tk.Label(AdrDetails,text = "Street Name : ",font = LFont).grid(row=3,column=1)
    tk.Label(AdrDetails,text = "Area : ",font = LFont).grid(row=4,column=1)
    tk.Label(AdrDetails,text = "City : ",font = LFont).grid(row=5,column=1)
    tk.Label(AdrDetails,text = "State : ",font = LFont).grid(row=6,column=1)
    DoorNo = tk.Entry(AdrDetails)
    DoorNo.grid(row=1,column=2)
    FlatNo = tk.Entry(AdrDetails)
    FlatNo.grid(row=2,column=2)
    StreetName = tk.Entry(AdrDetails)
    StreetName.grid(row=3,column=2)
    AreaName = tk.Entry(AdrDetails)
    AreaName.grid(row=4,column=2)
    CityName = tk.Entry(AdrDetails)
    CityName.grid(row=5,column=2)
    StateName = tk.Entry(AdrDetails)
    StateName.grid(row=6,column=2)

    tk.Button(AdrDetails,text = "Submit changes",font = LFont).grid(row=7,column=1)

MainWin = tk.Tk()
AdrWin = tk.Toplevel()
AdrWin.withdraw()
ChoiceWin = tk.Toplevel()
ChoiceWin.withdraw()
Without = tk.Toplevel()
Without.withdraw()
EditWin = tk.Toplevel()
EditWin.withdraw()
NewAddressscreen = tk.Toplevel()
NewAddressscreen.withdraw()
MainWin.state("zoomed")
MainWin.columnconfigure((0,1,2), weight = 1)
LFont = ("TkDefaultFont",16)

tk.Label(MainWin,text = "Hello world!",font = LFont).grid(row=0,column=1)
InfoFrame = tk.Frame(MainWin)
InfoFrame.grid(row=1,column=1)

tk.Label(InfoFrame,text = "Enter aadhar of landlord",font = LFont).grid(row=0, column = 0)
LordNum = tk.Entry(InfoFrame,font = LFont)
LordNum.grid(row = 1, columnspan = 1)

SubmitNo = tk.Button(InfoFrame, text = "Submit details",command = Submit, font = LFont)
SubmitNo.grid(row = 2, columnspan = 1, pady = 10)

MainWin.mainloop()
