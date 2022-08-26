import time
from tkinter import *
from PIL import Image
import image_colors
from tkinter import messagebox
import math
from logistic import Road

def load_txt():
    f=open("image_resource.txt")
    arr=[]
    for i in f:
        arr.append(list(map(int, i.split())))
    f.close()
    return arr

def load_rhouse():
    f = open("houses.txt")
    res = []
    for i in f:
        l = list(i.split())
        for n in range(0, 10):
            l[n] = float(l[n])
        for n in range(11, 13):
            l[n] = float(l[n])
        l[10] = int(l[10])
        l[13] = int(l[13])
        l[14] = bool(l[14])
        l[15] = int(l[15])
        l[16] = bool(l[16])
        new_r = [[l[0], l[1]], [l[2], l[3]], [l[4], l[5]], [l[6], l[7]],
                 [l[8], l[9]], l[10], [l[11], l[12]], l[13], l[14], l[15], l[16]]
        res.append(new_r)
        print(res)
    return res

image = Image.open('jelly.png')
draw_map = {(0, 0, 255, 255): (121, 142, 148, 255),
            (0, 0, 0, 255): (200,200,200, 255),
            (255, 255, 0, 255): (210, 204, 224, 255),
            (255, 0, 0, 255): (251, 250, 246, 255),
            (0, 255, 0, 255): (160, 205, 217, 255),
            (0, 255, 255, 255): (109, 181, 146, 255)}
draw_map2 = {(0, 0, 255, 255): -1,
             (0, 0, 0, 255): -1,
             (255, 255, 0, 255): -1,
             (255, 0, 0, 255): -1,
             (0, 255, 0, 255): 0,
             (0, 255, 255, 255): 0}
#image_colors.ImageColors().recognize_color(draw_map2)
arr = image.load()
w, h = image.size
print(image.size)
for x in range(w):
    try:
        for y in range(h):
            e = list(arr[x, y])
            for i in range(len(e)):
                e[i] = round((e[i]/255))*255
            e = tuple(e)
            arr[x, y] = draw_map[e]
    except:
        arr[x, y] = (255,255,255,255)
        pass


mapx, mapy = 0, 0
apx, apy = 0, 0
pointx = 0
pointy = 0
movcur = False
mode=0
on_morn=True
#0-двигается
#1-домик
pixel_map=load_txt()
#print(len(pixel_map[0]))
r_house=load_rhouse()
new_info=0
new_size=0
new_hight=0
new_type=0
index_variant_of_type_home=0
panel = 0
house_cords=[]
index_home_now=0
on_rotate=False
on_move=False
rubber_on = False
sost = []
type_home=["жилой","жилой элитный", "офис"]
type_home_s = [25, 5, 10]
roads = []
road_w = 80
road_h = 40
metro_img=[]
metro=[[[1876, 147], [1876-56, 147+20], [4200, 9600], [4200]], [[1900, 147], [1900, 147+20], [4000, 9600], [4000]]]
#что менять  я призрак призрак

def morn(event):
    global panel
    global  on_morn
    global sost
    on_morn=not on_morn
    panel.config(image=sost[0])
    if on_morn:
        panel.config(image=sost[0])
    else:
        panel.config(image=sost[1])

def create_roads():
    global roads
    #1
    road1 = Road(1, [1705, 163], [160, 214], [1380, 781], [1971, 1562], [], [[945, 246], [755, 160]])
    #2
    road2 = Road(2, [77, 192], [96, 660], [1953], [4883], [], [[102, 394]])
    # 3
    road3 = Road(3, [160, 617], [1284, 506], [1072, 789], [1357, 1337], [4], [[1196,595], [1082, 491]])
    # 4
    road4 = Road(4, [1372, 528], [1877, 326], [1227, 1091], [1379, 1408], [3], [[1686,468], [1761, 328]])
    roads=[road1, road2, road3, road4]
