import pyautogui
import keyboard
import random
import sys
import time
import threading

from config import STOP_THREAD
from srcs.bot_seren_female import do_seren_female_bot
from srcs.bot_seren_male import do_seren_male_bot
from srcs.main_bot import do_main_bot
from srcs.bot_maturity import do_maturity_bot

from srcs.set_filter import set_filter_etable_female
from srcs.set_filter import set_filter_enclos
from srcs.window import open_window

def check_exit_thread(): # check bot exit thread loop
    while STOP_THREAD.is_set() == False:
        if keyboard.is_pressed("0"):
            STOP_THREAD.set()
        time.sleep(0.01)
    print("exit thread stopped")

def main_bot_thread(): # main bot thread loop
    # -------- SERENITE POSITIVE --------
    # PLACER CHATOUILLEUR
    # OUVRIR ELEVAGE
    # set_filter_etable_female("NEGATIVE", True) # METTRE FILTRE ETABLE FEMELLE SERENITE NEGATIVE
    # set_filter_enclos("POSITIVE") # METTRE FILTRE ENCLOS POSITIVE
    # do_main_bot("POSITIVE") # MAIN BOT
    # FERMER ELEVAGE
    # ENLEVER ITEMS
    # -------- AMOUR --------
    # PLACER DRAGOFESSES
    # OUVRIR ELEVAGE
    # set_filter_etable_female("AMOUR", True) # METTRE FILTRE ETABLE FEMELLE BESOIN AMOUR
    # set_filter_enclos("AMOUR") # METTRE FILTRE ENCLOS AMOUR SUFFISANT
    # do_main_bot("AMOUR") # MAIN BOT
    # FERMER ELEVAGE
    # ENLEVER ITEMS
    # ----- SERENITE NEGATIVE -1200 -----
    # PLACER BAFFEURS
    # OUVRIR ELEVAGE
    # set_filter_etable_female("POSITIVE", True) # METTRE FILTRE ETABLE FEMELLE SERENITE POSITIVE
    # set_filter_enclos("NONE") # METTRE FILTRE ENCLOS SERENITE NEGATIVE
    # do_seren_female_bot() # BOT SERENITE FEMELLE
    # FERMER ELEVAGE
    # ENLEVER ITEMS
    # -------- SERENITE NEGATIVE --------
    # PLACER FOUDROYEUR
    # OUVRIR ELEVAGE
    # set_filter_etable_female("ENDURANCE", True) # METTRE FILTRE ETABLE FEMELLE BESOIN ENDURANCE
    # set_filter_enclos("ENDURANCE") # METTRE FILTRE ENCLOS ENDURANCE SUFFISANT
    # do_main_bot("ENDURANCE") # MAIN BOT
    # FERMER ELEVAGE
    # ENLEVER ITEMS
    # -------- (OPTION MATURITE) --------
    # PLACER ABREUVOIR
    # OUVRIR ELEVAGE
    # set_filter_etable_female("MATURITE", True) # METTRE FILTRE ETABLE FEMELLE BESOIN DE MATURITE
    # do_maturity_bot() # BOT MATURITE
    # FERMER ELEVAGE
    # ENLEVER ITEMS
    # -----------------------------------
    # PLACER MANGEOIRE
    # OUVRIR ELEVAGE
    set_filter_etable_female("ENERGIE", True) # METTRE FILTRE ETABLE FEMELLE BESOIN D'ENERGIE
    set_filter_enclos("ENERGIE") # METTRE FILTRE ENCLOS ENERGIE AU MAXIMUM
    do_main_bot("ENERGIE") # MAIN BOT
    # ----------- FIN FEMELLE -----------
    STOP_THREAD.set()

# order to up DD : FEMELLE -> POSITIVE -> AMOUR -> NEGATIVE -1100 -> ENDURANCE (-> MATURITE) -> ENERGIE 
#                  MALE -> NEGATIVE -> ENDURANCE -> POSITIVE +1100 -> AMOUR (-> MATURITE) -> ENERGIE

if __name__ == "__main__":
    time.sleep(2)
    thread_1 = threading.Thread(target=check_exit_thread)
    thread_2 = threading.Thread(target=main_bot_thread)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Les deux threads ont été arrêtés.")

# TO DO
# - PROBLEME AJOUT ITEM DANS LA BARRE D'ITEM SI DEUX ITEMS ONT LA MEME DURABILITÉ
# - PROBLEME FILTRE MATURITE
# - 