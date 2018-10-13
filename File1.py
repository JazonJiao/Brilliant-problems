def find():
    f = open("D:/2018/CS2201/Brilliant/180723.txt", "r")
    s = f.read()
    s = s.replace("\n", ",")
    f2 = open("D:/2018/CS2201/Brilliant/180724.txt", "w")
    f2.write(s)
    #return s


print(find())
