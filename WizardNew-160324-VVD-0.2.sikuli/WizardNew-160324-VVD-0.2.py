import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

logging.info("[info] Create new project 'SikuliX-Editor', and save and exit...")

find("1460535966422.png")
click()
wait("1458822263448.png",10)
paste(Pattern("1458822263448.png").targetOffset(-24,-222),"SikuliX-Editor")
click(Pattern("1458822358415.png").targetOffset(-15,-53))
click("1458822423703.png")
wait("1458822546599.png",10)
click(Pattern("1458822563767.png").targetOffset(226,11))
wait("1458822622398.png",10)
paste(Pattern("1458822661143.png").targetOffset(-215,-157),"Arnhem")
type(Key.ENTER)
wait("1458822737716.png",30)
click(Pattern("1458822780840.png").targetOffset(411,303))
#wait("1458822970279.png",150)

waittime=1
for x in range(0, 300):
    if exists("1458829978984.png", x):
        print("[success] creating project in %d seconds was successful!" % (x*waittime))
        logging.info("[success] Creating project in %d seconds was successful!" % (x*waittime))        
    
if not exists("1458829978984.png", x):
    print("[error] creating project failed after %d seconds!" % (x*waittime))
    logging.error("[error] creating project failed after %d seconds!" % (x*waittime))
    exit(1)

sleep(2)
find("1458822999918.png")
click("1458822999918.png")
wait("1458823028071.png")
click(Pattern("1458823028071.png").targetOffset(-6,93))
wait("1458823126678.png",10)
click(Pattern("1458823126678.png").targetOffset(-37,47))


