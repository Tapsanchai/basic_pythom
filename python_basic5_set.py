# Set ค่าซ้ำกันไม่ได้ / ลำดับไม่แน่นอน
d_set = {'a','b','y','z'}
print(d_set," -> ",type(d_set))

# add value to Set
d_set.add('A')
d_set.add('Z')
print(d_set)
# multiple add value to Set
d_set.update(['a01','b02'])
print(d_set)
print("จำนวนสมาชิก =",len(d_set),"\n")

for v in d_set:
    print(v,end="")
print("")
print("มีข้อมูลที่ค้นหา") if 'a01' in d_set else print("ไม่มีข้อมูลที่ค้นหา")

# remove value from set  
# use remove() or discard() 

# d_set.remove('A') //delete value | if
d_set.discard('A') # delete when see value
print("remove A =",d_set,"\n")

# set update / union value
fruitA = {'A', 'B', 'C'}
fruitB = { 'X', 'Y', 'Z'}
print("F_A: ", fruitA)
print("F_B: ", fruitB)
new_group = fruitA.union(fruitB)
print("new_group: ", new_group)
fruitA.update(fruitB)
print("fruitA update: ", fruitA, "\n")

# copy Set
fruitC =fruitA.copy()
print("f_C Copy F_A: ", fruitC)

# set different
fruitD = {'A','C','H'}
print("F_D: ", fruitD)
fruitD.difference_update(fruitC)
print("f_D Difference F_C: ", fruitD, "\n")

# set intersection
fruitE = {'p','g','j'}
fruitF = {'j','p','k'}
print("f_E", fruitE)
print("f_F", fruitF)
fruitE.intersection_update(fruitF)
print("f_E intersection F_F: ", fruitE, "\n")

# set find subset
fruitG = {'j'}
print("f_G", fruitG)
print("f_G issubset f_F ? =", fruitG.issubset(fruitF)) #มีลูกในพ่อมั้ย
print("f_F issuperset f_G ? =", fruitF.issuperset(fruitG), "\n") #มีพ่อในลูกมั้ย

# Frozen Set 
fruitH = frozenset(['n','o','m'])
print("Frozen H: ",fruitH)
print("Frozen H is type: ",type(fruitH))
# fruitH.add('w')
show_value_H = [print("index:", k,"value:", v) for k,v in enumerate(fruitH)]