create_roads()
def save_pixel_rh(bob):
    #print("Hello")
    global pixel_map
    a, b, c, d , center= bob[1], \
                         bob[2], \
                         bob[3], \
                         bob[4], \
                         bob[0]
    if b[1]!=a[1]:
        if b[0]==a[0]:
            ab_k=10**9
        else:
            ab_k=(abs(b[1]-a[1])/abs(b[0]-a[0]))*(b[1]-a[1])/abs(b[1]-a[1])*(b[0]-a[0])/abs(b[0]-a[0])
    else:
        ab_k=0

    if (c[1]!=b[1]):
        if b[0]==c[0]:
            bc_k=10**9
        else:
            bc_k = (abs(c[1] - b[1]) / abs(c[0] - b[0])) * (c[1] - b[1]) / abs(c[1] - b[1]) * (c[0] - b[0]) / abs(c[0] - b[0])
    else:
        bc_k = 0

    if(c[1]!=d[1]):
        if c[0]==d[0]:
            cd_k=10**9
        else:
            cd_k = (abs(d[1] - c[1]) / abs(d[0] - c[0])) * (d[1] - c[1]) / abs(d[1] - c[1]) * (d[0] - c[0]) / abs(d[0] - c[0])
    else:
        cd_k = 0

    if (d[1]!=a[1]):
        if d[0]==a[0]:
            da_k=10**9
        else:
            da_k = (abs(a[1] - d[1]) / abs(a[0] - d[0])) * (a[1] - d[1]) / abs(a[1] - d[1]) * (a[0] - d[0]) / abs(a[0] - d[0])
    else:
        da_k = 0
    ab_b=a[1]-a[0]*ab_k
    bc_b = b[1] - b[0] * bc_k
    cd_b = d[1] - d[0] * cd_k
    da_b = a[1] - a[0] * da_k
    R=((center[0]-a[0])**2+(center[1]-a[1])**2)**0.5
    for x in range(int(center[0]-R), round(center[0]+R)):
        for y in range(int(center[1]-R), round(center[1]+R)):
            if a[1]<b[1] and a[1]<c[1] and a[1]<d[1]:
                if x*bc_k+bc_b>y and x*cd_k+cd_b>y and x*ab_k+ab_b<y and x*da_k+da_b<y:
                    if pixel_map[y][x]==0:
                        pixel_map[y][x] = bob[9]
            if b[1]<a[1] and b[1]<c[1] and b[1]<d[1]:
                if x*bc_k+bc_b<y and x*cd_k+cd_b>y and x*ab_k+ab_b<y and x*da_k+da_b>y:
                    if pixel_map[y][x] == 0:
                        pixel_map[y][x] = bob[9]
            if c[1]<b[1] and c[1]<a[1] and c[1]<d[1]:
                if x*bc_k+bc_b<y and x*cd_k+cd_b<y and x*ab_k+ab_b>y and x*da_k+da_b>y:
                    if pixel_map[y][x] == 0:
                        pixel_map[y][x] = bob[9]
            if d[1]<b[1] and d[1]<c[1] and d[1]<a[1]:
                if x*bc_k+bc_b>y and x*cd_k+cd_b<y and x*ab_k+ab_b>y and x*da_k+da_b<y:
                    if pixel_map[y][x] == 0:
                        pixel_map[y][x] = bob[9]
def save_hoses():
    global mode
    if mode==0:
        text = ""
        for i in r_house:
            line = ""
            for a in range(0, len(i)):
                if a<5 or a==6:
                    line = line+str(i[a][0])+" "+str(i[a][1])+" "
                else:
                    line+=str(i[a])+" "
            text+=line+"\n"
            save_pixel_rh(i)
        f = open("houses.txt", "w")
        f.write(text)
        print(text)
        f.close()

        text = ""
        for y in pixel_map:
            line = ""
            for x in y:
                line = line + str(x) + " "
            line+="\n"
            text+=line
        f = open("image_resource.txt", "w")
        f.write(text)
        f.close()
        messagebox.showinfo(title="Success", message="Изменения сохранены")
def start_rotate():
    global on_rotate
    global mode
    if mode ==3:
        on_rotate=not on_rotate
