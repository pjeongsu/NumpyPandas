import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sklearn.externals
import joblib
import pandas as pd 
import numpy as np 
import mglearn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model', methods = ['GET','POST'])
def model():    
    if request.method == 'GET':
        return render_template('model/model.html')

    else:
        gender = request.form.get('gender') 
        major = request.form.get('major')
        edu_lev = request.form.get('edu_lev')
        en_uni  = request.form.get('en_uni')
        re_exp = request.form.get('re_exp')
        last = request.form.get('last')
        comp_type = request.form.get('comp_type')
        comp_size = request.form.get('comp_size')
        training = request.form.get('training')
        exp = request.form.get('exp')
        city = request.form.get('city')
        

        df = pd.DataFrame({'city_development_index':[city],'gender':[gender],'relevent_experience':[re_exp],
                            'enrolled_university':[en_uni],'education_level':[edu_lev],'major_discipline':[major],
                            'experience':[exp], 'company_size':[comp_size],'company_type':[comp_type],
                            'last_new_job':[last],'training_hours':[training]  } )

        df = df.astype({'city_development_index': 'float','experience':'int',
                        'training_hours':'int','last_new_job':'int'})
         
        pred  = model.predict_proba(df)
        pred  = (pred[0][1]*100).round(2)

        print(pred)
        print(type(pred))


        # if not(gender and major and edu_lev and re_exp and last and comp_type and comp_size and exp):
        #     return render_template('model.html')

        # turnover = Turn()
        # turnover.gender = gender
        # turnover.major = major
        # turnover.edu_lev = edu_lev
        # turnover.re_exp = re_exp
        # turnover.last = last
        # turnover.comp_type = comp_type
        # turnover.comp_size = comp_size
        # turnover.exp = exp
        
        # db.session.add(turnover)
        # db.session.commit()


        return render_template('/model/model.html',df=df, gender=gender ,major=major, 
                                edu_lev=edu_lev,en_uni=en_uni, re_exp=re_exp, last=last, comp_type=comp_type,
                                comp_size=comp_size,training=training,exp=exp, city=city, pred=pred)
    

if __name__ == '__main__':

    model = joblib.load('Web/model_soft.pkl')

    # basedir = os.path.abspath(os.path.dirname(__file__))
    # dbfile = os.path.join(basedir,'db.sqlite')

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    # app.config['SQLALCHEMY_COMMIT_ON_TEADDOWN'] = True # 사용자 요청의 끝에서 커밋을 한다는 의미 데이터 베이스에 저장을 하겠다.
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.init_app(app)
    # db.app = app 

    # # db 생성
    # db.create_all()
    app.run(host='127.0.0.1', port=5000,debug=True)    
