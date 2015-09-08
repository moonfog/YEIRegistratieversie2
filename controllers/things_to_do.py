@auth.requires_login()
def new():
    form = SQLFORM(db.things_to_do)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors :
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'

    return dict(form=form)