def rotate():
    global r_house
    global index_home_now
    global on_rotate
    if on_rotate:
        speed=3.14/180
        a, b, c, d, center = r_house[index_home_now][1],\
                             r_house[index_home_now][2],\
                             r_house[index_home_now][3],\
                             r_house[index_home_now][4],\
                             r_house[index_home_now][0]
        sap_mass=[]
        for i in range(1, 5):
            p=r_house[index_home_now][i].copy()
            p[0]=p[0]-center[0]
            p[1] = p[1] - center[1]
            ang=0
            L=(p[0]*p[0]+p[1]*p[1])**0.5
            if p[1]>=0:
                ang=math.acos(p[0]/L)
            else:
                ang = -math.acos(p[0] / L)
            ang+=speed
            p[0]=L*math.cos(ang)
            p[1] = L * math.sin(ang)
            p[0]=center[0]+p[0]
            p[1]=center[1]+p[1]
            r_house[index_home_now][i]=p
def build():
    global index_variant_of_type_home
    global new_size
    global new_hight
    global house_cords
    global r_house
    global mode
    global index_home_now
    global on_rotate
    flag = True
    #не злись на панду я стараюсь
    size=new_size.get()
    hight = new_hight.get()
    if "x" not in size:
        print("1")
        messagebox.showwarning(title="Error", message="Неправильный формат площади")
        return
    try:
        size = list(map(int, size.split("x")))
        if len(size)!=2:
            print("2")
            messagebox.showwarning(title="Error", message="Неправильный формат площади")
            return
    except:
        print(size)
        messagebox.showwarning(title="Error", message="Неправильный формат площади")
        return
    try:
        hight=int(hight)
        if hight<=0:
            print("4")
            messagebox.showwarning(title="Error", message="Неправильная высота")
            return
    except:
        print("5")
        messagebox.showwarning(title="Error", message="Неправильная высота")
        return
    #добавление дома : координата центра\ и четырех вершин
    id = 1
    while True:
        flag = False
        for i in r_house:
            if i[9]==id:
                flag = True
                break
        if flag:
            id+=1
        else:
            break

    r_house.append([house_cords,   [house_cords[0]+size[0]/2, house_cords[1]+size[1]/2],
                    [house_cords[0]+size[0]/2, house_cords[1]-size[1]/2],
                    [house_cords[0]-size[0]/2, house_cords[1]-size[1]/2],
                    [house_cords[0]-size[0]/2, house_cords[1]+size[1]/2],
                    index_variant_of_type_home, size, hight, False, id , False])

    new_info.destroy()
    mode=3

    index_home_now=len(r_house)-1
    on_rotate=True
    rotate()
    on_rotate=False
def line(x1, y1, x2, y2):
    c.create_line(x1, y1, x2, y2)
