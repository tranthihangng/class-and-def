# class-and-def
class human() :
    def __init__(self, para_ten, para_tuoi, para_job):# attribute thuoc tinh
        self.ten = para_ten
        self.tuoi = para_tuoi
        self.job = para_job
    def xin_chao(self):# phuong thuc method nam trong noi bo class
        return 'xin chao, ta chinh la '+ self.ten

human_A = human('Hang', '19', 'student')
print(human_A.xin_chao())
print(human.xin_chao(human_A))
#--------------------------------------------------------
class stock:
    def __init__(self, ce, pe, fl):
        self.tran = ce
        self.tham_chieu = pe
        self.san = fl
    def khuyen_nghi(self):
        if self.tran>30:
            return str(self.tran) +'is a dream price'
        else:
            return str(self.tran)+ 'tam on'
stock_A = stock(5,20,10)
print(stock.khuyen_nghi(stock_A))
print(stock_A.khuyen_nghi())
