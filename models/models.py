#gravacao_lg = db.define_table("gravacao_lg",
#      Field("datetime"),
#      Field("acao"),
#      Field("pastas"),
#      #auth.signature
#      format="%(nome)s")

uploadfolder='/home/fernando/web2py/applications/teste/static/images/article'

Article = db.define_table('article',
    Field("title"),
    Field("article_text", "text"),
    Field("picture", "upload", uploadfolder=uploadfolder,),
    Field("thumbnail", "upload", uploadfolder=uploadfolder,)
)

from smarthumb import SMARTHUMB

box = (200, 200)
Article.thumbnail.compute = lambda row: SMARTHUMB(row.picture, box)