def check():
    #print("Hello")
    global pixel_map
    a, b, c, d , center= r_house[index_home_now][1], \
                         r_house[index_home_now][2], \
                         r_house[index_home_now][3], \
                         r_house[index_home_now][4], \
                         r_house[index_home_now][0]
    if b[1]!=a[1]:
        if b[0]==a[0]:
            ab_k=10**9
        else:
            ab_k=(abs(b[1]-a[1])/abs(b[0]-a[0]))*(b[1]-a[1])/abs(b[1]-a[1])*(b[0]-a[0])/abs(b[0]-a[0])
    else:
        ab_k=0

    if (c[1]!=b[1]):
        if b[0]==c[0]:
            bc_k=10**9
        else:
            bc_k = (abs(c[1] - b[1]) / abs(c[0] - b[0])) * (c[1] - b[1]) / abs(c[1] - b[1]) * (c[0] - b[0]) / abs(c[0] - b[0])
    else:
        bc_k = 0

    if(c[1]!=d[1]):
        if c[0]==d[0]:
            cd_k=10**9
        else:
            cd_k = (abs(d[1] - c[1]) / abs(d[0] - c[0])) * (d[1] - c[1]) / abs(d[1] - c[1]) * (d[0] - c[0]) / abs(d[0] - c[0])
    else:
        cd_k = 0

    if (d[1]!=a[1]):
        if d[0]==a[0]:
            da_k=10**9
        else:
            da_k = (abs(a[1] - d[1]) / abs(a[0] - d[0])) * (a[1] - d[1]) / abs(a[1] - d[1]) * (a[0] - d[0]) / abs(a[0] - d[0])
    else:
        da_k = 0

    ab_b=a[1]-a[0]*ab_k
    bc_b = b[1] - b[0] * bc_k
    cd_b = d[1] - d[0] * cd_k
    da_b = a[1] - a[0] * da_k
    R=((center[0]-a[0])**2+(center[1]-a[1])**2)**0.5


    #line(0, ab_b, 2000, 2000*ab_k+ab_b)
    #line(0, bc_b, 2000, 2000 * bc_k + bc_b)
    #line(0, cd_b, 2000, 2000 * cd_k + cd_b)
    #line(0, da_b, 2000, 2000 * da_k + da_b)
    for x in range(int(center[0]-R), round(center[0]+R)):
        for y in range(int(center[1]-R), round(center[1]+R)):
            if a[1]<b[1] and a[1]<c[1] and a[1]<d[1]:
                if x*bc_k+bc_b>y and x*cd_k+cd_b>y and x*ab_k+ab_b<y and x*da_k+da_b<y:
                    if pixel_map[y][x]!=0:
                        return False

            if b[1]<a[1] and b[1]<c[1] and b[1]<d[1]:
                if x*bc_k+bc_b<y and x*cd_k+cd_b>y and x*ab_k+ab_b<y and x*da_k+da_b>y:
                    if pixel_map[y][x]!=0:
                        return False
            if c[1]<b[1] and c[1]<a[1] and c[1]<d[1]:
                if x*bc_k+bc_b<y and x*cd_k+cd_b<y and x*ab_k+ab_b>y and x*da_k+da_b>y:
                    if pixel_map[y][x]!=0:
                        return False
            if d[1]<b[1] and d[1]<c[1] and d[1]<a[1]:
                if x*bc_k+bc_b>y and x*cd_k+cd_b<y and x*ab_k+ab_b>y and x*da_k+da_b<y:
                    if pixel_map[y][x]!=0:
                        return False

    return True

    #я просто путаюсь где что уяза
def add(event):
    global  mode
    if mode==3:
        if (r_house[index_home_now][8]):
            r_house[index_home_now][10]=True
            mode = 0
            save_pixel_rh(r_house[index_home_now])
        else:
            messagebox.showwarning(title="Error", message="Невозможно разместить дом")
            return
def draw_h():
    global mapy
    global mapx
    global  r_house
    global c
    for i in r_house:

        color="blue"
        if i[8]==False:
            color="red"

        c.create_polygon(i[1][0]+mapx, i[1][1]+mapy, i[2][0]+mapx, i[2][1]+mapy, i[3][0]+mapx, i[3][1]+mapy, i[4][0]+mapx, i[4][1]+mapy, fill=color)
def change_type():
    global index_variant_of_type_home
    global new_type
    global type_home
    if index_variant_of_type_home<len(type_home)-1:
        index_variant_of_type_home+=1
    else:
        index_variant_of_type_home=0
    new_type["text"]=type_home[index_variant_of_type_home]
def back_0():
    global  mode
    global new_info
    new_info.destroy()
    mode=0
def create_house(x, y):

    global  mode
    global new_info
    global type_home
    global new_hight
    global new_size
    global new_type
    global index_variant_of_type_home
    global house_cords

    index_variant_of_type_home=0
    house_cords=[]

    house_cords.append(x)
    house_cords.append(y)
    new_info=Toplevel()
    new_info.title("Введите информацию о доме")
    mode=2

    new_info.protocol("WM_DELETE_WINDOW", back_0)
    text1 = Label(new_info, width=50, text="Площадь, например(В МЕТРАХ):50x100")
    new_size = Entry(new_info, width=50)
    new_size.insert(0, "  x  ")

    text2 =Label(new_info, width=50, text="Количество этажей, например:20")
    new_hight= Entry(new_info, width=50)

    text3 = Label(new_info, width=50, text="Тип дома (жилой дом или офис)")
    new_type = Button(new_info, width=30, command=change_type, text="жилой", background="white")
    Build = Button(new_info, width=10, command=build, text="Построить", background="blue")


    text1.pack()
    new_size.pack()
    text2.pack()
    new_hight.pack()
    text3.pack()
    new_type.pack()
    Build.pack()
