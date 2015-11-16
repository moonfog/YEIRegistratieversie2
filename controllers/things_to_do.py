﻿@auth.requires_login()
def new():
    form = SQLFORM(db.things_to_do)
    if form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL(r=request,f='overview',args =[session.guestID] ))
    elif form.errors :
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)

@auth.requires_login()
def overview():
    if len(request.args)!= 0:
	       #session.guestID = request.args[0]

	       things_to_do = db.things_to_do.guest == session.guestID
	       fields = [db.things_to_do.guest,db.things_to_do.guidance,db.things_to_do.startdate,db.things_to_do.date_to_aim,db.things_to_do.competence,db.things_to_do.story,db.things_to_do.success]


	       form = SQLFORM.grid(things_to_do,fields=fields,deletable=False,editable=False,details=False,paginate=10,create=False,csv=False,orderby=[~db.things_to_do.startdate],
           links = [lambda row:A(T('Details'),_href=URL("things_to_do","details",args=[row.id]))], user_signature=False)

	       return dict(form=form)

@auth.requires_login()
def details():
   session.things_to_do = (request.args[0])

   record = db(db.things_to_do.id==session.things_to_do).select().first()


   form = SQLFORM(db.things_to_do,record,showid = False,submit_button = T('Update'))
   form.add_button('Back', URL('guest','overview'), _class="btn btn-primary")

   if form.process().accepted:

       response.flash = T('form accepted')
       redirect(URL(r=request,f='overview',args=[record.guest]))

   elif form.errors:
        response.flash = T('form has errors')
   else:
        response.flash = T('Update Axion')

   return dict(form=form)
