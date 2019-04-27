#coding:utf-8
import glob
import random
from Database import Database
from flask import Flask, render_template, request
app = Flask(__name__)

def getCutWords():
    infoX = []
    with open('data_helper/push_cut.txt') as fr:
        for line in fr:
            newline = line.strip().split('\t')
            infoX.extend(newline[1].split())
    return [x for x in infoX if len(x) >1]


@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/loginX')
def loginX():
    results = []
    keys = random.sample(getCutWords(), 10)
    id_contents_weigth = getIdContentWeight()
    for index, kv in enumerate(id_contents_weigth, 1):
        try:
            results.append([index, str(kv[0]), id_contents[kv[0]][0][:20] + '...', kv[1]])
        except:
            pass
    return render_template('info.html', contents=results, keys=keys)



@app.route('/doLogin', methods=['GET', 'POST'])
def doLogin():
    db = Database()
    id_ = request.form['id']
    passwd = request.form['password2']
    sql_query = "SELECT `user`,`paswd` FROM info WHERE `user`='%s' AND `paswd`='%s'" % (id_, passwd)
    result = db.query(sql_query)
    results = []
    keys = random.sample(getCutWords(), 10)
    if result:
        id_contents_weigth = getIdContentWeight()
        for index, kv in enumerate(id_contents_weigth, 1):
            try:
                results.append([index, str(kv[0]), id_contents[kv[0]][0][:20] + '...', kv[1]])
            except:
                pass
        return render_template('info.html', contents=results, keys=keys)
    else:
        return render_template('login.html', nodata='NO')


@app.route('/doRegister', methods=['GET', 'POST'])
def doRegister():
    db = Database()
    id_ = request.form['id']
    passwd = request.form['password2']
    repasswd = request.form['password3']
    if passwd == repasswd:
        sql_insert = "INSERT INTO info (`user`, `paswd`) VALUES ('%s', '%s')" % (id_, passwd)
        results = db.execute(sql_insert)
        if results:
            return render_template('login.html')
        else:
            return render_template('register.html', nodata='NO')
    else:
        return render_template('register.html', nodata='NO')



def getIdContent():
    id_doc = {}
    filenames = glob.glob('NewsPushDir\\*.txt')
    for filename in filenames:
        tmp = []
        with open(filename, encoding='utf-8') as fr:
            for line in fr:
                tmp.append(line.strip())
        id_doc[filename.strip().split('\\')[-1].split('.')[0]] = tmp
    return id_doc

def getIdContentWeight():
    id_contents_weigth = {}
    with open('./data_helper/id_contents_weighte.csv', encoding='utf-8') as fr:
        for line in fr:
            newline = line.strip().split(',')
            id_contents_weigth[newline[0]] = float(newline[1])
    return sorted(id_contents_weigth.items(), key=lambda k:k[1], reverse=True)

id_contents = getIdContent()

@app.route('/')
def index():#读取推荐的内容 id,content,weigth
    results = []
    id_contents_weigth = getIdContentWeight()
    for index, kv in enumerate(id_contents_weigth, 1):
        try:
            # print([index, str(kv[0]), id_contents[kv[0]][0][:20]+'...', kv[0][1]])
            results.append([index, str(kv[0]), id_contents[kv[0]][0][:20]+'...', kv[1]])
        except:
            pass
    # print(results)
    return render_template('index.html', results=results)

@app.route('/show', methods=['POST', 'GET'])
def show():#获取id对应的原始内容
    key_ = request.args['ids']
    # print(id_contents[key_])
    return render_template('per.html', contents=id_contents[key_])

if __name__ == '__main__':
    app.run(debug=True)

