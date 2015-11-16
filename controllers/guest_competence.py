@auth.requires_login()
def new():
	session.guestID = request.vars.guestID
	competences = db.guest_competence.guest == session.guestID
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
	if len(request.args)!=0:
		session.guestID = request.args[0]

	competences = db.guest_competence.guest == session.guestID
	fields = [db.guest_competence.competence]

	form = SQLFORM.grid(competences,fields=fields,searchable=False,deletable=False,editable=False,details=False,paginate=10,create=False,csv=False,
		links = [lambda row:A(T('Details'),_href=URL("guest_competence","details",args=[row.id]))], user_signature=False)
	form[1].append(TAG.INPUT(_value=T('Add Competence'),_type="button",_class="btn btn-primary",_onclick="window.location='%s';"%URL(r=request,f='new',vars=request.vars)))
	form[1].append(TAG.INPUT(_value=T('Back'),_type="button",_class="btn btn-primary",_onclick="window.location='%s';"%URL('guest', 'overview')))
	return dict(form=form)

@auth.requires_login()
def details():
   session.competenceID = request.args[0]

   record = db(db.guest_competence.id==session.competenceID).select().first()

   form = SQLFORM(db.guest_competence,record,showid = False,submit_button = T('Update'))

   if form.process().accepted:
		response.flash = T('form accepted')
		redirect(URL(r=request,f='overview',args=[record.guest]))

   elif form.errors:
		response.flash = T('form has errors')
   else:
		response.flash = T('Update Guest Competence')

   return dict(form=form)
