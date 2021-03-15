# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HELLO WX", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Fom Data Mahasiswa" ), wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.Nama = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.Nama.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Narrow" ) )
		
		fgSizer3.Add( self.Nama, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nim", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.Nim = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer3.Add( self.Nim, 0, wx.ALL, 5 )
		
		self.Prodi = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Prodi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Prodi.Wrap( -1 )
		fgSizer3.Add( self.Prodi, 0, wx.ALL, 5 )
		
		ProdiChoices = [ u"Sistem Informasi", u"Teknologi Informasi", u"Informatika" ]
		self.Prodi = wx.ComboBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"pilih", wx.DefaultPosition, wx.Size( 150,-1 ), ProdiChoices, 0 )
		fgSizer3.Add( self.Prodi, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		fgSizer3.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		sbSizer3.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer3 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar2.Append( self.m_menu1, u"Home" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menubar2.Append( self.m_menu2, u"Menu" ) 
		
		self.m_menu3 = wx.Menu()
		self.m_menubar2.Append( self.m_menu3, u"About Us" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Prodi.Bind( wx.EVT_COMBOBOX, self.m_comboBox1OnCombobox )
		self.Prodi.Bind( wx.EVT_TEXT, self.m_comboBox1OnText )
		self.Prodi.Bind( wx.EVT_TEXT_ENTER, self.m_comboBox1OnTextEnter )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_comboBox1OnCombobox( self, event ):
		event.Skip()
	
	def m_comboBox1OnText( self, event ):
		event.Skip()
	
	def m_comboBox1OnTextEnter( self, event ):
		event.Skip()
	
	def m_button2OnButtonClick( self, event ):
		event.Skip()
	

