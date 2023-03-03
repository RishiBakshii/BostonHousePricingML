from django.shortcuts import render
import pickle
import numpy as np

model=pickle.load(open("regmodel.pkl","rb"))
scaler=pickle.load(open("scaling.pkl","rb"))


def home(r):
    return render(r,"home.html")

def predict_api(r):
    if r.method=='POST':
        dataDict=dict(r.POST.items())
        dataKeys=list(dict(r.POST.items()).keys())[1:]
        input_data=[]

        for keys in dataKeys:
            input_data.append(dataDict[keys])

        input_data_array=np.array(input_data).reshape(1,-1)
        scaled_input_data=scaler.transform(input_data_array)
        prediction=model.predict(scaled_input_data)

        context={
            "result":f"The Model Predicted {prediction}",
            "input_data":input_data
        }
        
        return render(r,"home.html",context)
    
