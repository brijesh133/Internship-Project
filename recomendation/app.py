from flask import Flask, redirect, url_for, render_template, request, session,flash   #

app = Flask(__name__)               #
 
#@app.route("/")
#def home():

#	return render_template("search1.html")


@app.route("/", methods=["POST","GET"])     #
def search1():     #
	dataextract=''  #
    transno=''      #
    if request.method == 'POST':  #
        transno = int(request.form['transno'])   #
        dataextract=dfcopy.loc[transno]       #
        if testing_prediction_all[transno] == 0:   #
            predicted_result = 1                   #
        else:                         #
            predicted_result = 0
    return render_template("search1.html",transno=transno, dataextract=dataextract,pred=predicted_result,actual=actual_result)  #





if __name__ == "__main__":  #
	app.run()                #