def rabber():
    global mode
    if mode==0:
        mode=5
    elif mode==5:
        mode=0
def start_house():
    global mode
    if mode ==0:
        mode=1
    else:
        return
def callback(event):
    global mapy
    global mapx
    global apy
    global apx
    global pointx
    global pointy
    global movcur
    global  on_move
    global rubber_on
    print(event.x - mapx, event.y - mapy)
    if mode==0:
        movcur = True
        apy = mapy
        apx = mapx
        pointx = event.x
        pointy = event.y
        #print("clicked at", event.x, event.y)
    if mode==3:
        on_move=True
    if mode==5:
        rubber_on=True
def draw_gui():
    global roads
    global road_w
    global road_h
    global mapx
    global mapy
    global metro_img
    global metro
    global b_mode
    if mode==0:
        for b_mode in range(len(metro)):
            m=metro[b_mode]
            c.create_image(m[0][0]+mapx, m[0][1]+mapy, image=metro_img[b_mode])
            c.create_rectangle(m[1][0] + mapx, m[1][1] + mapy, m[1][0] + road_h + mapx, m[1][1] + road_h + mapy, fill="white")
            c.create_text(m[1][0] + mapx+5, m[1][1]+ mapy,
                          text=str(int(metro[b_mode][3][0])), anchor=NW)
            if len(metro[b_mode][3])>1:
                c.create_text(m[1][0] + mapx+5, m[1][1] + mapy+18,
                              text=str(int(metro[b_mode][3][1])), anchor=NW)

        for i in roads:
            for n in range(0, len(i.tables)):
                t = i.tables[n]
                r = i.previos[n]*i.previos[n]/i.max_people[n]/i.max_people[n] * 255
                if r>255:
                    r = 255
                b = (1- i.previos[n]*i.previos[n]/i.max_people[n]/i.max_people[n]) * 255
                if b <0:
                    b = 0
                r = int(r)
                b = int(b*1.2)
                if b>255:
                    b=255
                al = "0123456789ABCDEF"
                nr=hex(r)[2:]
                nb = hex(b)[2:]
                if len(nr)==1:
                    nr = "0"+nr
                if len(nb)==1:
                    nb = "0"+nb

                color="#"+nr+nb+"77"
                c.create_rectangle(t[0] + mapx, t[1] + mapy, t[0]+road_w + mapx, t[1]+road_h + mapy, fill="white")
                c.create_text(t[0] + mapx + 5, t[1] + mapy,
                              text=str(int(i.previos[n])) + " " + str(int(100*i.previos[n]/i.max_people[n]))+"%",
                              fill=color, anchor=NW)
                if len(i.new)>0:
                    r = i.new[n] * i.new[n] / i.max_people[n] / i.max_people[n] * 255
                    if r > 255:
                        r = 255
                    b = (1 - i.new[n] * i.new[n] / i.max_people[n] / i.max_people[n]) * 255
                    if b < 0:
                        b = 0
                    r = int(r)
                    b = int(b * 1.2)
                    if b > 255:
                        b = 255
                    al = "0123456789ABCDEF"
                    nr = hex(r)[2:]
                    nb = hex(b)[2:]
                    if len(nr) == 1:
                        nr = "0" + nr
                    if len(nb) == 1:
                        nb = "0" + nb

                    color = "#" + nr + nb + "77"
                    c.create_text(t[0] + mapx + 5, t[1] + mapy+18,
                                  text=str(int(i.new[n])) + " " + str(int(100 * i.new[n] / i.max_people[n])) + "%",
                                  fill=color, anchor=NW)


