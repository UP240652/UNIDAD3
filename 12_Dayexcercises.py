import random as rd
import string as st

#Exercises: Level 1
#1
def random_user_id():
    word = ''
    char = st.ascii_letters + st.digits
    for i in range(6):
        x = rd.randint(0,len(char))
        word += char[x]
    return word
        


def user_id_gen_by_user():
    word = ''
    numChar = int(input("Enter the number of characters: "))
    numUser = int(input("Enter the number of user names: "))
    char = st.ascii_letters + st.digits
    for c in range(numUser):
        for i in range(numChar):
            x = rd.randint(0,len(char))
            word += char[x]
        print(word)
        word = ''


def rgb_color_gen():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    rgb =  [r,g,b]
    return rgb

print(rgb_color_gen())

#Exercises: Level 2
#1
def list_of_hexa_colors(n):
    char = st.ascii_letters[:6] + st.digits
    listHex = []
    hx = '#'
    for i in range(n):
        for x in range(6):
            num = rd.randint(0,len(char)-1)
            hx += char[num]
        listHex.append(hx)
        hx = '#'
    return listHex

#2
def list_of_rgb_colors(n):
    rgbList = []
    for i in range(n):
        r = rd.randint(0,255)
        g = rd.randint(0,255)
        b = rd.randint(0,255)
        rgb = f'rgb({r},{g},{b})'
        rgbList.append(rgb)
    return rgbList

#3
def generate_colors(colorType,n):
    if colorType.upper() == "HEX":
        hx = list_of_hexa_colors(n)
        return hx

    elif colorType.upper() == "RGB":
        rgb = list_of_rgb_colors(n)
        return rgb

    else:
        print(f"Color type no valid")

#Exercises: Level 3
fruits = ["manzana", "plátano", "naranja", "uva", "sandía", "pera", "kiwi", "mango", "fresa", "cereza"]

#1
def shuffle_list(lt):
    rd.shuffle(lt)
    return lt

#2
def unique_nums():
    nums = set()
    while len(nums) <= 7:
        x = rd.randint(0,len(st.digits)-1)
        nums.add(st.digits[x])
    return nums

