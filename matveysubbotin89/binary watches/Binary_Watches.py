import datetime
from tkinter import Tk, Frame, BOTH, Canvas
import time




def time_now():
    time = [i for i in str(datetime.datetime.time(datetime.datetime.now())) if i != ':']
    index = time.index('.')
    time = time[:index]
    return time



class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.parent.title("Binary Watches by Matvii Subbotin")
        self.pack(fill = BOTH, expand = 1)
        canvas = Canvas(self)
        normal_time = time_now()
        normal_time = list(map(int, normal_time))
        binary_time = [bin(i) for i in normal_time]
        binary_time = [str(i)[2:] for i in binary_time]
        first_point_x = 40
        first_point_y = 130
        second_point_x = 70
        second_point_y = 160
        print(normal_time)
        print(binary_time)
        for id, gorisont in enumerate(binary_time):
            how_many_square = len(gorisont)
            for every_item in range(1, how_many_square+1):
                if gorisont[0 - every_item] == '1':
                    if id == 0 or id == 1:
                        color = "#0057ff"
                    elif id == 2 or id == 3:
                        color = "#24db3a"
                    elif id == 4 or id == 5:
                        color = "#fd8922"
                    canvas.create_rectangle(first_point_x, first_point_y, second_point_x, second_point_y, outline=color, fill=color)
                    #canvas.pack(fill=BOTH, expand=1)
                    first_point_y -= 40
                    second_point_y -= 40
                elif gorisont[0 - every_item] == '0':
                    color = "#bababa"
                    canvas.create_rectangle(first_point_x, first_point_y, second_point_x, second_point_y, outline=color, fill=color)
                    #canvas.pack(fill=BOTH, expand=1)
                    first_point_y -= 40
                    second_point_y -= 40

            first_point_y = 130
            second_point_y = 160
            if id == 0 or id == 2 or id == 4:
                first_point_x += 40
                second_point_x += 40
            elif id == 1 or id == 3:
                first_point_x += 60
                second_point_x += 60
        canvas.pack(fill=BOTH, expand=1)
#        Frame.update(self)
        self.parent.after(1000, self.initUI)

#        self.after(600, self.initUI)

#    def repeater(self):

#        self.initUI()
#        time.sleep(1)


def main():
    root = Tk()
    root.geometry("400x180+300+300")
    app = Window(root)
#    app.pack()
    app.update()

#    app.pack(fill=BOTH, expand=1)
    root.mainloop()


if __name__ == '__main__':
    main()






