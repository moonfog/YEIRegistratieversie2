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
  fields = [db.difficultie.guest,db.difficultie.subject,db.difficultie.story]
  grid = SQLFORM.grid(difficulties, fields=fields ,user_signature=False )
  return dict(form=grid)
