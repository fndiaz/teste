# coding=UTF-8

def principal():
	response.title = 'Padrão'
	teste = "página principal"
	
	return response.render("initial/principal.html", teste=teste)

def addarticle():
	form = SQLFORM(Article).process()
	return response.render("initial/addarticle.html", form=form)
 
def showarticle():
	id = request.args(0) or redirect(URL('default', 'index'))
	article = Article[id] 
	print article
	return response.render("initial/showarticle.html", article=article)


def log():
	response.title = 'Padrão'
	teste = "página secundaria"
	
	return response.render("initial/principal.html", teste=teste)


def user():
	#if request.args(0) == 'register':
    #    	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	return response.render("initial/user.html", user=auth())

def register():
	return auth.register()

def login():
        return auth.login()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)



	



