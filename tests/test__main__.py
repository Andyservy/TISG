class MainClass1:

    def func_main1(self):
        print('This Welcome Message is from Main Class 1')


class MainClass2:

    def func_main2(self):
        print('This is an another Message coming from Main Class 2')


class ChildClass(MainClass1, MainClass2):

    def func_child(self):
        print('This is coming from Child Class')


chd = ChildClass()

chd.func_main1()
chd.func_main2()
chd.func_child()