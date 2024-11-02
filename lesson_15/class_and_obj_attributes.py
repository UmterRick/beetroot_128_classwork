class MyClass:
    cls_attribute = 1

    def __init__(self):
        print("Create NEW OBJECT")
        self.instance_attribute = -1



my_object = MyClass()

print(my_object.instance_attribute)
print("obj >", my_object.cls_attribute)
print("cls >", MyClass.cls_attribute)

my_object.cls_attribute += 2
print("change class attribute value in OBJECT")
print("obj >", my_object.cls_attribute)

MyClass.cls_attribute = 99
print("change class attribute value in CLASS")


print("cls >", MyClass.cls_attribute)
print("obj >", my_object.cls_attribute)


my_object_2 = MyClass()
print("obj_2 >", my_object_2.cls_attribute)




