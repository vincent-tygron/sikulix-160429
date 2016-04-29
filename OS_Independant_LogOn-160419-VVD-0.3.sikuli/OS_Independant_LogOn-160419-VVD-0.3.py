import logging;reload(logging)
FORMAT="%(asctime)-8s%(message)s"
logging.basicConfig(format=FORMAT, filename="testlog.log", level=logging.DEBUG)

################################################
# Log on to engine running on Windows or Linux #
################################################

if Settings.isLinux() or Settings.isWindows():
    find("LoginPanel-UserName-160418-VVD-0.2.png")
    doubleClick()
    type(Key.BACKSPACE)
    type(Key.BACKSPACE)
    doubleClick()
    paste("qaautotest2@tygron.com")
    type(Key.TAB)
    paste("autotest2qa")
    click("LoginPanel-LoginButton-160418-VVD-0.1.png")

######################################
# Log on to engine running on MacOSX #
######################################
    
elif Settings.isMac():
    find(Pattern("OSX-LoginPanel-PreviousUserNameAlreadyPresent-160419-VVD-0.1.png").similar(0.60))
    doubleClick()
    type(Key.BACKSPACE)
    type(Key.BACKSPACE)
    doubleClick()
    paste("qaautotest2@tygron.com")
    type(Key.TAB)
    paste("autotest2qa")
    click("OSX-LoginPanel-LoginButton-160419-VVD-0.1.png")    

##############################
# Exit when unable to log on #
##############################

else:
    print "[error] Unable to log on!"
    logging.error("[error] Unable to log on!")
    exit(1)

##################################
# Check if log on is successfull #
##################################

if exists("MainMenu-SignOutButton-160419-VVD-0.1.png") or exists("OSX-MainMenu-SignOutButton-160419-VVD-0.1.png"):
    print"[success] Log on succesfull!"
    logging.info("[success] Log on succesfull!")

else:
    print"[error] Log on failed!"
    logging.error("[error] Log on failed!")
    exit(1)