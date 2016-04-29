import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

logging.info("[info] Log in with password only, as username is already filled in...")

find("1458821475701.png")
doubleClick("1458821475701.png")
wait("1458821531951.png",10)
paste(Pattern("1458821531951.png").targetOffset(-12,-66),"autotest1qa")
click(Pattern("1458821531951.png").targetOffset(-5,48))
#wait("1458821691231.png",10)
if not exists("1458821691231.png",10):
    print("[error] log in (PW only) failed!")
    logging.error("[error] log in (PW only) failed!")
    exit(1)
else:
    print"[success] log in (PW only) successful!"
    logging.info("[success] Log in (PW only) successful!")