def calculate_distance_between_line_and_point(x1, y1, x2, y2, point_x, point_y):
    a = (point_x-x1)**2+(point_y-y1)**2
    b = (point_x - x2) ** 2 + (point_y - y2) ** 2
    c = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5
    x = (b+c**2-a)/(2*c)
    l=(b-x**2)**0.5

    ac = [point_x-x1, point_y-y1]
    bc = [point_x - x2, point_y - y2]
    ab  = [x2-x1, y2-y1]
    ba = [x1 - x2, y1 - y2]
    if (ac[0]*ab[0]+ac[1]*ab[1]<0 or bc[0]*ba[0]+bc[1]*ba[1]<0):
        return min([a**0.5, b**0.5])
    return l
def calculate_work_load_of_road(number_of_people):
    return number_of_people * 0.4 / 1.2 * 0.35
def make():
    global r_house
    global roads
    global on_morn
    global type_home_s
    global metro
    for b_mode in range(0, len(metro)):
        if len(metro[b_mode][3])>1:
            metro[b_mode][3][0]=metro[b_mode][3][1]
            k=0
            for i in r_house:
                add_people=i[6][0] * i[6][1] * i[7] / type_home_s[i[5]]
                add_people=add_people*0.6*0.35*0.4
                k+=add_people
            if on_morn:
                metro[b_mode][3][1]=metro[b_mode][2][0]+k
            else:
                metro[b_mode][3][1] = metro[b_mode][2][1] + k
        else:
            k=0
            for i in r_house:
                add_people=i[6][0] * i[6][1] * i[7] / type_home_s[i[5]]
                add_people=add_people*0.6*0.35*0.4
                k+=add_people
            if on_morn:
                metro[b_mode][3].append(metro[b_mode][2][0]+k)
            else:
                metro[b_mode][3].append(metro[b_mode][2][1]+k)



    for v in roads:
        if len(v.new)>0:
            v.previos = v.new
            v.new = v.base_people
    for i in r_house:
        mn = 0
        minim = 6000
        for u in range(0, len(roads)):
            r = roads[u]
            l = calculate_distance_between_line_and_point(r.a[0], r.a[1], r.b[0], r.b[1], i[0][0], i[0][1])
            if l<minim:
                mn = u
                minim = l

        add_people = calculate_work_load_of_road(i[6][0] * i[6][1] * i[7] / type_home_s[i[5]])
        road = roads[mn]
        print(road.id)
        if road.id==2:
            roads[mn].new = [roads[mn].base_people[0] + add_people]
        if road.id==1:
            if on_morn:
                roads[mn].new = [roads[mn].base_people[0] + add_people * 0.8,
                                 roads[mn].base_people[1] + add_people * 0.2]
            else:
                roads[mn].new = [roads[mn].base_people[0] + add_people * 0.2,
                                 roads[mn].base_people[1] + add_people * 0.8]
        if road.id==3:
            if on_morn:
                roads[mn].new = [roads[mn].base_people[0] + add_people * 0.8,
                                 roads[mn].base_people[1] + add_people * 0.2]
            else:
                roads[mn].new = [roads[mn].base_people[0] + add_people * 0.2,
                                 roads[mn].base_people[1] + add_people * 0.8]
        if road.id==4:
            if on_morn:
                roads[mn].new = [roads[mn].base_people[0] + add_people * 0.8,
                                 roads[mn].base_people[1] + add_people * 0.2]
            else:
                roads[mn].new = [roads[mn].base_people[0] + add_people * 0.2,
                                 roads[mn].base_people[1] + add_people * 0.8]
    #print(roads[3].new,roads[2].base_people, roads[2].new)
    for n in range(0, len(roads)):
        if len(roads[n].new)<1:
            roads[n].new= (roads[n].base_people).copy()

    roads[3].new[0]+=(roads[2].new[0]-roads[2].base_people[0])*0.7
    roads[2].new[1]+=(roads[3].new[1]-roads[3].base_people[1])*0.7











