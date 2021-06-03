# Dictionary | key -> value (Object Datatype)
d_dic = {'id': 1, 'name': 'parew', 'grade': 3.5}
print("d_dic = ", d_dic, "->", type(d_dic))
print("name = ", d_dic['name'], "\n")

# add / update (ถ้ามีอยู่แล้วให้แก้ไข ไม่มีให้เพิ่มใหม่เข้าไป)
new_value = {'school': 'KCC', 'city': 'yasothon'}
d_dic.update({'room': '305'})
d_dic.update(new_value)
print("update d_dic = ", d_dic, "\n")

# remove key,value of dict
d_dic.pop('school')
d_dic.popitem()  #ลบตัวหลังสุดออก
print("delete d_dic = ", d_dic, "\n")

# clear dict
d_dic.clear()
print("clear d_dic = ", d_dic)
if d_dic == {}:
    del d_dic
    print("delete d_dic successfully..")
else:
    print("delete d_dic error!!")
print("\n")

# next step dict | JSON style
Restaurant = {
    'ร้าน A': {
        'name': 'A',
        'menu': 'test1'
    },
    'ร้าน B': {
        'name': 'B',
        'menu': 'test2'
    }
}

print("Restaurant: ",Restaurant , "->", type(Restaurant))
"""
print(Restaurant['ร้าน A'])
print(Restaurant['ร้าน B'])
"""

# Format 1
for value in Restaurant:
    print("ชื่อร้าน: ", value)
    print("--ชื่อคนขาย: ", Restaurant[value]['name'])
    print("--ชื่ออาหาร: ", Restaurant[value]['menu'])
print("")

# Format 2
for key, value in Restaurant.items():
    print("ชื่อร้าน: ", key)
    print("--ชื่อคนขาย: " ,value['name'])
    print("--ชื่ออาหาร: ", value['menu'])
print("")
find_menu = "test2"
print("ร้าน A มีเมนูชื่อ:",find_menu, "=>",find_menu in Restaurant['ร้าน A']['menu']) if find_menu in Restaurant['ร้าน A']['menu'] else print("ร้าน A ไม่มีเมนูชื่อ:",find_menu, "=>",find_menu in Restaurant['ร้าน A']['menu'])

new_R_id ="ร้าน C"
new_R = {'ร้าน C': {
    'name': 'C',
    'menu': 'test3'
}}
print("New Data Dict =",new_R)
Restaurant.update(new_R)
# Restaurant[new_R_id] = {
#     'name': 'C',
#     'menu': 'test3'
# }
print("New Restaurant: ",Restaurant)