# (keytest.py)
#
# Keyboard Input Tester by Jon Wilson (10yard)
# Copyright (c) 2023
#
# Originally developed for KADE projects in 2013.
# Jon Wilson    - jon123wilson@hotmail.com
# Bruno Freitas - bootsector@ig.com.br
# Kevin Mackett - kevin@sharpfork.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS per GNU GPL Section 7
# No trademark or publicity rights are granted. This license does NOT give you 
# any right, title or interest in the KADE brand. You may not distribute any 
# modification of this program using the KADE name or KADE logo or claim any 
# affiliation or association with KADE or the KADE development team.
#
# Any propagation or conveyance of this program must include this copyright 
# notice and these terms.
#
# You may not misrepresent the origins of this program; modified versions of the 
# program must be marked as such and not identified as the original program.
import os
import wx
import gui
import pyWinhook as pyHook
import maps
import subprocess
from win32process import CREATE_NO_WINDOW


class KeyTest(gui.keytest):
  def __init__(self, parent):
    gui.keytest.__init__(self, parent)

    # set application icon
    self.SetIcon(wx.Icon("resources/kade.ico", wx.BITMAP_TYPE_ICO))

    # load keymaps for the gui keyboard
    self.key_dict = maps.get_key_dictionary(self)
    self.func_map_list = maps.get_func_map()

    # maintain focus on a hidden gui field to prevent unwanted cursor movement
    self.setDummyFocus() 

    # register keyboard events
    self.hm = pyHook.HookManager()
    self.hm.KeyDown = self.OnKeyboardEvent
    self.hm.KeyUp = self.OnKeyboardEvent
    self.hm.HookKeyboard()

    # prepare the list control
    self.m_list.InsertColumn(0, 'Key Code')
    self.m_list.InsertColumn(1, 'ASCII Code')
    self.m_list.InsertColumn(2, 'Scan')
    self.m_list.InsertColumn(3, 'Ext')
    self.m_list.InsertColumn(4, 'Window in Focus')
    self.m_list.InsertColumn(5, 'Event')
    self.m_list.InsertColumn(6, 'MAME Function')
    self.m_list.InsertColumn(7, 'Pinball Function')
    self.m_list.SetColumnWidth(0, 90)
    self.m_list.SetColumnWidth(1, 78)    
    self.m_list.SetColumnWidth(2, 50)
    self.m_list.SetColumnWidth(3, 28)    
    self.m_list.SetColumnWidth(4, 150)
    self.m_list.SetColumnWidth(5, 70)
    self.m_list.SetColumnWidth(6, 138)    
    self.m_list.SetColumnWidth(7, 168)    

    # remember the last event.  We don't want to show duplicates in log
    self.last_event = None

    # use height of window to determine if activity log is being viewed
    self.height = self.Size[1]
    
    # set the default keyboard
    self.setKeyboard([False, True].index(os.path.exists("us_key")), True)

    # initialise the UI
    self.UI(initial=True)

    # initialise the speech engine
    self.process = None
    self.say()
    
  @staticmethod
  def setFontSize(field, size):
    font = field.GetFont()
    font.SetPointSize(size)
    field.SetFont(font)     
    
  def OnKeyboardEvent(self, event):
    gui_object = self.getGUIObject(event.KeyID, event.Extended)
    if gui_object:
      if "down" in event.MessageName:
        gui_object.SetBackgroundColour(wx.GREEN) 
      else:
        gui_object.SetBackgroundColour(wx.NullColour)

    if self.last_event != (event.KeyID, event.MessageName):
      if self.m_show_up.GetValue() or "down" in event.MessageName:
        try:
          # insert item into list.  catch exception to handle any odd info in the descriptives
          mame_function = self.getFunction("MAME", event.KeyID)
          pin_function = self.getFunction("PIN", event.KeyID)
          
          self.m_list.InsertItem(0, "%s (%s)" % (str(event.Key), str(event.KeyID)))
          self.m_list.SetItem(0, 1, "%s (%s)" % (chr(event.Ascii), str(event.Ascii)))
          self.m_list.SetItem(0, 2, str(event.ScanCode))
          self.m_list.SetItem(0, 3, str(event.Extended))
          self.m_list.SetItem(0, 4, event.WindowName)
          self.m_list.SetItem(0, 5, event.MessageName.title().replace("Sys ", ""))
          self.m_list.SetItem(0, 6, mame_function)
          self.m_list.SetItem(0, 7, pin_function)

          # update last key field
          self.m_last_key.SetValue("%s (%s)" % (str(event.Key), str(event.KeyID)))          

          # speak the key pressed
          word = ""
          speak_func = self.m_speak.GetSelection()
          if speak_func > 0:
            if speak_func == 1:
              word = str(event.Key)
            elif speak_func == 2:
              word = mame_function
            elif speak_func == 3:
              word = pin_function

            word = word.split("(")[0]
            word = word.replace("|", ", or").replace("/", ", or")  # multiple functions should speak an "OR".
            word = word.replace("Return", "Enter")        # to fix in the DB
            word = word.replace("Capital", "Caps Lock")   # to fix in the DB

            # Extend the player word
            word = word.replace("P1", "Player 1").replace("P2", "Player 2")
            word = word.replace("P3", "Player 3").replace("P4", "Player 4")

            self.say(word)
        except Exception:
          pass
                
    self.last_event = (event.KeyID, event.MessageName) 
    return True

  def say(self, word=""):
    try:
      # abruptly stop any other speech
      self.process.terminate()
    except Exception:
      pass
    try:
      # speak the given word
      self.process = subprocess.Popen("resources/saystatic.exe %s" % word, creationflags=CREATE_NO_WINDOW)
    except WindowsError:
      pass
    
  def getGUIObject(self, code, extended):
    obj = None
    for item in self.key_dict:
      if item[0] == code:
        try:
          obj = item[1+extended]
        except Exception:
          obj = item[1]
        break
    return obj

  def getFunction(self, system, code):
    function = ''
    for item in self.func_map_list:
      if item[0] == system and item[1] == code:
        function = item[2]
        
      # workaround a specific US pinball issue
      if self.m_keyboard.GetSelection() == 1 and item[0] == system+"_US" and item[1] == code:
        function = item[2]
        
    return function

  def setDummyFocus(self):
    self.m_dummy.SetFocus() 

  def setKeyboard(self, keyboard, initial=False):
    # Set the visual keyboard. If initial then set the default country
    if keyboard == 0:
      self.m_uk.Show()
      self.m_us.Hide()
      if not initial and os.path.exists("us_key"): 
        try:      
          os.rmdir("us_key")
        except Exception:
          pass
    else:
      self.m_us.Show()
      self.m_uk.Hide()
      if not initial and not os.path.exists("us_key"):
        try:
          os.mkdir("us_key")
        except Exception:
          pass

    if initial:
      self.m_keyboard.SetSelection(keyboard)
    self.key_dict = maps.get_key_dictionary(self, keyboard)
    self.m_panel1.Layout()
    self.setDummyFocus()           
    
  def clearGUI(self, clear_log=False):
    # clear all button status and optionally clear the log
    if clear_log:
      self.m_list.DeleteAllItems()      
    for obj in self.key_dict:
      obj[1].SetBackgroundColour(wx.NullColour)
    self.setDummyFocus() 

  def UI(self, initial=False):
    if initial or self.height != self.Size[1]:
      self.height = self.Size[1]
      if self.height < 360:
        self.m_show_up.Disable()
        self.m_clear_list.Disable()
        self.m_show_log.SetLabel("Show Activity Log")
        self.m_show_log.SetToolTip("Show the keyboard activity log")
      else:
        self.m_show_up.Enable()
        self.m_clear_list.Enable()
        self.m_show_log.SetLabel("Hide Activity Log")
        self.m_show_log.SetToolTip("Hide the keyboard activity log")
      self.Layout()

  def onLog(self, event):
    # adjust the window height to hide/show the activity log
    if self.Size[1] < 372:
      self.SetSize((800, 597))
    else:
      self.SetSize((800, 330))
    self.m_dummy.SetFocus() 

  def onUI(self, event):
    self.UI()

  def onButton(self, event):    
    self.setDummyFocus() 

  def onGUIClick(self, event):
    self.setDummyFocus() 
    
  def onClear(self, event):
    self.clearGUI(clear_log=True)
    
  def onKeyboardLayout(self, event):
    self.setKeyboard(self.m_keyboard.GetSelection())
    self.clearGUI()

  def onSpeakFunction(self, event):
    self.clearGUI()

  def onAbout(self, event):
    about = AboutBox(None)
    about.ShowModal()
    about.Destroy()
    
  def onClose(self, event):
    self.Destroy()


# ==========================================================================================
# About

class AboutBox(gui.AboutBox):
  def __init__(self, parent):
    gui.AboutBox.__init__(self, parent)
        
  def onOK(self, event):
    self.Close()
    self.Destroy()


# ==========================================================================================
# Main

def main():
  app = wx.App()
  KeyTest(None).Show()
  app.MainLoop()
  app.Destroy()


if __name__ == "__main__":
  main()
