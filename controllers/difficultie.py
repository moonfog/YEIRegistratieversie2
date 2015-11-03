@auth.requires_login()
def new():
    form = SQLFORM(db.difficultie)
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

  difficulties =((db.difficultie.registrator == auth.user.id) & (db.difficultie.guest == session.guestID))
  fields = [db.difficultie.guest,db.difficultie.subject]
  form = SQLFORM.grid(difficulties, fields=fields ,deletable=False,editable=False,details=False,paginate=10,create=False,csv=False,links = [lambda row:A(T('Details'),_href=URL("difficultie","details",args=[row.id]))],user_signature=False)
  form[0].append(TAG.INPUT(_value=T('Add Difficultie'),_type="button",_onclick="window.location='%s';"%URL(r=request,f='new',vars=request.vars)))
  return dict(form=form)

@auth.requires_login()
def details():
      session.difficultieID = request.args[0]

      record = db(db.difficultie.id==session.difficultieID).select().first()

      form = SQLFORM(db.difficultie,record,showid = False, submit_button = T('Update'))

      if form.process().accepted:

          response.flash = T('form accepted')
          redirect(URL(r=request,f='overview',args=[record.guest]))

      elif form.errors:
           response.flash = T('form has errors')
      else:
           response.flash = T('Update Talk')

      return dict(form=form)
