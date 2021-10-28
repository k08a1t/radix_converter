from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def identify_type(type_in):
    if type_in == '2進数':
        return 2
    elif type_in == '8進数':
        return 8
    elif type_in == '10進数':
        return 10
    elif type_in == '16進数':
        return 16

def btn_click():

    get_type_in =combobox1.get()
    get_type_out=combobox2.get()

    if get_type_in == get_type_out :
        messagebox.showerror('エラー','同じ基数が選択されています')
        return

    out_txt.delete(0,END)

    if get_type_out == '10進数':
       out_txt.insert(END,int(in_txt.get(),identify_type(get_type_in)))
    else:
        txt=int(in_txt.get(),identify_type(get_type_in))
        if get_type_out == '2進数':
            out_txt.insert(END,bin(txt))
        elif get_type_out == '8進数':
            out_txt.insert(END,oct(txt))
        elif get_type_out == '16進数':
            out_txt.insert(END,hex(txt))

def reset_txt():
    in_txt.delete(0,END)
    out_txt.delete(0,END)

#ウィンドウの作成
root = Tk()
root.title('Radix Converter')
root.iconbitmap('icon.ico')
root.geometry('500x200')


pulldown_list=('2進数','8進数','10進数','16進数')


#ウィジェットの作成

image_t=PhotoImage(file='triangle_r.png')

label1=Label(root,text='変換前')
label2=Label(root,text='変換後')
label_image=Label(root,image=image_t)

combobox1=ttk.Combobox(root,values=pulldown_list)
combobox2=ttk.Combobox(root,values=pulldown_list)
combobox1.set('2進数')
combobox2.set('2進数')

in_txt=Entry(width=23)
out_txt=Entry(width=23)

button_c=Button(root,width=20,bg="#ffd59e",text='Convert!',command=btn_click)
button_reset=Button(root,width=10,bg="#cee6ff",text='reset',command=reset_txt)

#レイアウト
label1.place(x=50,y=20)
label2.place(x=300,y=20)
label_image.place(x=210,y=47)

combobox1.place(x=50,y=50)
combobox2.place(x=300,y=50)

in_txt.place(x=50,y=90)
out_txt.place(x=300,y=90)
button_c.place(x=170,y=140)
button_reset.place(x=365,y=140)

#ウィンドウの表示開始
root.mainloop()