# seed=7552

# def ran():
#     global seed
#     s=str(seed**2)
#     while len(s)!=8:
#         s="0" +s
#     seed=int(s[4:6])
#     return seed
# l=[]
# for i in range(0,100):
#    # print(ran()," ")
#    l.append(ran())
# dup={x for x in l if l.count(x)>1}
# print(l)
# print("\n")
# print(dup)
# print(len(dup))

seed = 7182

def ran():
    global seed
    s= str(seed**2)
    while(len(s) != 8):
        s="0"+s
    
    seed=int(s[2:6])

    return seed

for i in range(0,15):
    print(ran()," ")