def end(event):
    global movcur
    global mapx
    global mapy
    global  on_move
    global rubber_on
    if mode==3:
        on_move=False
    if mode==0:
        movcur = False
    if mode ==1:
        create_house(event.x-mapx, event.y-mapy)
    if mode==5:
        rubber_on=False
def del_build(id):
    if id<=0:
        return
    for i in range(0, len(r_house)):
        if r_house[i][9]==id:
            for y in range(0, len(pixel_map)):
                for x in range(0, len(pixel_map[y])):
                    if pixel_map[y][x]==id:
                        pixel_map[y][x] = 0
        r_house.pop(i)
        return
def moving(event):
    global apy
    global apx
    global pointx
    global pointy
    global movcur
    global mapx
    global mapy
    global on_move
    global mode
    global r_house
    global index_home_now
    global rubber_on
    if mode==3 and on_move:
        c_cort=r_house[index_home_now][0]
        vect=[event.x-(c_cort[0]+mapx), event.y - (c_cort[1] + mapy)]
        for i in range(0, 5):
            r_house[index_home_now][i][0]+=vect[0]
            r_house[index_home_now][i][1] += vect[1]
    if mode ==0:
        if movcur:
            if -985 <= apx + event.x - pointx <= 0:
                mapx = apx + event.x - pointx
            if -456 <= apy + event.y - pointy <= 0:
                mapy = apy + event.y - pointy

    if mode== 5 and rubber_on:
        del_build(pixel_map[event.y-mapy][event.x - mapx])
root = Tk()
metro_img=[PhotoImage(file='metro2.png'), PhotoImage(file='metro3.png')]
#не ори я все слышу прекрасно
image.save("jelly2.png")
map1 = PhotoImage(file="jelly2.png")

root.geometry("985x390")
root.title("Анализ строительства")
c = Canvas(root, width=985, height=456, background="#AAAAAA")
c.bind("<Motion>", moving)
c.bind("<Button-1>", callback)
root.bind("<Return>", add)
c.bind("<ButtonRelease>", end)
#image_colors = image_colors.ImageColors()
#image_colors.recognize_color(draw_map2)
#вот дааа
c.pack()
# c.config(cursor="hand1")
frame = Frame(root, background='white')
frame.place(rely=0.83, relheight=0.17, relwidth=1)
img = PhotoImage(file='fb12.png')
img2 = PhotoImage(file='fb22.png')
img3 = PhotoImage(file='fb32.png')
img4 = PhotoImage(file='fb42.png')
img5 = PhotoImage(file='fb52.png')
sost = [PhotoImage(file='fb62.png'), PhotoImage(file='fb72.png')]
Button(frame, image=img, background="white", command=start_house).place(relx=0, relwidth=0.1, relheight=1)
Button(frame, image=img2, background="white",  command=start_rotate).place(relx=0.1, relwidth=0.1, relheight=1)
Button(frame, image=img3, background="white",  command=save_hoses).place(relx=0.2, relwidth=0.1, relheight=1)
Button(frame, image=img4, background="white",  command=rabber).place(relx=0.3, relwidth=0.1, relheight=1)
Button(frame, image=img5, background="white",  command=make).place(relx=0.4, relwidth=0.1, relheight=1)
panel = Label(frame, image = sost[0])
panel.place(relx=0.5, relwidth=0.1, relheight=1)
panel.bind("<Button-1>", morn)


while True:
    if mode ==0 and movcur:
        c.config(cursor="hand2")
    elif mode==0 and not(movcur):
        c.config(cursor="arrow")
    elif mode==1:
        c.config(cursor="tcross")
    elif mode==3:
        c.config(cursor="sizing")
    elif mode==5:
        c.config(cursor="dotbox")

    #print(mapx, mapy)
    c.delete("all")
    rotate()
    c.create_image(mapx, mapy, image=map1, anchor=NW)
    if mode==3:
        #print(r_house[index_home_now])
        r_house[index_home_now][8]=check()
    draw_h()
    draw_gui()



    root.update()
    time.sleep(0.010)
#щааа
root.mainloop()
