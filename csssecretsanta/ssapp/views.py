#provides backends for each url
from flask import request, redirect, render_template, url_for, \
    stream_with_context, \
    flash, send_from_directory

from ssapp.models import *
from ssapp import app, db, mail
from flask import request,session,abort
import random
import urllib
import random
from flask_mail import Message

#logs out current user
@app.route('/logout', methods=['GET','POST'])
def logout():
    session['logged_in']=False
    session['currentuser']=-1
    return redirect('/')

#prompts visitor to login
@app.route('/login',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
         try:
             #get the pool specified
             pool=Pool.query.filter_by(name=request.form['pool']).first()
             #get the users matching the username and password
             users=User.query.filter_by(username=request.form['username']).filter_by(password=request.form['password']).all()
             #check if any of those users are in the pool's userinfo
             user=None
             pool_users=pool.userinfo.split(' ')
             for u in users:
                  if(str(u.id) in pool_users):
                        user=u
             if(user):
                 #login the user and send to /poolinfo page
                 if(str(user.id) in pool.userinfo.split(' ')):
                      session['currentuser']=user.id
                      session['logged_in']=True
                      return redirect("/poolinfo/"+str(pool.id))
                 #even though error, I chose to use bg-success color(green) because it contrasts with the website background color(red)
                 flash("User not in Group",'bg-success') 
             else:
                 flash("User not Found",'bg-success')
             return redirect('/login')
         except:
             flash("Login Error",'bg-success')
             return redirect('/login')
         return redirect("/login")
    return render_template('login.html')


        
#once logged in, users cann see their target and can enter in a wishlist in the pool page 
@app.route('/poolinfo/<int:poolid>',methods=['GET','POST'])
def poolinfo(poolid):
    #get user and pool objects
    pool=Pool.query.get(poolid)
    currentuser=User.query.get(session['currentuser'])
    

    #if users submits a wishlist
    if request.method=='POST':
        try:
            currentuser.wishlist=request.form['wishlist']
            db.session.add(currentuser)
            db.session.commit()
            flash('Added Wishlist','bg-success')
            return redirect('/poolinfo/'+str(poolid))
        except:
            flash("Error Adding Wishlist",'bg-success')
            return redirect('/poolinfo/'+str(poolid))

    #get the user's target
    userlist=pool.userinfo.split(' ')
    target=userlist.index(str(currentuser.id))+1
    if(target>=len(userlist)):
        target=userlist[0]
    else:
        target=userlist[target]
    target=User.query.get(int(target))
    noWishList=currentuser.wishlist is None
    return render_template('poolinfo.html',pool=pool,user=currentuser,noWishList=noWishList,target=target)

@app.route('/createpool',methods=['GET','POST'])
def createpool():
    if request.method=='POST':
        try:
            #check that the pool name is unique
            samepools=Pool.query.filter_by(name=request.form['name']).all()
            if(len(samepools)>0):
                 flash("Group name already exists",'bg-success')
                 return redirect('/')
 
            #create users
            allusers=request.form['userinfo']
            allusers=allusers.split('\n')
            userstr=[]
            for u in allusers:
                if(len(u)==0):
                   continue
                temp=u.split(',')
                if(len(temp)!=3):
                   continue
                user=User(temp[0].strip(),temp[1].strip(),temp[2].strip())
                db.session.add(user)
                db.session.commit()
                userstr.append(str(user.id))


            #shuffle the order of users so random secret santas
            random.shuffle(userstr)



            #send users emails
            for idx,u in enumerate(userstr):
                user=User.query.get(int(u))
                target=idx+1
                if(idx+1>=len(userstr)):
                    target=0
                target=int(userstr[target])
                target=User.query.get(target)
                a=str(user.email).strip()
                try:
                    msg=Message('Secret Santa Group Invitation',sender='secsanta9@gmail.com',recipients=[a])
                    msg.body="Welcome to Secret Santa Group: {}\nYour target is {}.\nLogin to add a wishlist.".format(request.form['name'],target.username)
                    mail.send(msg)
                except:
                    flash('email error','bg-success')



            #create the pool
            userstr=' '.join(userstr).strip()
            newpool=Pool(request.form['name'].strip(),request.form['description'].strip(),userstr)
            flash("Group Created",'bg-success')
            flash("Emails sent out",'bg-success')
            db.session.add(newpool)
            db.session.commit()
            return redirect('/login')
        except:
            flash("Error","bg-success")
            return redirect('/login')
    else:
       return render_template('newpool.html')


