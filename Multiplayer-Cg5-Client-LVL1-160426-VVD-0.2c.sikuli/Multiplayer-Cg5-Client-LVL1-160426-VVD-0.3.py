import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info] Play Level 1...")

################
# Municipality #
################
'''
if exists(""):
    print"[info] SSH selected as stakeholder" 
    logging.info("[info] SSH selected as stakeholder")
    find("")
    click()
    click()
    type(Key.SPACE)
    click("")
        
    # Building something

    click("")
    click("")
    dragDrop(, )
    click("1461669742268.png")
    wait("1461669772050.png", 5)
    click()
    wait("1461669817711.png")
    dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
    paste("4/2/2010")
    click("1461669963955.png")
    wait("1461671232017.png", FOREVER)
    click()
    wait("1461671253872.png")
    click("1461671279745.png")    
'''
##############
# Waterboard #
##############

if exists("Multiplayer-CG5-Waterboard-LVL1-IntroPanel-160426-VVD-0.1.png"):
    print"[info] Waterboard selected as stakeholder" 
    logging.info("[info] Waterboard selected as stakeholder")
    find("Multiplayer-CG5-WaterBoard-LVL1-IntroMainView-160426-VVD-0.1.png")
    click()
    click()
    type(Key.SPACE)
    wait("Multiplayer-CG5-Waterbaord-LVL1-MiniMap1-160426-VVD-0.2.png", 3)
    click()
        
    # Building something

    click("Multiplayer-CG5-Waterboard-LVL1-WaterActionMenuBtn-160426-VVD-0.1.png")
    exists("Multiplayer-CG5-Waterboard-LVL1-OpenWaterLocation-160426-VVD-0.1.png", 5)
    dragDrop(Pattern("1461676305234.png").targetOffset(589,-287), Pattern("1461676305234.png").targetOffset(-665,301))
    click("Multiplayer-CG5-Waterboard-LVL1-WaterActionMenuYesBtn-160426-VVD-0.1.png")
    wait("1461669772050.png", 10)
    click()
    wait("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfPanelImage-160426-VVD-0.1.png")
    dragDrop(Pattern("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfPanelDate-160426-VVD-0.1.png").targetOffset(67,0), Pattern("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfPanelDate-160426-VVD-0.1.png").targetOffset(-105,-3))
    paste("4/2/2010")
    click("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfirmBtn-160426-VVD-0.1.png")
    wait("1461671232017.png", FOREVER)
    click()
    wait("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ApprovalPanel-160426-VVD-0.1.png", 3)
    click(Pattern("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ApprovalPanel-160426-VVD-0.1.png").targetOffset(394,144))

#######
# SSH #
#######

elif exists(Pattern("1461669319306.png").similar(0.90)):
    print"[info] SSH selected as stakeholder" 
    logging.info("[info] SSH selected as stakeholder")
    find("1461669423619.png")
    click()
    click()
    type(Key.SPACE)
    click("1461669563841.png")
        
    # Building cheap student housing

    click("1461669579386.png")
    click("1461669604651.png")
    dragDrop(Pattern("1461670183163.png").targetOffset(-242,-46), Pattern("1461670183163.png").targetOffset(174,-5))
    click("1461669742268.png")
    wait("1461669772050.png", 5)
    click()
    wait("1461669817711.png")
    dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
    paste("4/2/2010")
    click("1461669963955.png")
    wait("1461671232017.png", FOREVER)
    click()
    wait("1461671253872.png")
    click("1461671279745.png")

###################
# UNI Real Estate #
###################

else:
#elif exists("Multiplayer-CG5-UNI-LVL1-IntroPanel-160426-VVD-0.1.png"):
    print"[info] Uni Real Estate selected as stakeholder" 
    logging.info("[info] Uni Real Estate selected as stakeholder")
    find("Multiplayer-CG5-UNI-LVL1-IntroMainViewl-160426-VVD-0.1.png")
    click()
    click()
    type(Key.SPACE)
    click("Multiplayer-CG5-UNI-LVL1-MiniMap1l-160426-VVD-0.1.png")
        
# Building educational building

    click("Multiplayer-CG5-UNI-LVL1-BuildActionMenuBtn-160426-VVD-0.1.png")
    click("Multiplayer-CG5-UNI-LVL1-EduLuxuryBtn-160426-VVD-0.1.png")
    dragDrop(Pattern("Multiplayer-CG5-UNI-LVL1-EduLuxeLocation-160426-VVD-0.1.png").targetOffset(-85,-90), Pattern("Multiplayer-CG5-UNI-LVL1-EduLuxeLocation-160426-VVD-0.1.png").targetOffset(67,78))
    click("1461669742268.png")
    wait("1461669772050.png", 5)
    click()
    wait("1461669817711.png")
    dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
    paste("4/2/2010")
    click("1461669963955.png")
    wait("1461671232017.png", FOREVER)
    click()
    wait("1461671253872.png")
    click("1461671279745.png")