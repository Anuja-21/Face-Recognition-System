from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from subprocess import call

def newWindow():
    root.destroy()
    call(["python","attendance/temp.py"])
    



class Face_Recognition_system :
    
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition System")
        
    
      #  first image
        #img=Image.open(r"C:\Users\atvha\OneDrive\Desktop\face recongition\attendance\screen pageimage\im.png")
        #img=img.resize((500,130),Image.Resampling.LANCZOS)
        #self.photoimg=ImageTk.PhotoImage(img)
        
        #first_label=Label(self.root,image=self.photoimg)
        #first_label.place(x=0,y=0,width=500,height=130)
        
        #second image
        #img1=img1.resize((600,200),Image.Resampling.LANCZOS)
        #self.photoimg1=ImageTk.PhotoImage(img1)
        
        #first_label=Label(self.root,image=self.photoimg1)
        #first_label.place(x=500,y=0,width=500,height=130)
        
         #third image
        #img2=Image.open(r"C:\Users\atvha\OneDrive\Desktop\face recongition\attendance\screen pageimage\eye.jpg")
       # img2=img.resize((500,130),Image.Resampling.LANCZOS)
      #  self.photoimg2=ImageTk.PhotoImage(img2)
        
      
      #  first_label=Label(self.root,image=self.photoimg2)
     #   first_label.place(x=1000,y=0,width=500,height=130)
        
         #bg image
        img3=Image.open(r"C:\Users\atvha\OneDrive\Desktop\face recongition\attendance\screen pageimage\kk.png")
        img3=img3.resize((2000,1000),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1600,height=650)
        
        title_lbl=Label(bg_image,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM    ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1600,height=45)
        
        img4=Image.open(r"C:\Users\atvha\OneDrive\Desktop\face recongition\attendance\screen pageimage\face2.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
   
        b1=Button(bg_image,image=self.photoimg4,cursor="hand2",command=newWindow)
        b1.place(x=300,y=150,width=220,height=220)
        
        b1_1=Button(bg_image,text="FACE DECTOR",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=300,y=350,width=220,height=40)

        b2_2=Button(bg_image,text="Click Me ",cursor="hand2",font=("times new roman",15,"bold"),bg="Black",fg="white",command=newWindow)
        b2_2.place(x=300,y=350,width=220,height=40)
        
        # b2=Button(bg_image,image=self.photoimg4,cursor="hand2",command=newWindow1)
        # b2.place(x=700,y=150,width=220,height=220)
        
        # b2_1=Button(bg_image,text="attendance sheet",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        # b2_1.place(x=700,y=350,width=220,height=40)
    
if __name__ == "__main__":
     root=Tk()
     obj=Face_Recognition_system(root)
     root.mainloop()
     
     
