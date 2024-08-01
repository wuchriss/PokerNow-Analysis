from player import Player
from session import Session
import pandas as pd

class PokerAnalysis:

    def __init__(self, file_path):
        self.file_path = file_path
        self.session = Session("Session_1")
        self.entries = pd.read_csv(self.file_path)["entry"].iloc[::-1].reset_index(drop=True)
        
    def run_analysis(self):
        self.session.analyze(self.entries)
        print(self.session.test_statistic())
        self.session.plot_pfr_vpip()
        
        