# Tuple (ไม่สามารถเปลี่ยนเปลงค่าได้)
d_tuples = (1,2,3,10)
d_list = [1,2,3]
print("List =",d_list)
print("Tuple =",d_tuples)
print("มีข้อมูลค่า 1 จำนวน ",d_tuples.count(1), "ชุด")
new_re = tuple(reversed(d_tuples))
print("new reversed =",new_re)

# add new value to tuple
d_tuples += ("k",)
print(d_tuples)
#สืบทอดคุณสมบัติ
new_tuples_union = (*d_tuples, "T")
print(new_tuples_union,"\n")

f_name = "parew"
new_tuple = tuple(f_name)
print("old string datatype =", f_name)
print("new tuple =",new_tuple)
print("reversed new tuple =",tuple(reversed(new_tuple)))
"""
print(d_tuples[0])
new_list_from_tuples = list(d_tuples)
print("NewList =",new_list_from_tuples)
new_list_from_tuples[0] = "A"
print("change new value =", new_list_from_tuples)
d_tuples = tuple(new_list_from_tuples)
print("NewTuple =",d_tuples)
"""