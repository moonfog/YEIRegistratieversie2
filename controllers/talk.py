@auth.requires_login()
def new():

   fields = ['guest','date_talk','type_of_talk','story']
   form = SQLFORM(db.talk,fields=fields)

   if form.process().accepted:
        response.flash = 'form accepted'
   elif form.errors :
        response.flash = 'form has errors'
   else:
        response.flash = 'please fill out the form'

   return dict(form=form)

@auth.requires_login()
def overview():
	session.guestID = request.args[0]

	talks = db.talk.guest == session.guestID
	fields = [db.talk.date_talk, db.talk.type_of_talk]

	form = SQLFORM.grid(talks,fields=fields,deletable=False,editable=False,details=False,paginate=10,create=False,csv=False,orderby=[~db.talk.date_talk],
        links = [lambda row:A(T('Details'),_href=URL("talk","details",args=[row.id]))], user_signature=False)

	return dict(form=form)

@auth.requires_login()
def details():
   session.talkID = request.args[0]

   record = db(db.talk.id==session.talkID).select().first()
        #fields = ['name' , 'sex', 'birth_year','nationality','origin','education']
   form = SQLFORM(db.talk,record,showid = False,submit_button = T('Update'))

   if form.process().accepted:
       #session.guestID=form.vars.guest.id
       response.flash = T('form accepted')
       redirect(URL(r=request,f='overview'))

   elif form.errors:
        response.flash = T('form has errors')
   else:
        response.flash = T('Update Talk')

   return dict(form=form)
