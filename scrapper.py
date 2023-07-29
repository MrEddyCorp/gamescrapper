
import os 
from platforms import platforms as ptf
from engines import engines as eg



def getData( engine , platform , roms_path):

    for root, dirs,files in os.walk(roms_path):
        for file in files:
            if(file.split('.')[-1:][0] in platform['formats'] ):
                #clean file
                file = file.split('(')[0]
                data = engine["source"].scrap(file,platform)




r_path = "\\\\NASLOCAL\\U6000v2\\Juegos\\Rooms\\Nintendo 64\\n64"
getData(eg.thegamedb,ptf.N64,r_path)