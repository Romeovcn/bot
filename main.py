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

from srcs.set_filter import set_filter_etable_male
from srcs.set_filter import set_filter_etable_female
from srcs.set_filter import set_filter_enclos
from srcs.window import open_window
from srcs.window import close_window
from srcs.item import remove_items
from srcs.item import add_items

def check_exit_thread(): # check bot exit thread loop
    while STOP_THREAD.is_set() == False:
        if keyboard.is_pressed("0"):
            STOP_THREAD.set()
        time.sleep(0.01)
    print("exit thread stopped")

def do_female(first_cycle):
    return
    # -------- SERENITE POSITIVE --------
    # if add_items("POSITIVE"): return # PLACER CARESSEUR
    # if open_window(): return # OUVRIR ELEVAGE
    # if set_filter_etable_female("NEGATIVE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE SERENITE NEGATIVE
    # if set_filter_enclos("POSITIVE"): return # METTRE FILTRE ENCLOS POSITIVE
    # do_main_bot("POSITIVE") # MAIN BOT
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # -------- AMOUR --------
    # if add_items("AMOUR"): return: return # PLACER DRAGOFESSES
    # if open_window(): return # OUVRIR ELEVAGE
    # if set_filter_etable_female("AMOUR", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN AMOUR
    # if set_filter_enclos("AMOUR"): return # METTRE FILTRE ENCLOS AMOUR SUFFISANT
    # do_main_bot("AMOUR") # MAIN BOT
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # ----- SERENITE NEGATIVE -1200 -----
    # if add_items("NEGATIVE"): return: return # PLACER BAFFEURS
    # if open_window(): return # OUVRIR ELEVAGE
    # if set_filter_etable_female("POSITIVE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE SERENITE POSITIVE
    # if set_filter_enclos("NONE"): return # METTRE FILTRE ENCLOS SERENITE NEGATIVE
    # do_seren_female_bot() # BOT SERENITE FEMELLE
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # -------- ENDURANCE --------
    # if add_items("ENDURANCE"): return: return # PLACER FOUDROYEUR
    # if open_window(): return # OUVRIR ELEVAGE
    # if set_filter_etable_female("ENDURANCE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN ENDURANCE
    # if set_filter_enclos("ENDURANCE"): return # METTRE FILTRE ENCLOS ENDURANCE SUFFISANT
    # do_main_bot("ENDURANCE") # MAIN BOT
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # -------- (OPTION MATURITE): return --------
    # if add_items("MATURITE"): return: return # PLACER ABREUVOIR
    # if open_window(): return # OUVRIR ELEVAGE
    # if set_filter_etable_female("MATURITE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN DE MATURITE
    # do_maturity_bot() # BOT MATURITE
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # ------------ ENERGIE ------------
    # if add_items("ENERGIE"): return: return # PLACER MANGEOIRE
    # if open_window(): return # OUVRIR ELEVAGE
    # if set_filter_etable_female("ENERGIE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN D'ENERGIE
    # if set_filter_enclos("ENERGIE"): return # METTRE FILTRE ENCLOS ENERGIE AU MAXIMUM
    # do_main_bot("ENERGIE") # MAIN BOT
    # ----------- FIN FEMELLE -----------
    STOP_THREAD.set()

def do_male(first_cycle):
    # -------- SERENITE NEGATIVE --------
    # if add_items("NEGATIVE"): return: return # PLACER BAFFEUR
    # if open_window(): return # OUVRIR ELEVAGE
    # set_filter_etable_male("POSITIVE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE SERENITE NEGATIVE
    # if set_filter_enclos("NEGATIVE"): return # METTRE FILTRE ENCLOS NEGATIVE
    # do_main_bot("NEGATIVE") # MAIN BOT
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # -------- ENDURANCE --------
    # if add_items("ENDURANCE"): return: return # PLACER FOUDROYEUR
    # if open_window(): return # OUVRIR ELEVAGE
    # set_filter_etable_male("ENDURANCE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN ENDURANCE
    # if set_filter_enclos("ENDURANCE"): return # METTRE FILTRE ENCLOS ENDURANCE SUFFISANT
    # do_main_bot("ENDURANCE") # MAIN BOT
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # ----- SERENITE NEGATIVE +1200 -----
    # if add_items("POSITIVE"): return: return # PLACER CARESSEUR
    # if open_window(): return # OUVRIR ELEVAGE
    # set_filter_etable_male("NEGATIVE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE SERENITE POSITIVE
    # if set_filter_enclos("NONE"): return # METTRE FILTRE ENCLOS SERENITE NEGATIVE
    # do_seren_male_bot() # BOT SERENITE FEMELLE
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # -------- AMOUR --------
    # if add_items("AMOUR"): return: return # PLACER DRAGOFESSES
    # if open_window(): return # OUVRIR ELEVAGE
    # set_filter_etable_male("AMOUR", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN AMOUR
    # if set_filter_enclos("AMOUR"): return # METTRE FILTRE ENCLOS AMOUR SUFFISANT
    # do_main_bot("AMOUR") # MAIN BOT
    # if close_window(): return # FERMER ELEVAGE
    # if remove_items(): return # ENLEVER ITEMS
    # -------- (OPTION MATURITE): return --------
    # if add_items("MATURITE"): return: return # PLACER ABREUVOIR
    # if open_window(): return # OUVRIR ELEVAGE
    # set_filter_etable_male("MATURITE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN DE MATURITE
    # do_maturity_bot() # BOT MATURITE
    # if close_window(): return # FERMER ELEVAGE
    if remove_items(): return # ENLEVER ITEMS
    # ------------ ENERGIE ------------
    if add_items("ENERGIE"): return: return # PLACER MANGEOIRE
    if open_window(): return # OUVRIR ELEVAGE
    set_filter_etable_male("ENERGIE", first_cycle, True): return # METTRE FILTRE ETABLE FEMELLE BESOIN D'ENERGIE
    if set_filter_enclos("ENERGIE"): return # METTRE FILTRE ENCLOS ENERGIE AU MAXIMUM
    do_main_bot("ENERGIE") # MAIN BOT
    # ----------- FIN FEMELLE -----------
    STOP_THREAD.set()

def main_bot_thread(): # main bot thread loop
    first_cycle = True
    do_female(first_cycle)
    do_male(first_cycle)

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