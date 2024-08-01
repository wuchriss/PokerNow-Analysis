import os
import pandas as pd
from pokeranalysis import PokerAnalysis
from scrape import Scrape

if __name__ == "__main__":
    #file_path = input("Enter the path to your poker log CSV file: ")
    #file_path = "/Users/wuuchriss/Desktop/poker_now_log.csv"
    #file_path = "/Users/wuuchriss/Desktop/ayaan_online.csv"
    #file_path = "/Users/wuuchriss/Desktop/homegame.csv"
    
    #game_link = input("Enter the link to your recent PokerNow game: ")
    

    #file_path = "/Users/wuuchriss/Desktop/onlinehg.csv"
    file_path = "/Users/wuuchriss/Desktop/plo_home.csv"
    #scrape = Scrape(game_link)
    #file_path = scrape.file_path
    if os.path.exists(file_path): #and (file_path.endswith('.csv') or file_path.endswith('.csv.crdownload')):
        print(f"File path is valid: {file_path}")
        # Proceed with loading and processing the file
        analysis = PokerAnalysis(file_path)
        analysis.run_analysis()
    else:
        print("Invalid file path. Please make sure the path is correct and points to a CSV file.")
    