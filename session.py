from player import Player
from entry import Entry
from hand import Hand
import matplotlib.pyplot as plt

class Session:
    def __init__(self, session_id):
        self.session_id = session_id
        self.hands = []
        self.players = {} #maps player_id to Player object

    def analyze(self, entries):
        index = 0
        entryList = []
        #iterates through all entries
        while index < len(entries):
            curr = Entry(entries[index])
            #adds all entries for a single hand to this
            #print(entries[index], curr.descriptor, index)
            entryList.append(curr)
            if curr.descriptor == "end":
                self.hands.append(Hand(entryList, self))
                entryList = []
            index += 1
            

    def test_statistic(self):
        for player in self.players.values():
            print(player.get_player_statistics())

    def add_player(self, player_id, player):
        self.players[player_id] = player

    def get_player(self, player_id):
        return self.players[player_id]
    
    def plot_pfr_vpip(self):
        pfrs = []
        vpips = []
        names = []
        for player in self.players.values():
            pfr, vpip = player.get_pfr_vpip()
            pfrs.append(pfr)
            vpips.append(vpip)
            names.append(player.name)

        plt.figure(figsize=(10, 6))
        plt.scatter(pfrs, vpips)

        for i, name in enumerate(names):
            plt.text(pfrs[i], vpips[i], name, fontsize=9, ha='right')
        plt.xlim(0)
        plt.ylim(0)
        plt.xlabel("%PFR (Passive / Aggressive)")
        plt.ylabel("%VPIP (Tight / Loose)")
        plt.title("PFR vs VPIP")
        plt.grid(True)
        plt.show()
                    