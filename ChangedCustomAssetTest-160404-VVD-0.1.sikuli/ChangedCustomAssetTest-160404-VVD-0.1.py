import logging;reload(logging)
FORMAT="%(asctime)-8s%(message)s"
logging.basicConfig(format=FORMAT, filename="testlog.log", level=logging.DEBUG)

logging.info("=====Uploading updated set of custom assets=====")

openApp("C:\Users\Vincent\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
wait("1458739770583.png",10)
dragDrop(Pattern("1459518307992.png").targetOffset(261,-121),Pattern("1459518307992.png").targetOffset(-268,-122))
type(Key.BACKSPACE)
paste(Pattern("1458739802503.png").targetOffset(-3,-122),"qaautotest1@tygron.com")
paste(Pattern("1458739802503.png").targetOffset(-4,-64),"autotest1qa")
click(Pattern("1458739802503.png").targetOffset(-6,47))
wait("1460631750673.png",15)
click()
paste("1459843581563.png", "Sikulix-asset test")
click("1459844726323.png")
if not exists("1459859232979.png", 30):
    print"[error] Project not loaded!"
    logging.error("[erroProject not loaded!")
    exit(1)

click("1460467075162.png")
click("1459769534717.png")
#click(Pattern("1459853297207.png").targetOffset(-52,-102))
click("1459851885184.png")
wait("1459859377876.png", 10)
click(Pattern("1459859377876.png").targetOffset(91,-453))
wait("1459859434827.png", 10)
click(Pattern("1459859377876.png").targetOffset(5,-88))
wait("1459859713570.png", 15)
click(Pattern("1459859713570.png").targetOffset(-179,206))
wait("1459769876588.png", 10)
click(Pattern("1459769876588.png").targetOffset(-16,-216))
paste("C:\Users\Vincent\Desktop\AssetTest-0331\Updated")
type(Key.ENTER)
click("1460461697120.png")
click(Pattern("1459859829026.png").targetOffset(247,200))
wait("1459859887424.png", 10)
click(Pattern("1459859887424.png").targetOffset(19,-182))
click(Pattern("1459859887424.png").targetOffset(98,252))
if not exists(Pattern("1459860203590.png").exact(), 5):
    print("[error] The custom stakeholder image was not added as expected!")
    logging.error("[error] The custom stakeholder image was not added as expected!")
else:
    print("[success] The custom stakeholder image was successfully added!")
    logging.info("[success] The custom stakeholder image was successfully added!")
click("1459771132666.png")
wait("1459863444950.png", 10)
click(Pattern("1459863444950.png").targetOffset(-1,-23))
wait("1459863495454.png", 5)
click("1459863495454.png")
wait("1459863584422.png", 5)
click(Pattern("1459863584422.png").targetOffset(-178,205))
wait("1460461985990.png", 10)
click("1460461985990.png")
click(Pattern("1459863644086.png").targetOffset(249,201))
wait("1459863727788.png")
click(Pattern("1459863727788.png").targetOffset(80,-184))
click(Pattern("1459868071078.png").targetOffset(97,251))
if not exists("1459863782276.png", 5):
    print("[error] The custom action menu image was not added as expected!")
    logging.error("[error] The custom action menu image was not added as expected!")
    exit(1)
else:
    print("[success] The custom action menu image was successfully added!")
    logging.info("[success] The custom action menu image was successfully added!")
click("1459772458832.png")
click("1459868458803.png")
click("1459863854588.png")
wait("1459863874844.png", 5)
click(Pattern("1459863874844.png").targetOffset(-169,201))
wait("1460462099101.png", 10)
click("1460462099101.png")
click(Pattern("1459863644086.png").targetOffset(249,201))
click(Pattern("1459864011852.png").targetOffset(51,-180))
click(Pattern("1459864011852.png").targetOffset(101,250))
if not exists("1459864064978.png", 5):
    print("[error] The custom measure image was not added as expected!")
    logging.error("[error] The custom measure image was not added as expected!")
    exit(1)
else:
    print("[success] The custom measure image was successfully added!")
    logging.info("[success] The custom measure image was successfully added!")
click("1459773712671.png")
click("1459773830726.png")
if not exists("1459864142938.png", 5):
    print("[error] The custom function value image was not added as expected!")
    logging.error("[error] The custom function value image was not added as expected!")
    exit(1)
else:
    print("[success] The custom function value image was successfully added!")
    logging.info("[success] The custom function value image was successfully added!")
click(Pattern("1459864199274.png").targetOffset(368,-291))
click("1460627692446.png")
#click("1459931854338.png")
#click("1459869103934.png")
#click("1459849139235-1.png")
click("1459846801644-1.png")
if not exists("1459864492439-1.png", 5):
    print"[error] Can't find updated custom function image!"
    logging.error("[error] Can't find updated custom function image!")
    exit(1)
click(Pattern("1459864591751-1.png").targetOffset(0,110))
wait("1459847819158-1.png", 5)
click("1460626426078.png")
click("1459847874509-1.png")
click(Pattern("1459847894261-1.png").targetOffset(86,-186))
click("1459854553718-1.png")
if not exists("1459864636870-1.png", 5):
    print"[error] Custom image for measure failed when executing measure!"
    logging.error("[error] Custom image for measure failed when executing measure!")
    exit(1)
click(Pattern("1459864636870-1.png").targetOffset(250,90))
click("1459847914820-1.png")
click("1460632084998.png")
click("1459775456044-1.png")
wait("1459864729742-1.png")
click("1459864729742-1.png")
#wait("1459864767709-1.png",10)
click("1459864767709-1.png")
wait("1459864792245-1.png", 5)
click(Pattern("1459864792245-1.png").targetOffset(-177,203))
wait("1460462345891.png", 5)
click("1460462345891.png")
click(Pattern("1459863644086-1.png").targetOffset(249,201))

for x in range(0, 10):
    if not exists(Pattern("1459864885686-1.png").targetOffset(54,-164), 1):
        print("[error] The image was not uploaded as expected, trying again!")
        logging.error("[error] The image was not uploaded as expected, trying again!")
        click("1460468051043.png")
        wait("1460462345891.png", 5)
        click("1460462345891.png")
        click(Pattern("1459863644086-1.png").targetOffset(249,201))
        #wait(1)
        break
        

if not exists(Pattern("1459864885686-1.png").targetOffset(54,-164)):
    print("[error] The image was still not uploaded as expected!")
    logging.error("[error] The image was still not uploaded as expected!")
    exit(1)
else:
    print("[success] The image was uploaded as expected!")
    logging.error("[success] The image was uploaded as expected!")
    click(Pattern("1459864885686-1.png").targetOffset(54,-164))
    click(Pattern("1459869173943.png").targetOffset(96,248))
if not exists(Pattern("1459864961076-1.png").similar(0.79), 5):
    print("[error] The custom overlay image was not added as expected!")
    logging.error("[error] The custom overlay image was not added as expected!")
    #exit(1)
else:
    print("[success] The custom overlay image was successfully added!")
    logging.info("[success] The custom overlay image was successfully added!")
click("1460472513836.png")

click("1459778258791-1.png")
click("1459778276391-1.png")
hover("1459869453876.png")
click(Pattern("1459865025876-1.png").targetOffset(-34,-1))
click("1459778406855-1.png")
click("1459865207842-1.png")
wait("1459769876588-1.png", 10)
click("1459778481462-1.png")
click(Pattern("1459778534814-1.png").targetOffset(250,202))
click(Pattern("1460463814520.png").targetOffset(-28,-2))
if not exists("1459865318545-1.png", 15):
    print("[error] The excel indicator file output is not as expected!")
    logging.error("[error] The excel indicator file output is not as expected!")
    #exit(1)
else:
    print("[success] The excel indicator file shows the correct output!")
    logging.info("[success] The excel indicator file shows the correct output!")

click(Pattern("1460456062280.png").similar(0.60).targetOffset(287,-224))

click("1460450493993.png")
sleep(1)
hover("1460467511343.png")
click(Pattern("1460467527431.png").targetOffset(0,8))
wait("1460450592130.png", 5)
click(Pattern("1460450592130.png").targetOffset(-172,206))
click("1460461811415.png")
click("1460450698288.png")
if not exists("1460468525832.png", 15):
    print("[error] The custom indicator image was not uploaded as expected!")
    logging.error("[error] The custom indicator image was not uploaded as expected!")
    exit(1)
else:
    print("[success] The custom indicator image was successfully uploaded!")
    logging.info("[success] The custom indicator image was successfully uploaded!")
click("1460468525832.png")
click("1460450830055.png")
click("1460725813780.png")
if not exists("1460468574080.png", 5):
    print("[error] The custom indicator image was not added as expected!")
    logging.error("[error] The custom indicator image was not added as expected!")
    #exit(1)
else:
    print("[success] The custom indicator image was successfully added!")
    logging.info("[success] The custom indicator image was successfully added!")
if not exists(Pattern("1460468599751.png").similar(0.96), 5):
    print("[error] The custom indicator image did not appear on the top bar as expected!")
    logging.error("[error] The custom indicator image did not appear on the top bar as expected!")
    #exit(1)
else:
    print("[success] The custom indicator image appeared on the top bar as expected!")
    logging.info("[success] The custom indicator imappeared on the top bar as expected!")

click("1459780227625-1.png")
click("1459780248393-1.png")
wait(Pattern("1458740876103-1.png").targetOffset(-41,51), 5)
click(Pattern("1458740876103-1.png").targetOffset(-41,51))
if not exists("1459780227625-1.png", 5):
    print("[success] The updated project was saved and closed")
    logging.info("[success] The updated project was saved and closed")
else:
    print("[error] The updated project did not exit as expected!")
    logging.info("[error] The updated project did not exit as expected!")
    exit(1)

logging.info("=====Finished uploading updated set of custom assets=====")

