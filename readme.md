# **Keyboard Input Test Utility** #
by 10yard (a.k.a. Degenatrons)


A general purpose keyboard test utility which will echo pressed keys to a virtual on-screen
keyboard.  Currently the utility has UK and US visual keyboards but would support many
different types of keyboard input - including encoders,  such as the KADE encoder.

The keyboard will stay on top of your other sessions and will continue to record keyboard 
input when it is not in focus.

There is a detailed view of activity available by clicking on the "Show Activity Log" 
button.  All inputs are displayed in a list and extensive information about keys is
reported including key code, ASCII code and scan code values. 
To assist those that are setting up encoders for use with MAME and Pinball,  I have
included the default function name that is assigned to the key press.


![Screenshot](https://github.com/10yard/keyboardtester/blob/main/screenshot.png)


## DOWNLOADS

The latest release is available to download from below.

| Download Link                                                                                                                    | Operating System                          |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------|
| [keyboard_tester_v0_2_win64.zip](https://github.com/10yard/keyboardtester/releases/download/v0.2/keyboard_tester_v0_2_win64.zip) | Windows 64 bit (x64) systems: 10, 11      |
| [keyboard_tester_v0_2_win32.zip](https://github.com/10yard/keyboardtester/releases/download/v0.2/keyboard_tester_v0_2_win32.zip) | Windows 32 bit (x86) systems: Vista, 7, 8 |


## VERSION HISTORY

v0.2.0.0 - 08/08/2023
  Update sources to modern Python version.  Switch to pyWinHook package.
  Fix icon bug.
  Windows 32 and 64 bit builds.

v0.1.0.8 - 07/04/2014
  MAME key mappings changed for P3 direction keys - to prevent conflict with P2.

v0.1.0.7 - 30/12/2013
  Show activity log by default when program starts.

v0.1.0.6 - 06/05/2013
  Removed the system menu and replaced with simple close icon.  The menu was being invoked by "Alt" and other key presses.

v0.1.0.5 - 05/05/2013
  Added speech option to speak the pressed keys or functions.  Useful for testing input without watching screen.
  Speech module provided by krolik.net - http://krolik.net/wsvn/wsvn/public/Say%2B%2B/
  Added an about box with donate button - for those using the software that would like to contribute.

v0.1.0.4 - 21/04/2013
  Improve UI for compatibility with Windows 8

v0.1.0.3 - 22/02/2013
  Fix minor difference between the two industry-standard keyboard layouts which was 
  causing confusion between the ' and ` keys and preventing US keyboard from displaying
  "Right Upper Flipper" function for pinball.

v0.1.0.2 - 29/01/2013
  Minor tweaks to US keyboard MAP

v0.1.0.1 - 28/01/2013
  Keyboard selection added (UK and US) and selected option is saved as default.
  Last key code is displayed in the keyboard only view for easy reference.
  Added readme.txt

v0.1.0.0 - 26/01/2013
  Initial release of the keyboard test utility.
