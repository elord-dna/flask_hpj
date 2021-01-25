import random
class Pokedex():
    ytype = ['一般','火','水','草','电','冰','虫','飞行','地面','岩石','格斗','超能力','幽灵','毒','恶','钢','龙','妖精']
    chara = ['恶臭','降雨','加速','战斗盔甲']
    def __init__(self,id):
        self.uid = id
        self.pokename = ''
        self.shape = ''
        self.type1 = ''
        self.type2 = ''
        self.characteristic1 = ''
        self.characteristic2 = ''
        self.hidden = ''
        self.hp = 1
        self.attack = 0
        self.difense = 0
        self.sattack = 0
        self.sdifense = 0
        self.speed = 0
        self.ti = 1

    def suiji(self):
        astr = '撒谎低于奥斯但是打开懒得哈师大和工程部被可'
        self.pokename = ''.join(random.sample(astr, random.randint(2,5)))
        self.type1 = self.ytype[random.randint(0,17)]
        self.type2 = self.ytype[random.randint(0,17)]
        self.characteristic1 = self.chara[random.randint(0,3)]
        self.characteristic2 = self.chara[random.randint(0,3)]
        self.hidden = self.chara[random.randint(0,3)]
        self.hp = random.randint(1,255)
        self.attack = random.randint(1,255)
        self.sattack = random.randint(1,255)
        self.difense = random.randint(1,255)
        self.sdifense = random.randint(1,255)
        self.speed = random.randint(1,255)
        self.ti = self.hp + self.attack + self.sattack + self.difense + self.sdifense + self.speed
        # return self

    def __str__(self):
        return "id:%s,name:%s,type1:%s,,type2:%s,characteristic1:%s,characteristic2:%s,hidden:%s,hp:%d,attack:%d,sattack:%d,difense:%d,sdifense:%d,speed:%d,ti:%d"%(self.uid,self.pokename,self.type1,
            self.type2,self.characteristic1,self.characteristic2,self.hidden,self.hp,self.attack,self.sattack,self.difense,self.sdifense,self.speed,self.ti
        )

    
# po = Pokedex('001')
# po.suiji()
# print(po)