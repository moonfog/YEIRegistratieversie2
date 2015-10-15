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
  grid = SQLFORM.grid(difficulties, fields=fields ,deletable=False,editable=False,details=False,paginate=10,create=False,csv=False,links = [lambda row:A(T('Details'),_href=URL("difficultie","details",args=[row.id]))]user_signature=False)
  return dict(form=grid)
