@auth.requires_login()
def new():
    session.guestID = request.vars.guestID
    form = SQLFORM(db.guest_competence)
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

	competences = db.guest_competence.guest == session.guestID
	fields = [db.guest_competence.competence]

	form = SQLFORM.grid(competences,fields=fields,deletable=False,editable=False,details=False,paginate=10,create=False,csv=False,
        links = [lambda row:A(T('Details'),_href=URL("guest_competence","details",args=[row.id]))], user_signature=False)
	form[0].append(TAG.INPUT(_value=T('Add Competence'),_type="button",_onclick="window.location='%s';"%URL(r=request,f='new',vars=request.vars)))

	return dict(form=form)

@auth.requires_login()
def details():
   session.competenceID = request.args[0]

   record = db(db.guest_competence.id==session.competenceID).select().first()

   form = SQLFORM(db.guest_competence,record,showid = False,submit_button = T('Update'))

   if form.process().accepted:
        response.flash = T('form accepted')
        redirect(URL(r=request,f='overview'))

   elif form.errors:
        response.flash = T('form has errors')
   else:
        response.flash = T('Update Guest Competence')

   return dict(form=form)
