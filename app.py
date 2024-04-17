from json import dump
import os
from flask import Flask, Request, render_template, request
import mysql.connector
from werkzeug.utils import secure_filename
# from cesar import cesar
# from werkzeug.datastructures import MultiDict
# from flask_mysql_connector import MySQL
# from flaskext.mysql import MySQL
import stagano
# print(mydb)
UPLOAD_FOLDER = '/static/upload/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','webp'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def welcome():
    return render_template("index.html")
@app.route('/stegano',methods=['GET', 'POST'])
def stegano():
    # return "HEY"
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            return 'No file part'
        file = request.files['image']
        file.save(file.filename)
        
        if(request.form["action"]=="encrypt"):
            
            img=stagano.hide(request.form['message'],file.filename)
            return img
            return "<a href='{{ url_for(\'static\', filename=\'"+img+"\') }}' download class='p-4 bg-blue-500'>Telecharger l'image</a>"
        if(request.form["action"]=="decrypt"):
            return stagano.discover(file.filename)
    
    return "POST REQUEST NEEDED"



# @app.route("/message")
# def messagerie():
#     return render_template("message.html")
# @app.route("/hi/<string:name>")
# def hi(name:str):
#     return render_template("hi.html",name=name)

# # Insert
# @app.route("/insert/<table>",methods=['GET', 'POST'])
# def insert(table:str):
#     if(request.method=="GET"):
#         l=request.args
#     else:
#         l=request.form
#     values=""
#     c=1

#     # #     # cesar("SAL",5)
#     #     cesar(l.get("message"),l[0]["id_destination"])
#     for v in  list(l.values()):
#         if(table=="message"):
#             v=cesar(v,int(l.get("destinateur")))
#         values+=f"'{v}'"
#         if(len(list(l.values()))>c):
            
#             values+="," 
#         c+=1
    
#     keys=""
#     c=1
#     for k in  list(l.keys()):
#         keys+=k
#         if(len(list(l.keys()))>c):
#             keys+="," 
#         c+=1
    
#     sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
#     mycursor.execute(sql)
#     mydb.commit()
#     return f"{table} added!"

# # Update
# @app.route("/update/<table>/<id>",methods=['GET', 'POST'])
# def update(table:str,id:int):
#     if(request.method=="GET"):
#         l=request.args
#     else:
#         l=request.form
#     keys=""
#     c=1
#     for k in  list(l.keys()):
#         keys+=k+"='"+list(l.values())[c-1]+"'"
#         if(len(list(l.keys()))>c):
#             keys+="," 
#         c+=1
#     sql = f"UPDATE {table} set {keys} WHERE id={id}"
#     mycursor.execute(sql)
#     mydb.commit()
#     return "Student updated!"

# @app.route("/select/<string:table>/<int:id>")
# def select(table:str,id:int):
#     arg=""
#     if(id!=0):
#         arg=f"WHERE id={id}"
#     sql = f"SELECT * FROM {table} {arg}"
#     mycursor.execute(sql)
#     data=mycursor.fetchall()
#     # if(table=="message" and id!=0):
#     #     d=tuple()
#     #     for i in data:
#     #         d=d+(i[0],cesar(i[1],id,"decrypt"))
        
        
#     return data

# @app.route("/delete/<string:table>/<int:id>")
# def delete(table:str,id:int):    
#     sql = f"DELETE FROM {table} where id={id}"
#     mycursor.execute(sql)
#     mydb.commit()
#     return f"Student {id} deleted"



if __name__ == '__main__':
    app.run(debug=True)