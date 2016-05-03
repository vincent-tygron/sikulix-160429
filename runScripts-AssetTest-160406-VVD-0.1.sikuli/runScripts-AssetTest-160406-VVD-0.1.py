import logging;reload(logging)
FORMAT="%(asctime)-8s%(message)s"
logging.basicConfig(format=FORMAT, filename="testlog.log", level=logging.DEBUG)

logging.info(">>>>>>>>>>>>>>>>>>>> STARTING Asset test... <<<<<<<<<<<<<<<<<<<<")

runScript("C:\Users\Vincent\Documents\SikuliX\OriginalsCustomAssetTest-160404-VVD-0.2.sikuli")
runScript("C:\Users\Vincent\Documents\SikuliX\LoadSP-CustomAssetTest-160404-VVD-0.1.sikuli")
runScript("C:\Users\Vincent\Documents\SikuliX\ChangedCustomAssetTest-160404-VVD-0.1.sikuli")
runScript("C:\Users\Vincent\Documents\SikuliX\LoadSPSaveFile-CustomAssetTest-160404-VVD-0.1.sikuli")
runScript("C:\Users\Vincent\Documents\SikuliX\RemoveAssetTestProject-160406-VVD-0.1.sikuli")

logging.info("<<<<<<<<<<<<<<<<<<<< ENDING Asset test... >>>>>>>>>>>>>>>>>>>>>")