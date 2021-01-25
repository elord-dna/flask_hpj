from flask import Flask,request,session,render_template,redirect,url_for
from pokemon import Pokedex
import SQLcontrol
app = Flask(__name__)
# session.keys = '123hioydsaiydoiashyd1'
app.config['SECRET_KEY'] = '123hioydsaiydoiashyd1'
adict = {'111':'222','333':'444'}
alist = []
bdict = {'111':'18','333':'28'}

def _randomPokedex(n):
    if n > 9: n = 9
    d = {}
    e = {}
    for i in range(n):
        uid = '00' + str(i+1)
        p = Pokedex(uid)
        p.suiji()
        d[uid] = p
        e[p.pokename] = p
    return d,e

def _allPokedex(_dict: dict):
    shuzu = []
    for k,v in _dict.items():
        shuzu.append(v)
    return shuzu

pokeDict, pokeDictName = _randomPokedex(9)
plpl = _allPokedex(pokeDict)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
# app.debug = True

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in adict.keys():
            if password == adict[username]:
                session['username'] = username
                alist.append(username)
                # return render_template('index.html')
                return redirect(url_for('index'))
            else:
                return render_template('login.html',msg = '密码错误')
        else:
             return render_template('login.html',msg = '没有用户名')
    else:
        return render_template('login.html')

@app.route('/index')
def index():
    # pi = session.get('username')
    # if pi in alist:
    #     return render_template('index.html',users = bdict)
    # else:
    #     return redirect(url_for('login'))
    kpl = SQLcontrol.findall()
    return render_template('index.html',users = kpl)

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))

@app.route('/index/<uid>')
def index2(uid):
    if is_number(uid):
        spl = SQLcontrol.findById(uid)
        return render_template('nindex.html',plplpl = spl)
    else:
        return render_template('nindex.html',plplpl = pokeDictName[uid])
        
        

if __name__ == "__main__":

    app.run()