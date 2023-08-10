# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class keytest
###########################################################################

class keytest ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Keyboard Input Tester v0.2", pos = wx.DefaultPosition, size = wx.Size( 800,597 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.RESIZE_BORDER|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,330 ), wx.Size( 800,-1 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.WANTS_CHARS )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_uk = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer65 = wx.BoxSizer( wx.VERTICAL )

		bSizer65.SetMinSize( wx.Size( -1,232 ) )
		self.m_dummy = wx.TextCtrl( self.m_uk, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dummy.SetMaxLength( 0 )
		self.m_dummy.Hide()

		bSizer65.Add( self.m_dummy, 0, wx.ALL, 5 )


		bSizer65.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		bSizer67 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_escape = wx.Button( self.m_uk, wx.ID_ANY, u"Esc", wx.DefaultPosition, wx.Size( 36,35 ), 0 )
		bSizer67.Add( self.m_escape, 0, wx.ALL, 0 )


		bSizer67.Add( ( 16, 0), 0, wx.EXPAND, 5 )

		self.m_f1 = wx.Button( self.m_uk, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f1, 0, wx.ALL, 0 )

		self.m_f2 = wx.Button( self.m_uk, wx.ID_ANY, u"F2", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f2, 0, wx.ALL, 0 )

		self.m_f3 = wx.Button( self.m_uk, wx.ID_ANY, u"F3", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f3, 0, wx.ALL, 0 )

		self.m_f4 = wx.Button( self.m_uk, wx.ID_ANY, u"F4", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f4, 0, wx.ALL, 0 )


		bSizer67.Add( ( 15, 0), 0, wx.EXPAND, 5 )

		self.m_f5 = wx.Button( self.m_uk, wx.ID_ANY, u"F5", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f5, 0, wx.ALL, 0 )

		self.m_f6 = wx.Button( self.m_uk, wx.ID_ANY, u"F6", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f6, 0, wx.ALL, 0 )

		self.m_f7 = wx.Button( self.m_uk, wx.ID_ANY, u"F7", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f7, 0, wx.ALL, 0 )

		self.m_f8 = wx.Button( self.m_uk, wx.ID_ANY, u"F8", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f8, 0, wx.ALL, 0 )


		bSizer67.Add( ( 15, 0), 0, wx.EXPAND, 5 )

		self.m_f9 = wx.Button( self.m_uk, wx.ID_ANY, u"F9", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f9, 0, wx.ALL, 0 )

		self.m_f10 = wx.Button( self.m_uk, wx.ID_ANY, u"F10", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f10, 0, wx.ALL, 0 )

		self.m_f11 = wx.Button( self.m_uk, wx.ID_ANY, u"F11", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f11, 0, wx.ALL, 0 )

		self.m_f12 = wx.Button( self.m_uk, wx.ID_ANY, u"F12", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer67.Add( self.m_f12, 0, wx.ALL, 0 )


		bSizer67.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_print = wx.Button( self.m_uk, wx.ID_ANY, u"PrtSc", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_print.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer67.Add( self.m_print, 0, wx.ALL, 0 )

		self.m_scroll = wx.Button( self.m_uk, wx.ID_ANY, u"ScrLk", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_scroll.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer67.Add( self.m_scroll, 0, wx.ALL, 0 )

		self.m_break = wx.Button( self.m_uk, wx.ID_ANY, u"Pause\nBreak", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_break.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer67.Add( self.m_break, 0, wx.ALL, 0 )


		bSizer67.Add( ( 16, 0), 0, wx.EXPAND, 5 )

		self.m_KADE1 = wx.BitmapButton( self.m_uk, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 136,35 ), wx.BU_AUTODRAW|wx.BORDER_NONE|wx.BORDER_NONE )

		self.m_KADE1.SetBitmap( wx.Bitmap( u"resources/keyboard.png", wx.BITMAP_TYPE_ANY ) )
		bSizer67.Add( self.m_KADE1, 0, 0, 5 )


		bSizer65.Add( bSizer67, 0, wx.EXPAND, 0 )


		bSizer65.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_squiggle = wx.Button( self.m_uk, wx.ID_ANY, u"`\n¬", wx.DefaultPosition, wx.Size( 36,35 ), 0 )
		self.m_squiggle.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_squiggle, 0, wx.ALL, 0 )

		self.m_1 = wx.Button( self.m_uk, wx.ID_ANY, u"!\n1", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_1.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_1, 0, wx.ALL, 0 )

		self.m_2 = wx.Button( self.m_uk, wx.ID_ANY, u"\"\n2", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_2.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_2, 0, wx.ALL, 0 )

		self.m_3 = wx.Button( self.m_uk, wx.ID_ANY, u"£\n3", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_3.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_3, 0, wx.ALL, 0 )

		self.m_4 = wx.Button( self.m_uk, wx.ID_ANY, u"$\n4", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_4.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_4, 0, wx.ALL, 0 )

		self.m_5 = wx.Button( self.m_uk, wx.ID_ANY, u"%\n5", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_5.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_5, 0, wx.ALL, 0 )

		self.m_6 = wx.Button( self.m_uk, wx.ID_ANY, u"^\n6", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_6.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_6, 0, wx.ALL, 0 )

		self.m_7 = wx.Button( self.m_uk, wx.ID_ANY, u"&&\n7", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_7.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_7, 0, wx.ALL, 0 )

		self.m_8 = wx.Button( self.m_uk, wx.ID_ANY, u"*\n8", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_8.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_8, 0, wx.ALL, 0 )

		self.m_9 = wx.Button( self.m_uk, wx.ID_ANY, u"(\n9", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_9.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_9, 0, wx.ALL, 0 )

		self.m_0 = wx.Button( self.m_uk, wx.ID_ANY, u")\n0", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_0.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_0, 0, wx.ALL, 0 )

		self.m_minus = wx.Button( self.m_uk, wx.ID_ANY, u"_\n-", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_minus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_minus, 0, wx.ALL, 0 )

		self.m_plus = wx.Button( self.m_uk, wx.ID_ANY, u"+\n=", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_plus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_plus, 0, wx.ALL, 0 )

		self.m_backspace = wx.Button( self.m_uk, wx.ID_ANY, u"Back\nSpace", wx.DefaultPosition, wx.Size( 46,35 ), 0 )
		self.m_backspace.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_backspace, 0, wx.ALL, 0 )


		bSizer68.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_insert = wx.Button( self.m_uk, wx.ID_ANY, u"Ins", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_insert.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_insert, 0, wx.ALL, 0 )

		self.m_home = wx.Button( self.m_uk, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_home.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_home, 0, wx.ALL, 0 )

		self.m_page_up = wx.Button( self.m_uk, wx.ID_ANY, u"Page\nUp", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_page_up.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_page_up, 0, wx.ALL, 0 )


		bSizer68.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_numlock = wx.Button( self.m_uk, wx.ID_ANY, u"Num\nLock", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_numlock.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_numlock, 0, wx.ALL, 0 )

		self.m_num_slash = wx.Button( self.m_uk, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num_slash.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_num_slash, 0, wx.ALL, 0 )

		self.m_num_asterix = wx.Button( self.m_uk, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num_asterix.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_num_asterix, 0, wx.ALL, 0 )

		self.m_num_minus = wx.Button( self.m_uk, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num_minus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68.Add( self.m_num_minus, 0, wx.ALL, 0 )


		bSizer65.Add( bSizer68, 0, wx.EXPAND, 0 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_tab = wx.Button( self.m_uk, wx.ID_ANY, u"Tab", wx.DefaultPosition, wx.Size( 36,35 ), 0 )
		bSizer8.Add( self.m_tab, 0, wx.ALL, 0 )

		self.m_q = wx.Button( self.m_uk, wx.ID_ANY, u"Q", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_q, 0, wx.ALL, 0 )

		self.m_w = wx.Button( self.m_uk, wx.ID_ANY, u"W", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_w, 0, wx.ALL, 0 )

		self.m_e = wx.Button( self.m_uk, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_e, 0, wx.ALL, 0 )

		self.m_r = wx.Button( self.m_uk, wx.ID_ANY, u"R", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_r, 0, wx.ALL, 0 )

		self.m_t = wx.Button( self.m_uk, wx.ID_ANY, u"T", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_t, 0, wx.ALL, 0 )

		self.m_y = wx.Button( self.m_uk, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_y, 0, wx.ALL, 0 )

		self.m_u = wx.Button( self.m_uk, wx.ID_ANY, u"U", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_u, 0, wx.ALL, 0 )

		self.m_i = wx.Button( self.m_uk, wx.ID_ANY, u"I", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_i, 0, wx.ALL, 0 )

		self.m_o = wx.Button( self.m_uk, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_o, 0, wx.ALL, 0 )

		self.m_p = wx.Button( self.m_uk, wx.ID_ANY, u"P", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer8.Add( self.m_p, 0, wx.ALL, 0 )

		self.m_left_brace = wx.Button( self.m_uk, wx.ID_ANY, u"{\n[", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_left_brace.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer8.Add( self.m_left_brace, 0, wx.ALL, 0 )

		self.m_right_brace = wx.Button( self.m_uk, wx.ID_ANY, u"}\n]", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_right_brace.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer8.Add( self.m_right_brace, 0, wx.ALL, 0 )


		bSizer11.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_caps_lock = wx.Button( self.m_uk, wx.ID_ANY, u"Caps\nLock", wx.DefaultPosition, wx.Size( 36,35 ), 0 )
		self.m_caps_lock.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer81.Add( self.m_caps_lock, 0, wx.ALL, 0 )

		self.m_a = wx.Button( self.m_uk, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_a, 0, wx.ALL, 0 )

		self.m_s = wx.Button( self.m_uk, wx.ID_ANY, u"S", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_s, 0, wx.ALL, 0 )

		self.m_d = wx.Button( self.m_uk, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_d, 0, wx.ALL, 0 )

		self.m_f = wx.Button( self.m_uk, wx.ID_ANY, u"F", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_f, 0, wx.ALL, 0 )

		self.m_g = wx.Button( self.m_uk, wx.ID_ANY, u"G", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_g, 0, wx.ALL, 0 )

		self.m_h = wx.Button( self.m_uk, wx.ID_ANY, u"H", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_h, 0, wx.ALL, 0 )

		self.m_j = wx.Button( self.m_uk, wx.ID_ANY, u"J", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_j, 0, wx.ALL, 0 )

		self.m_k = wx.Button( self.m_uk, wx.ID_ANY, u"K", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_k, 0, wx.ALL, 0 )

		self.m_l = wx.Button( self.m_uk, wx.ID_ANY, u"L", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer81.Add( self.m_l, 0, wx.ALL, 0 )

		self.m_colon = wx.Button( self.m_uk, wx.ID_ANY, u":\n;", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_colon.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer81.Add( self.m_colon, 0, wx.ALL, 0 )

		self.m_at = wx.Button( self.m_uk, wx.ID_ANY, u"@\n'", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_at.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer81.Add( self.m_at, 0, wx.ALL, 0 )

		self.m_tilde = wx.Button( self.m_uk, wx.ID_ANY, u"~\n#", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_tilde.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer81.Add( self.m_tilde, 0, wx.ALL, 0 )


		bSizer11.Add( bSizer81, 0, wx.EXPAND, 5 )


		bSizer9.Add( bSizer11, 0, wx.EXPAND, 5 )

		self.m_enter = wx.Button( self.m_uk, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 46,70 ), 0 )
		bSizer9.Add( self.m_enter, 0, wx.ALL, 0 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer681 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer681.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_delete = wx.Button( self.m_uk, wx.ID_ANY, u"Del", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_delete.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681.Add( self.m_delete, 0, wx.ALL, 0 )

		self.m_end = wx.Button( self.m_uk, wx.ID_ANY, u"End", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_end.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681.Add( self.m_end, 0, wx.ALL, 0 )

		self.m_page_down = wx.Button( self.m_uk, wx.ID_ANY, u"Page\nDown", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_page_down.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681.Add( self.m_page_down, 0, wx.ALL, 0 )


		bSizer681.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_num7 = wx.Button( self.m_uk, wx.ID_ANY, u"7\nHme", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num7.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681.Add( self.m_num7, 0, wx.ALL, 0 )

		self.m_num8 = wx.Button( self.m_uk, wx.ID_ANY, u"8\n˄", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num8.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681.Add( self.m_num8, 0, wx.ALL, 0 )

		self.m_num9 = wx.Button( self.m_uk, wx.ID_ANY, u"9\nPgUp", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num9.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681.Add( self.m_num9, 0, wx.ALL, 0 )


		bSizer15.Add( bSizer681, 0, wx.EXPAND, 5 )

		bSizer6811 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6811.Add( ( 130, 0), 0, wx.EXPAND, 5 )

		self.m_num4 = wx.Button( self.m_uk, wx.ID_ANY, u"4\n˂", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num4.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6811.Add( self.m_num4, 0, wx.ALL, 0 )

		self.m_num5 = wx.Button( self.m_uk, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num5.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6811.Add( self.m_num5, 0, wx.ALL, 0 )

		self.m_num6 = wx.Button( self.m_uk, wx.ID_ANY, u"6\n˃", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num6.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6811.Add( self.m_num6, 0, wx.ALL, 0 )


		bSizer15.Add( bSizer6811, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer15, 0, wx.EXPAND, 0 )

		self.m_num_plus = wx.Button( self.m_uk, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 38,70 ), 0 )
		self.m_num_plus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer9.Add( self.m_num_plus, 0, wx.ALL, 0 )


		bSizer65.Add( bSizer9, 0, wx.EXPAND, 5 )

		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		bSizer82 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_left_shift = wx.Button( self.m_uk, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 36,35 ), 0 )
		bSizer82.Add( self.m_left_shift, 0, wx.ALL, 0 )

		self.m_backslash = wx.Button( self.m_uk, wx.ID_ANY, u"|\n\\", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_backslash.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer82.Add( self.m_backslash, 0, wx.ALL, 0 )

		self.m_z = wx.Button( self.m_uk, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer82.Add( self.m_z, 0, wx.ALL, 0 )

		self.m_x = wx.Button( self.m_uk, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer82.Add( self.m_x, 0, wx.ALL, 0 )

		self.m_c = wx.Button( self.m_uk, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer82.Add( self.m_c, 0, wx.ALL, 0 )

		self.m_v = wx.Button( self.m_uk, wx.ID_ANY, u"V", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer82.Add( self.m_v, 0, wx.ALL, 0 )

		self.m_b = wx.Button( self.m_uk, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer82.Add( self.m_b, 0, wx.ALL, 0 )

		self.m_n = wx.Button( self.m_uk, wx.ID_ANY, u"N", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer82.Add( self.m_n, 0, wx.ALL, 0 )

		self.m_m = wx.Button( self.m_uk, wx.ID_ANY, u"M", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer82.Add( self.m_m, 0, wx.ALL, 0 )

		self.m_comma = wx.Button( self.m_uk, wx.ID_ANY, u"<\n,", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_comma.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer82.Add( self.m_comma, 0, wx.ALL, 0 )

		self.m_period = wx.Button( self.m_uk, wx.ID_ANY, u">\n.", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_period.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer82.Add( self.m_period, 0, wx.ALL, 0 )

		self.m_question = wx.Button( self.m_uk, wx.ID_ANY, u"?\n/", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.m_question.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer82.Add( self.m_question, 0, wx.ALL, 0 )

		self.m_right_shift = wx.Button( self.m_uk, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 80,35 ), 0 )
		bSizer82.Add( self.m_right_shift, 0, wx.ALL, 0 )


		bSizer111.Add( bSizer82, 0, wx.EXPAND, 5 )

		bSizer811 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_left_ctrl = wx.Button( self.m_uk, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 50,35 ), 0 )
		bSizer811.Add( self.m_left_ctrl, 0, wx.ALL, 0 )

		self.m_left_windows = wx.Button( self.m_uk, wx.ID_ANY, u"Win\nKey", wx.DefaultPosition, wx.Size( 54,35 ), 0 )
		self.m_left_windows.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer811.Add( self.m_left_windows, 0, wx.ALL, 0 )

		self.m_left_alt = wx.Button( self.m_uk, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.Size( 51,35 ), 0 )
		bSizer811.Add( self.m_left_alt, 0, wx.ALL, 0 )

		self.m_space = wx.Button( self.m_uk, wx.ID_ANY, u"Space", wx.DefaultPosition, wx.Size( 130,35 ), 0 )
		bSizer811.Add( self.m_space, 0, wx.ALL, 0 )

		self.m_right_alt = wx.Button( self.m_uk, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.Size( 51,35 ), 0 )
		bSizer811.Add( self.m_right_alt, 0, wx.ALL, 0 )

		self.m_right_windows = wx.Button( self.m_uk, wx.ID_ANY, u"Win\nKey", wx.DefaultPosition, wx.Size( 54,35 ), 0 )
		self.m_right_windows.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer811.Add( self.m_right_windows, 0, wx.ALL, 0 )

		self.m_menu = wx.Button( self.m_uk, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.Size( 50,35 ), 0|wx.WANTS_CHARS )
		self.m_menu.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )

		bSizer811.Add( self.m_menu, 0, wx.ALL, 0 )

		self.m_right_ctrl = wx.Button( self.m_uk, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 50,35 ), 0 )
		bSizer811.Add( self.m_right_ctrl, 0, wx.ALL, 0 )


		bSizer111.Add( bSizer811, 0, wx.EXPAND, 5 )


		bSizer91.Add( bSizer111, 0, wx.EXPAND, 5 )

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		bSizer6812 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6812.Add( ( 8, 0), 0, wx.EXPAND, 5 )


		bSizer6812.Add( ( 38, 0), 0, wx.EXPAND, 0 )

		self.m_up = wx.Button( self.m_uk, wx.ID_ANY, u"Up", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_up.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6812.Add( self.m_up, 0, wx.ALL, 0 )


		bSizer6812.Add( ( 38, 0), 0, wx.EXPAND, 5 )


		bSizer6812.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_num1 = wx.Button( self.m_uk, wx.ID_ANY, u"1\nEnd", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num1.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6812.Add( self.m_num1, 0, wx.ALL, 0 )

		self.m_num2 = wx.Button( self.m_uk, wx.ID_ANY, u"2\n˅", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num2.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6812.Add( self.m_num2, 0, wx.ALL, 0 )

		self.m_num3 = wx.Button( self.m_uk, wx.ID_ANY, u"3\nPgDn", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num3.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6812.Add( self.m_num3, 0, wx.ALL, 0 )


		bSizer151.Add( bSizer6812, 0, wx.EXPAND, 5 )

		bSizer68111 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer68111.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_left = wx.Button( self.m_uk, wx.ID_ANY, u"Left", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_left.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68111.Add( self.m_left, 0, wx.ALL, 0 )

		self.m_down = wx.Button( self.m_uk, wx.ID_ANY, u"Down", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_down.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68111.Add( self.m_down, 0, wx.ALL, 0 )

		self.m_right = wx.Button( self.m_uk, wx.ID_ANY, u"Right", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_right.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68111.Add( self.m_right, 0, wx.ALL, 0 )


		bSizer68111.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.m_num0 = wx.Button( self.m_uk, wx.ID_ANY, u"0\nIns", wx.DefaultPosition, wx.Size( 76,35 ), 0 )
		self.m_num0.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68111.Add( self.m_num0, 0, wx.ALL, 0 )

		self.m_num_period = wx.Button( self.m_uk, wx.ID_ANY, u".\nDel", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.m_num_period.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68111.Add( self.m_num_period, 0, wx.ALL, 0 )


		bSizer151.Add( bSizer68111, 1, wx.EXPAND, 5 )


		bSizer91.Add( bSizer151, 0, wx.EXPAND, 0 )

		self.m_num_enter = wx.Button( self.m_uk, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 38,70 ), 0 )
		self.m_num_enter.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer91.Add( self.m_num_enter, 0, wx.ALL, 0 )


		bSizer65.Add( bSizer91, 1, wx.EXPAND, 5 )


		self.m_uk.SetSizer( bSizer65 )
		self.m_uk.Layout()
		bSizer65.Fit( self.m_uk )
		bSizer24.Add( self.m_uk, 0, wx.EXPAND|wx.TOP, 10 )

		self.m_us = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_us.Hide()

		bSizer651 = wx.BoxSizer( wx.VERTICAL )

		bSizer651.SetMinSize( wx.Size( -1,232 ) )
		self.m_dummy1 = wx.TextCtrl( self.m_us, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dummy1.SetMaxLength( 0 )
		self.m_dummy1.Hide()

		bSizer651.Add( self.m_dummy1, 0, wx.ALL, 5 )


		bSizer651.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		bSizer671 = wx.BoxSizer( wx.HORIZONTAL )

		self.mus_escape = wx.Button( self.m_us, wx.ID_ANY, u"Esc", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_escape, 0, wx.ALL, 0 )


		bSizer671.Add( ( 16, 0), 0, wx.EXPAND, 5 )

		self.mus_f1 = wx.Button( self.m_us, wx.ID_ANY, u"F1", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f1, 0, wx.ALL, 0 )

		self.mus_f2 = wx.Button( self.m_us, wx.ID_ANY, u"F2", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f2, 0, wx.ALL, 0 )

		self.mus_f3 = wx.Button( self.m_us, wx.ID_ANY, u"F3", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f3, 0, wx.ALL, 0 )

		self.mus_f4 = wx.Button( self.m_us, wx.ID_ANY, u"F4", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f4, 0, wx.ALL, 0 )


		bSizer671.Add( ( 16, 0), 0, wx.EXPAND, 5 )

		self.mus_f5 = wx.Button( self.m_us, wx.ID_ANY, u"F5", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f5, 0, wx.ALL, 0 )

		self.mus_f6 = wx.Button( self.m_us, wx.ID_ANY, u"F6", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f6, 0, wx.ALL, 0 )

		self.mus_f7 = wx.Button( self.m_us, wx.ID_ANY, u"F7", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f7, 0, wx.ALL, 0 )

		self.mus_f8 = wx.Button( self.m_us, wx.ID_ANY, u"F8", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f8, 0, wx.ALL, 0 )


		bSizer671.Add( ( 16, 0), 0, wx.EXPAND, 5 )

		self.mus_f9 = wx.Button( self.m_us, wx.ID_ANY, u"F9", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f9, 0, wx.ALL, 0 )

		self.mus_f10 = wx.Button( self.m_us, wx.ID_ANY, u"F10", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f10, 0, wx.ALL, 0 )

		self.mus_f11 = wx.Button( self.m_us, wx.ID_ANY, u"F11", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f11, 0, wx.ALL, 0 )

		self.mus_f12 = wx.Button( self.m_us, wx.ID_ANY, u"F12", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer671.Add( self.mus_f12, 0, wx.ALL, 0 )


		bSizer671.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.mus_print = wx.Button( self.m_us, wx.ID_ANY, u"PrtSc", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_print.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer671.Add( self.mus_print, 0, wx.ALL, 0 )

		self.mus_scroll = wx.Button( self.m_us, wx.ID_ANY, u"ScrLk", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_scroll.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer671.Add( self.mus_scroll, 0, wx.ALL, 0 )

		self.mus_break = wx.Button( self.m_us, wx.ID_ANY, u"Pause\nBreak", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_break.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer671.Add( self.mus_break, 0, wx.ALL, 0 )


		bSizer671.Add( ( 16, 0), 0, wx.EXPAND, 5 )

		self.m_KADE2 = wx.BitmapButton( self.m_us, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 136,35 ), wx.BU_AUTODRAW|0|wx.BORDER_NONE )

		self.m_KADE2.SetBitmap( wx.Bitmap( u"resources/keyboard.png", wx.BITMAP_TYPE_ANY ) )
		bSizer671.Add( self.m_KADE2, 0, 0, 5 )


		bSizer651.Add( bSizer671, 0, wx.EXPAND, 0 )


		bSizer651.Add( ( 0, 10), 0, wx.EXPAND, 5 )

		bSizer682 = wx.BoxSizer( wx.HORIZONTAL )

		self.mus_squiggle = wx.Button( self.m_us, wx.ID_ANY, u"~\n`", wx.DefaultPosition, wx.Size( 32,35 ), 0 )
		self.mus_squiggle.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_squiggle, 0, wx.ALL, 0 )

		self.mus_1 = wx.Button( self.m_us, wx.ID_ANY, u"!\n1", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_1.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_1, 0, wx.ALL, 0 )

		self.mus_2 = wx.Button( self.m_us, wx.ID_ANY, u"@\n2", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_2.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_2, 0, wx.ALL, 0 )

		self.mus_3 = wx.Button( self.m_us, wx.ID_ANY, u"#\n3", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_3.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_3, 0, wx.ALL, 0 )

		self.mus_4 = wx.Button( self.m_us, wx.ID_ANY, u"$\n4", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_4.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_4, 0, wx.ALL, 0 )

		self.mus_5 = wx.Button( self.m_us, wx.ID_ANY, u"%\n5", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_5.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_5, 0, wx.ALL, 0 )

		self.mus_6 = wx.Button( self.m_us, wx.ID_ANY, u"^\n6", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_6.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_6, 0, wx.ALL, 0 )

		self.mus_7 = wx.Button( self.m_us, wx.ID_ANY, u"&&\n7", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_7.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_7, 0, wx.ALL, 0 )

		self.mus_8 = wx.Button( self.m_us, wx.ID_ANY, u"*\n8", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_8.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_8, 0, wx.ALL, 0 )

		self.mus_9 = wx.Button( self.m_us, wx.ID_ANY, u"(\n9", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_9.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_9, 0, wx.ALL, 0 )

		self.mus_0 = wx.Button( self.m_us, wx.ID_ANY, u")\n0", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_0.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_0, 0, wx.ALL, 0 )

		self.mus_minus = wx.Button( self.m_us, wx.ID_ANY, u"_\n-", wx.DefaultPosition, wx.Size( 33,35 ), 0 )
		self.mus_minus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_minus, 0, wx.ALL, 0 )

		self.mus_plus = wx.Button( self.m_us, wx.ID_ANY, u"+\n=", wx.DefaultPosition, wx.Size( 33,35 ), 0 )
		self.mus_plus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_plus, 0, wx.ALL, 0 )

		self.mus_backspace = wx.Button( self.m_us, wx.ID_ANY, u"Back\nSpace", wx.DefaultPosition, wx.Size( 52,35 ), 0 )
		self.mus_backspace.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_backspace, 0, wx.ALL, 0 )


		bSizer682.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.mus_insert = wx.Button( self.m_us, wx.ID_ANY, u"Ins", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_insert.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_insert, 0, wx.ALL, 0 )

		self.mus_home = wx.Button( self.m_us, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_home.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_home, 0, wx.ALL, 0 )

		self.mus_page_up = wx.Button( self.m_us, wx.ID_ANY, u"Page\nUp", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_page_up.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_page_up, 0, wx.ALL, 0 )


		bSizer682.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.mus_numlock = wx.Button( self.m_us, wx.ID_ANY, u"Num\nLock", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_numlock.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_numlock, 0, wx.ALL, 0 )

		self.mus_num_slash = wx.Button( self.m_us, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num_slash.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_num_slash, 0, wx.ALL, 0 )

		self.mus_num_asterix = wx.Button( self.m_us, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num_asterix.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_num_asterix, 0, wx.ALL, 0 )

		self.mus_num_minus = wx.Button( self.m_us, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num_minus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer682.Add( self.mus_num_minus, 0, wx.ALL, 0 )


		bSizer651.Add( bSizer682, 0, wx.EXPAND, 0 )

		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer112 = wx.BoxSizer( wx.VERTICAL )

		bSizer83 = wx.BoxSizer( wx.HORIZONTAL )

		self.mus_tab = wx.Button( self.m_us, wx.ID_ANY, u"Tab", wx.DefaultPosition, wx.Size( 48,35 ), 0 )
		bSizer83.Add( self.mus_tab, 0, wx.ALL, 0 )

		self.mus_q = wx.Button( self.m_us, wx.ID_ANY, u"Q", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_q, 0, wx.ALL, 0 )

		self.mus_w = wx.Button( self.m_us, wx.ID_ANY, u"W", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_w, 0, wx.ALL, 0 )

		self.mus_e = wx.Button( self.m_us, wx.ID_ANY, u"E", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_e, 0, wx.ALL, 0 )

		self.mus_r = wx.Button( self.m_us, wx.ID_ANY, u"R", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_r, 0, wx.ALL, 0 )

		self.mus_t = wx.Button( self.m_us, wx.ID_ANY, u"T", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_t, 0, wx.ALL, 0 )

		self.mus_y = wx.Button( self.m_us, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_y, 0, wx.ALL, 0 )

		self.mus_u = wx.Button( self.m_us, wx.ID_ANY, u"U", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_u, 0, wx.ALL, 0 )

		self.mus_i = wx.Button( self.m_us, wx.ID_ANY, u"I", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_i, 0, wx.ALL, 0 )

		self.mus_o = wx.Button( self.m_us, wx.ID_ANY, u"O", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_o, 0, wx.ALL, 0 )

		self.mus_p = wx.Button( self.m_us, wx.ID_ANY, u"P", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer83.Add( self.mus_p, 0, wx.ALL, 0 )

		self.mus_left_brace = wx.Button( self.m_us, wx.ID_ANY, u"{\n[", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_left_brace.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer83.Add( self.mus_left_brace, 0, wx.ALL, 0 )

		self.mus_right_brace = wx.Button( self.m_us, wx.ID_ANY, u"}\n]", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_right_brace.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer83.Add( self.mus_right_brace, 0, wx.ALL, 0 )

		self.mus_backslash = wx.Button( self.m_us, wx.ID_ANY, u"|\n\\", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_backslash.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer83.Add( self.mus_backslash, 0, wx.ALL, 0 )


		bSizer112.Add( bSizer83, 0, wx.EXPAND, 5 )

		bSizer812 = wx.BoxSizer( wx.HORIZONTAL )

		self.mus_caps_lock = wx.Button( self.m_us, wx.ID_ANY, u"Caps\nLock", wx.DefaultPosition, wx.Size( 58,35 ), 0 )
		self.mus_caps_lock.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer812.Add( self.mus_caps_lock, 0, wx.ALL, 0 )

		self.mus_a = wx.Button( self.m_us, wx.ID_ANY, u"A", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_a, 0, wx.ALL, 0 )

		self.mus_s = wx.Button( self.m_us, wx.ID_ANY, u"S", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_s, 0, wx.ALL, 0 )

		self.mus_d = wx.Button( self.m_us, wx.ID_ANY, u"D", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_d, 0, wx.ALL, 0 )

		self.mus_f = wx.Button( self.m_us, wx.ID_ANY, u"F", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_f, 0, wx.ALL, 0 )

		self.mus_g = wx.Button( self.m_us, wx.ID_ANY, u"G", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_g, 0, wx.ALL, 0 )

		self.mus_h = wx.Button( self.m_us, wx.ID_ANY, u"H", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_h, 0, wx.ALL, 0 )

		self.mus_j = wx.Button( self.m_us, wx.ID_ANY, u"J", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_j, 0, wx.ALL, 0 )

		self.mus_k = wx.Button( self.m_us, wx.ID_ANY, u"K", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_k, 0, wx.ALL, 0 )

		self.mus_l = wx.Button( self.m_us, wx.ID_ANY, u"L", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer812.Add( self.mus_l, 0, wx.ALL, 0 )

		self.mus_colon = wx.Button( self.m_us, wx.ID_ANY, u":\n;", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_colon.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer812.Add( self.mus_colon, 0, wx.ALL, 0 )

		self.mus_at = wx.Button( self.m_us, wx.ID_ANY, u"\"\n'", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_at.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer812.Add( self.mus_at, 0, wx.ALL, 0 )

		self.mus_enter = wx.Button( self.m_us, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 58,35 ), 0 )
		bSizer812.Add( self.mus_enter, 0, wx.ALL, 0 )


		bSizer112.Add( bSizer812, 0, wx.EXPAND, 5 )


		bSizer92.Add( bSizer112, 0, wx.EXPAND, 5 )

		bSizer152 = wx.BoxSizer( wx.VERTICAL )

		bSizer6813 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6813.Add( ( 8, 0), 0, wx.EXPAND, 0 )

		self.mus_delete = wx.Button( self.m_us, wx.ID_ANY, u"Del", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_delete.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6813.Add( self.mus_delete, 0, wx.ALL, 0 )

		self.mus_end = wx.Button( self.m_us, wx.ID_ANY, u"End", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_end.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6813.Add( self.mus_end, 0, wx.ALL, 0 )

		self.mus_page_down = wx.Button( self.m_us, wx.ID_ANY, u"Page\nDown", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_page_down.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6813.Add( self.mus_page_down, 0, wx.ALL, 0 )


		bSizer6813.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.mus_num7 = wx.Button( self.m_us, wx.ID_ANY, u"7\nHme", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num7.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6813.Add( self.mus_num7, 0, wx.ALL, 0 )

		self.mus_num8 = wx.Button( self.m_us, wx.ID_ANY, u"8\n˄", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num8.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6813.Add( self.mus_num8, 0, wx.ALL, 0 )

		self.mus_num9 = wx.Button( self.m_us, wx.ID_ANY, u"9\nPgUp", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num9.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6813.Add( self.mus_num9, 0, wx.ALL, 0 )


		bSizer152.Add( bSizer6813, 0, wx.EXPAND, 5 )

		bSizer68112 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer68112.Add( ( 130, 0), 0, wx.EXPAND, 5 )

		self.mus_num4 = wx.Button( self.m_us, wx.ID_ANY, u"4\n˂", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num4.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68112.Add( self.mus_num4, 0, wx.ALL, 0 )

		self.mus_num5 = wx.Button( self.m_us, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num5.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68112.Add( self.mus_num5, 0, wx.ALL, 0 )

		self.mus_num6 = wx.Button( self.m_us, wx.ID_ANY, u"6\n˃", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num6.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68112.Add( self.mus_num6, 0, wx.ALL, 0 )


		bSizer152.Add( bSizer68112, 1, wx.EXPAND, 5 )


		bSizer92.Add( bSizer152, 0, wx.EXPAND, 0 )

		self.mus_num_plus = wx.Button( self.m_us, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 38,70 ), 0 )
		self.mus_num_plus.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer92.Add( self.mus_num_plus, 0, wx.ALL, 0 )


		bSizer651.Add( bSizer92, 0, wx.EXPAND, 5 )

		bSizer911 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer1111 = wx.BoxSizer( wx.VERTICAL )

		bSizer821 = wx.BoxSizer( wx.HORIZONTAL )

		self.mus_left_shift = wx.Button( self.m_us, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 75,35 ), 0 )
		bSizer821.Add( self.mus_left_shift, 0, wx.ALL, 0 )

		self.mus_z = wx.Button( self.m_us, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer821.Add( self.mus_z, 0, wx.ALL, 0 )

		self.mus_x = wx.Button( self.m_us, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer821.Add( self.mus_x, 0, wx.ALL, 0 )

		self.mus_c = wx.Button( self.m_us, wx.ID_ANY, u"C", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer821.Add( self.mus_c, 0, wx.ALL, 0 )

		self.mus_v = wx.Button( self.m_us, wx.ID_ANY, u"V", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer821.Add( self.mus_v, 0, wx.ALL, 0 )

		self.mus_b = wx.Button( self.m_us, wx.ID_ANY, u"B", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer821.Add( self.mus_b, 0, wx.ALL, 0 )

		self.mus_n = wx.Button( self.m_us, wx.ID_ANY, u"N", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer821.Add( self.mus_n, 0, wx.ALL, 0 )

		self.mus_m = wx.Button( self.m_us, wx.ID_ANY, u"M", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		bSizer821.Add( self.mus_m, 0, wx.ALL, 0 )

		self.mus_comma = wx.Button( self.m_us, wx.ID_ANY, u"<\n,", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_comma.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer821.Add( self.mus_comma, 0, wx.ALL, 0 )

		self.mus_period = wx.Button( self.m_us, wx.ID_ANY, u">\n.", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_period.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer821.Add( self.mus_period, 0, wx.ALL, 0 )

		self.mus_question = wx.Button( self.m_us, wx.ID_ANY, u"?\n/", wx.DefaultPosition, wx.Size( 34,35 ), 0 )
		self.mus_question.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer821.Add( self.mus_question, 0, wx.ALL, 0 )

		self.mus_right_shift = wx.Button( self.m_us, wx.ID_ANY, u"Shift", wx.DefaultPosition, wx.Size( 75,35 ), 0 )
		bSizer821.Add( self.mus_right_shift, 0, wx.ALL, 0 )


		bSizer1111.Add( bSizer821, 0, wx.EXPAND, 5 )

		bSizer8111 = wx.BoxSizer( wx.HORIZONTAL )

		self.mus_left_ctrl = wx.Button( self.m_us, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 48,35 ), 0 )
		bSizer8111.Add( self.mus_left_ctrl, 0, wx.ALL, 0 )

		self.mus_left_windows = wx.Button( self.m_us, wx.ID_ANY, u"Win\nKey", wx.DefaultPosition, wx.Size( 53,35 ), 0 )
		self.mus_left_windows.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer8111.Add( self.mus_left_windows, 0, wx.ALL, 0 )

		self.mus_left_alt = wx.Button( self.m_us, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.Size( 51,35 ), 0 )
		bSizer8111.Add( self.mus_left_alt, 0, wx.ALL, 0 )

		self.mus_space = wx.Button( self.m_us, wx.ID_ANY, u"Space", wx.DefaultPosition, wx.Size( 134,35 ), 0 )
		bSizer8111.Add( self.mus_space, 0, wx.ALL, 0 )

		self.mus_right_alt = wx.Button( self.m_us, wx.ID_ANY, u"Alt", wx.DefaultPosition, wx.Size( 51,35 ), 0 )
		bSizer8111.Add( self.mus_right_alt, 0, wx.ALL, 0 )

		self.mus_right_windows = wx.Button( self.m_us, wx.ID_ANY, u"Win\nKey", wx.DefaultPosition, wx.Size( 53,35 ), 0 )
		self.mus_right_windows.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer8111.Add( self.mus_right_windows, 0, wx.ALL, 0 )

		self.mus_menu = wx.Button( self.m_us, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.Size( 50,35 ), 0|wx.WANTS_CHARS )
		self.mus_menu.SetExtraStyle( wx.WS_EX_BLOCK_EVENTS )

		bSizer8111.Add( self.mus_menu, 0, wx.ALL, 0 )

		self.mus_right_ctrl = wx.Button( self.m_us, wx.ID_ANY, u"Ctrl", wx.DefaultPosition, wx.Size( 50,35 ), 0 )
		bSizer8111.Add( self.mus_right_ctrl, 0, wx.ALL, 0 )


		bSizer1111.Add( bSizer8111, 0, wx.EXPAND, 5 )


		bSizer911.Add( bSizer1111, 0, wx.EXPAND, 5 )

		bSizer1511 = wx.BoxSizer( wx.VERTICAL )

		bSizer68121 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer68121.Add( ( 8, 0), 0, wx.EXPAND, 5 )


		bSizer68121.Add( ( 38, 0), 0, wx.EXPAND, 0 )

		self.mus_up = wx.Button( self.m_us, wx.ID_ANY, u"Up", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_up.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68121.Add( self.mus_up, 0, wx.ALL, 0 )


		bSizer68121.Add( ( 38, 0), 0, wx.EXPAND, 5 )


		bSizer68121.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.mus_num1 = wx.Button( self.m_us, wx.ID_ANY, u"1\nEnd", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num1.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68121.Add( self.mus_num1, 0, wx.ALL, 0 )

		self.mus_num2 = wx.Button( self.m_us, wx.ID_ANY, u"2\n˅", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num2.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68121.Add( self.mus_num2, 0, wx.ALL, 0 )

		self.mus_num3 = wx.Button( self.m_us, wx.ID_ANY, u"3\nPgDn", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num3.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer68121.Add( self.mus_num3, 0, wx.ALL, 0 )


		bSizer1511.Add( bSizer68121, 0, wx.EXPAND, 5 )

		bSizer681111 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer681111.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.mus_left = wx.Button( self.m_us, wx.ID_ANY, u"Left", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_left.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681111.Add( self.mus_left, 0, wx.ALL, 0 )

		self.mus_down = wx.Button( self.m_us, wx.ID_ANY, u"Down", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_down.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681111.Add( self.mus_down, 0, wx.ALL, 0 )

		self.mus_right = wx.Button( self.m_us, wx.ID_ANY, u"Right", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_right.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681111.Add( self.mus_right, 0, wx.ALL, 0 )


		bSizer681111.Add( ( 8, 0), 0, wx.EXPAND, 5 )

		self.mus_num0 = wx.Button( self.m_us, wx.ID_ANY, u"0\nIns", wx.DefaultPosition, wx.Size( 76,35 ), 0 )
		self.mus_num0.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681111.Add( self.mus_num0, 0, wx.ALL, 0 )

		self.mus_num_period = wx.Button( self.m_us, wx.ID_ANY, u".\nDel", wx.DefaultPosition, wx.Size( 38,35 ), 0 )
		self.mus_num_period.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer681111.Add( self.mus_num_period, 0, wx.ALL, 0 )


		bSizer1511.Add( bSizer681111, 1, wx.EXPAND, 5 )


		bSizer911.Add( bSizer1511, 0, wx.EXPAND, 0 )

		self.mus_num_enter = wx.Button( self.m_us, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 38,70 ), 0 )
		self.mus_num_enter.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer911.Add( self.mus_num_enter, 0, wx.ALL, 0 )


		bSizer651.Add( bSizer911, 1, wx.EXPAND, 5 )


		self.m_us.SetSizer( bSizer651 )
		self.m_us.Layout()
		bSizer651.Fit( self.m_us )
		bSizer24.Add( self.m_us, 0, wx.EXPAND|wx.TOP, 10 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )


		bSizer23.Add( ( 0, 15), 0, wx.ALL|wx.EXPAND, 0 )

		self.m_list = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_SIMPLE )
		self.m_list.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer23.Add( self.m_list, 1, wx.ALL|wx.EXPAND, 1 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_show_log = wx.Button( self.m_panel1, wx.ID_ANY, u"Hide Activity Log", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_show_log.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_show_log.SetToolTip( u"Show the keyboard activity log" )
		self.m_show_log.SetMinSize( wx.Size( 120,20 ) )

		bSizer26.Add( self.m_show_log, 0, wx.ALL, 2 )

		self.m_clear_list = wx.Button( self.m_panel1, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.Size( 75,20 ), 0 )
		self.m_clear_list.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_clear_list.SetToolTip( u"Clear the keyboard activity log" )

		bSizer26.Add( self.m_clear_list, 0, wx.ALL, 2 )

		self.m_show_up = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Show key up events", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_show_up.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_show_up.Enable( False )
		self.m_show_up.SetToolTip( u"Show key up as well as key down events" )

		bSizer26.Add( self.m_show_up, 0, wx.ALL, 5 )

		m_keyboardChoices = [ u"UK Keyboard", u"US Keyboard" ]
		self.m_keyboard = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,18 ), m_keyboardChoices, 0 )
		self.m_keyboard.SetSelection( 0 )
		self.m_keyboard.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26.Add( self.m_keyboard, 0, wx.ALL, 2 )

		m_speakChoices = [ u"No speech", u"Say Key", u"Say MAME", u"Say Pinball" ]
		self.m_speak = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 90,18 ), m_speakChoices, 0 )
		self.m_speak.SetSelection( 0 )
		self.m_speak.SetFont( wx.Font( 6, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26.Add( self.m_speak, 0, wx.ALL, 2 )

		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Last Key:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_last_key = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 95,18 ), wx.TE_READONLY )
		self.m_last_key.SetMaxLength( 0 )
		self.m_last_key.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_last_key.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )

		bSizer26.Add( self.m_last_key, 1, wx.ALL, 3 )

		self.m_about = wx.Button( self.m_panel1, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_about.SetFont( wx.Font( 7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_about.SetToolTip( u"Show the keyboard activity log" )
		self.m_about.SetMinSize( wx.Size( 55,20 ) )

		bSizer26.Add( self.m_about, 0, wx.ALL, 2 )


		bSizer23.Add( bSizer26, 0, wx.EXPAND, 0 )


		bSizer24.Add( bSizer23, 1, wx.ALL|wx.EXPAND, 0 )


		bSizer21.Add( bSizer24, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer21 )
		self.m_panel1.Layout()
		bSizer21.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.Bind( wx.EVT_SIZE, self.onUI )
		self.Bind( wx.EVT_UPDATE_UI, self.onUI )
		self.m_escape.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f1.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f2.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f3.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f4.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f5.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f6.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f7.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f8.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f9.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f10.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f11.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f12.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_print.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_scroll.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_break.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_KADE1.Bind( wx.EVT_BUTTON, self.onKADE )
		self.m_squiggle.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_1.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_2.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_3.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_4.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_5.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_6.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_7.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_8.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_9.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_0.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_minus.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_plus.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_backspace.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_insert.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_home.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_page_up.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_numlock.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num_slash.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num_asterix.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num_minus.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_tab.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_q.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_w.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_e.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_r.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_t.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_y.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_u.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_i.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_o.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_p.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_left_brace.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_right_brace.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_caps_lock.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_a.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_s.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_d.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_f.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_g.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_h.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_j.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_k.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_l.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_colon.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_at.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_tilde.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_enter.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_delete.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_end.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_page_down.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num7.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num8.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num9.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num4.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num5.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num6.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num_plus.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_left_shift.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_backslash.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_z.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_x.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_c.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_v.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_b.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_n.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_m.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_comma.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_period.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_question.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_right_shift.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_left_ctrl.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_left_windows.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_left_alt.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_space.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_right_alt.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_right_windows.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_menu.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_right_ctrl.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_up.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num1.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num2.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num3.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_left.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_down.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_right.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num0.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num_period.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_num_enter.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_escape.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f1.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f2.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f3.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f4.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f5.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f6.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f7.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f8.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f9.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f10.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f11.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f12.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_print.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_scroll.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_break.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_KADE2.Bind( wx.EVT_BUTTON, self.onKADE )
		self.mus_squiggle.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_1.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_2.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_3.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_4.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_5.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_6.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_7.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_8.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_9.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_0.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_minus.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_plus.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_backspace.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_insert.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_home.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_page_up.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_numlock.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num_slash.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num_asterix.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num_minus.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_tab.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_q.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_w.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_e.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_r.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_t.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_y.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_u.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_i.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_o.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_p.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_left_brace.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_right_brace.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_backslash.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_caps_lock.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_a.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_s.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_d.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_f.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_g.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_h.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_j.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_k.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_l.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_colon.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_at.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_enter.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_delete.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_end.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_page_down.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num7.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num8.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num9.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num4.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num5.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num6.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num_plus.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_left_shift.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_z.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_x.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_c.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_v.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_b.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_n.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_m.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_comma.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_period.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_question.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_right_shift.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_left_ctrl.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_left_windows.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_left_alt.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_space.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_right_alt.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_right_windows.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_menu.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_right_ctrl.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_up.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num1.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num2.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num3.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_left.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_down.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_right.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num0.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num_period.Bind( wx.EVT_BUTTON, self.onButton )
		self.mus_num_enter.Bind( wx.EVT_BUTTON, self.onButton )
		self.m_show_log.Bind( wx.EVT_BUTTON, self.onLog )
		self.m_clear_list.Bind( wx.EVT_BUTTON, self.onClear )
		self.m_show_up.Bind( wx.EVT_CHECKBOX, self.onGUIClick )
		self.m_keyboard.Bind( wx.EVT_CHOICE, self.onKeyboardLayout )
		self.m_speak.Bind( wx.EVT_CHOICE, self.onSpeakFunction )
		self.m_about.Bind( wx.EVT_BUTTON, self.onAbout )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onClose( self, event ):
		event.Skip()

	def onUI( self, event ):
		event.Skip()


	def onButton( self, event ):
		event.Skip()
















	def onKADE( self, event ):
		event.Skip()



































































































































































































	def onLog( self, event ):
		event.Skip()

	def onClear( self, event ):
		event.Skip()

	def onGUIClick( self, event ):
		event.Skip()

	def onKeyboardLayout( self, event ):
		event.Skip()

	def onSpeakFunction( self, event ):
		event.Skip()

	def onAbout( self, event ):
		event.Skip()


###########################################################################
## Class AboutBox
###########################################################################

class AboutBox ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About Keyboard Tester v0.2", pos = wx.DefaultPosition, size = wx.Size( 360,250 ), style = wx.CAPTION|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self.m_panel2, wx.ID_ANY, wx.Bitmap( u"resources/keyboard.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"A general purpose keyboard test utility\nby 10yard (a.k.a. Degenatrons).\n\nKADE software is open and is licensed under GNU GPL V3.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( 340 )

		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self.m_panel2, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		m_sdbSizer1.Realize();

		bSizer3.Add( m_sdbSizer1, 0, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		bSizer2.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.onOK )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onOK( self, event ):
		event.Skip()


