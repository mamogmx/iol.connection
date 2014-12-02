from five import grok
from AccessControl import ClassSecurityInfo
from plone.dexterity.content import Container,DexterityContent

from iol.connection import MessageFactory as _

import sqlalchemy as sql

from iol.connection.interfaces import IPGConnection,IPGTable


# Interface class; used to define content-type schema.


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class PGConnection(Container):
    grok.implements(IPGConnection)
    security = ClassSecurityInfo()
    def __init__(self):
        pass
    # Add your class methods and properties here
    def getConnectionString(self):
        return "postgres://%s:%s@%s:%s/%s" %(self.db_user,self.db_pwd,self.db_host,self.db_port,self.db_name)
        
       

class PGTable(DexterityContent):
    grok.implements(IPGTable)
    security = ClassSecurityInfo()
    def __init__(self):
        pass
# View class
# The view will automatically use a similarly named template in
# pg_desktop_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.


#class View(grok.View):
    """ sample view class """

#    pass