#!/usr/bin/env python

# ##################################
#	@Author Kaio Cesar
#	@version 0.1 for linux
# ##################################

#import libs
import pygtk
import gtk


#functions
def click_( botao , label):
	if label.get_text() == "" :
		label.set_text( "Clicou no botao" )
	else:
		label.set_text( "" )


# Settings windows
win=gtk.Window()
win.set_title('CronosPy')
win.set_size_request(800,500)
win.connect("destroy", gtk.main_quit)


# Create a box
box=gtk.VBox( )
win.add( box )

# Elements
label=gtk.Label( "" )
box.pack_start( label )

botao=gtk.Button( "Clique aqui" )
box.pack_start( botao )

# Events
botao.connect("clicked" , click_ , label )

# Show \o/
win.show_all()
gtk.main()