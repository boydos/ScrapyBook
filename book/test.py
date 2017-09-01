
class Person :
    king = " "
    kings = "ddfa "
    def __init__(self):
        pass
    def say(self,strs):
        print "hello ",strs
    def tong(self,name,word):
        print self.king
        if not self.king.strip() or not self.kings.strip():
            print "king is null" ;
            return;
        print "My Name is ",name
        self.say(word)

p = Person()
p.tong("kkk","okk")
