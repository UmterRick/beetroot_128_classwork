class MyContextManagerObject:

    def __enter__(self):
        print("I am enter method!")
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("I am exit method!")


print("START OF CODE")

with MyContextManagerObject() as my_object:
    print("I am inside with-as")

print("END OF CODE")
