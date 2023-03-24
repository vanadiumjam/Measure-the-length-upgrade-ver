from tkinter import *
import tkinter.messagebox

def real_m():
    if len(_input.get()) == 0: # 아무것도 입력하지 않았으면
        tkinter.messagebox.showwarning("인상적인", "우리는 아무것도 찾을 수 없었다.")

    elif len(_input.get()) > 100: # 입력한 문자열의 길이가 100보다 크면
        tkinter.messagebox.showerror("실패의", "우리는 연산능력한도에 도달했다.")

    else: # 정상적이면.
        tkinter.messagebox.showinfo("성공적. 결과완성", "끼쁜소식! 우리는 해냈다. 그 문자(열)의 길이는 (공백포함) %s이다!!" % str(len(_input.get())))

def quit_window():
    # 윈도우 삭제
    tkinter.messagebox.askretrycancel("ERR", "창을(를) 종료할 수 없음.") #ㅋ
    root.destroy()
    root.quit()


root = Tk()
root.geometry("420x75+500+300")
root.title("mtl (measure the length)")

msg = Label(root, text="놀라운! 아무 것이나 입력하면 그 길이 출력한다.", font=("굴림", 10))
msg.grid(column=0, row=0)

start_button = Button(root, text="기록하다!", bg="blue", fg="white", command=real_m)
start_button.grid(row=1, column=1)

_input = Entry(root, width=50)
_input.grid(row=1, column=0)

cls_btn = Button(root, text="Quit", bg="red", fg="black", command=quit_window)
cls_btn.grid(row=2, column=0)



root.mainloop()
