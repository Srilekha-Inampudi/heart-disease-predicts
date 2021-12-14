from flask import Flask,request,render_template
import pickle




file3 = open('heart.pkl','rb')
lr3 = pickle.load(file3)
file3.close()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')





"""<!-- age	bp	sg	al	su	bgr	bu	sc	hemo	pcv	htn	appet	pe	ane	 -->

    <!-- age - age
bp - blood pressure
sg - specific gravity
al - albumin
su - sugar
bgr - blood glucose random
bu - blood urea
sc - serum creatinine
hemo - hemoglobin
pcv - packed cell volume
htn - hypertension
appet - appetite
pe - pedal edema
ane - anemia
-->

"""





@app.route('/heart',methods = ['GET','POST'])
def heart():
    #if request == 'POST'
    if request.method == 'POST':
        my_dict2 = request.form
        age1 = float(my_dict2['age1'])
        htn1 = float(my_dict2['htn1'])
        sg1 = float(my_dict2['sg1'])
        sg2 = float(my_dict2['sg2'])
        al1 = float(my_dict2['al1'])
        su1= float(my_dict2['su1'])
        bgrk1 = float(my_dict2['bgrk1'])
        bu1= float(my_dict2['bu1'])
        sc1= float(my_dict2['sc1'])
        hemo1= float(my_dict2['hemo1'])
        pcv1= float(my_dict2['pcv1'])
        pcv2= float(my_dict2['pcv2'])
        pcv3= float(my_dict2['pcv3'])
        input_features2 = [age1,htn1,sg1,sg2,al1,su1,bgrk1,bu1,sc1,hemo1,pcv1,pcv2,pcv3]
        inf = lr3.predict([input_features2])
        if inf == 1:
            inf = 'YES'
        elif inf == 0:
            inf = 'NO'
        return render_template('heartshow.html',inf = inf)
    
    return render_template('heart.html')


@app.route('/aboutheart')
def aboutheart():
    return render_template('aboutheart.html')



if __name__ == "__main__":
    app.run(debug = True)
