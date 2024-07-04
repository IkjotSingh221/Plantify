<<<<<<< HEAD
from pymongo import MongoClient
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.staticfiles import StaticFiles
import numpy as np
from fastapi import FastAPI, UploadFile, File, Form, Request
import uvicorn
import cv2
import tensorflow as tf
import hashlib
import csv
import re
from starlette.templating import Jinja2Templates

client=MongoClient("mongodb+srv://<Your_username>:<Your_password>@cluster0.27fgh31.mongodb.net/")
templates = Jinja2Templates(directory="HTML")

app = FastAPI()
app.mount("/css", StaticFiles(directory=r"C:\Users\ikjot\OneDrive\Documents\Coding\plantify\CSS"), name="css")
app.mount("/assets", StaticFiles(directory=r"C:\Users\ikjot\OneDrive\Documents\Coding\plantify\Assets"), name="assets")
app.mount("/js", StaticFiles(directory=r"C:\Users\ikjot\OneDrive\Documents\Coding\plantify\JS"), name="js")

model = tf.keras.models.load_model(r'C:\Users\ikjot\OneDrive\Documents\Coding\plantify\models\Final_Plantify.keras')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
async def newUser(request: Request, uname: str = Form(...) , email_id: str = Form(...), pswd: str = Form(...)):
    mydb = client["Plantify"]
    mycol = mydb["Userdata"]
    # if(pswd!=pswd2):
    #     data = [1, 2, 3, 4, 5]
    #     msg = "The re-entered password does not match"
    #     return templates.TemplateResponse("signup.html",{"request" : request, "error" : msg, "data" : data})
    if(mycol.count_documents({"username":uname})>0):
        msg = "This username is already taken"
        return templates.TemplateResponse("signup.html",{"request" : request, "error" : msg})
    else:
        rec = {"username": uname, "email" : email_id , "password" : pswd}
        x=mycol.insert_one(rec)
        msg = "Record inserted successfully"
        return templates.TemplateResponse("upload.html",{"request" : request, "response": "Logged in!"})

@app.post("/login")
async def oldUser(request: Request, email_id_login: str = Form(...) , pswd_login: str = Form(...)):
    mydb = client["Plantify"]
    mycol = mydb["Userdata"]
    if(mycol.count_documents({"email":email_id_login})==0):
        msg = "This username does not exist"
        return templates.TemplateResponse("login.html",{"request" : request, "error" : msg})
    else:
        rec = mycol.find({"email ":email_id_login})
        if (pswd_login != rec[0]["password"]):
            msg = "Incorrect password!"
            return templates.TemplateResponse("login.html",{"request" : request, "error" : msg})
        else:
            msg = "Successfully Logged in"
            return templates.TemplateResponse("upload.html",{"request" : request, "response": msg})

@app.post("/images/")
async def create_upload_file(request: Request,file: UploadFile = File(...)):
    """POST request with file=path of the file"""
    try:
        contents = await file.read()
        nparr = np.fromstring(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        preprocessed_image = cv2.resize(image, (150, 150))
        preprocessed_image = preprocessed_image.astype("float32") / 255.0
        preprocessed_image = np.expand_dims(preprocessed_image, axis=0)

        predictions = model.predict(preprocessed_image)
        predicted_class = np.argmax(predictions)
        class_labels=["Daisy","Dandelion","Rose","Sunflower","Tulip"]
        flower=class_labels[predicted_class]
        return templates.TemplateResponse("upload.html", {"request": request,"flower":flower})
    except Exception as e:

        return {"Please upload a file!"}

@app.get("/images")
async def root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=5000, reload=True)

=======
from pymongo import MongoClient
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.staticfiles import StaticFiles
import numpy as np
from fastapi import FastAPI, UploadFile, File, Form, Request
import uvicorn
import cv2
import tensorflow as tf
import hashlib
import csv
import re
from starlette.templating import Jinja2Templates

client=MongoClient("mongodb+srv://<Your_username>:<Your_password>@cluster0.27fgh31.mongodb.net/")
templates = Jinja2Templates(directory="HTML")

app = FastAPI()
app.mount("/css", StaticFiles(directory=r"C:\Users\ikjot\OneDrive\Documents\Coding\plantify\CSS"), name="css")
app.mount("/assets", StaticFiles(directory=r"C:\Users\ikjot\OneDrive\Documents\Coding\plantify\Assets"), name="assets")
app.mount("/js", StaticFiles(directory=r"C:\Users\ikjot\OneDrive\Documents\Coding\plantify\JS"), name="js")

model = tf.keras.models.load_model(r'C:\Users\ikjot\OneDrive\Documents\Coding\plantify\models\Final_Plantify.keras')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
async def newUser(request: Request, uname: str = Form(...) , email_id: str = Form(...), pswd: str = Form(...)):
    mydb = client["Plantify"]
    mycol = mydb["Userdata"]
    # if(pswd!=pswd2):
    #     data = [1, 2, 3, 4, 5]
    #     msg = "The re-entered password does not match"
    #     return templates.TemplateResponse("signup.html",{"request" : request, "error" : msg, "data" : data})
    if(mycol.count_documents({"username":uname})>0):
        msg = "This username is already taken"
        return templates.TemplateResponse("signup.html",{"request" : request, "error" : msg})
    else:
        rec = {"username": uname, "email" : email_id , "password" : pswd}
        x=mycol.insert_one(rec)
        msg = "Record inserted successfully"
        return templates.TemplateResponse("upload.html",{"request" : request, "response": "Logged in!"})

@app.post("/login")
async def oldUser(request: Request, email_id_login: str = Form(...) , pswd_login: str = Form(...)):
    mydb = client["Plantify"]
    mycol = mydb["Userdata"]
    if(mycol.count_documents({"email":email_id_login})==0):
        msg = "This username does not exist"
        return templates.TemplateResponse("login.html",{"request" : request, "error" : msg})
    else:
        rec = mycol.find({"email ":email_id_login})
        if (pswd_login != rec[0]["password"]):
            msg = "Incorrect password!"
            return templates.TemplateResponse("login.html",{"request" : request, "error" : msg})
        else:
            msg = "Successfully Logged in"
            return templates.TemplateResponse("upload.html",{"request" : request, "response": msg})

@app.post("/images/")
async def create_upload_file(request: Request,file: UploadFile = File(...)):
    """POST request with file=path of the file"""
    try:
        contents = await file.read()
        nparr = np.fromstring(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        preprocessed_image = cv2.resize(image, (150, 150))
        preprocessed_image = preprocessed_image.astype("float32") / 255.0
        preprocessed_image = np.expand_dims(preprocessed_image, axis=0)

        predictions = model.predict(preprocessed_image)
        predicted_class = np.argmax(predictions)
        class_labels=["Daisy","Dandelion","Rose","Sunflower","Tulip"]
        flower=class_labels[predicted_class]
        return templates.TemplateResponse("upload.html", {"request": request,"flower":flower})
    except Exception as e:

        return {"Please upload a file!"}

@app.get("/images")
async def root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=5000, reload=True)

>>>>>>> 381c6abcc1795e6cb7c919b789296410e5bbad5b
