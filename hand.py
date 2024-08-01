from entry import Entry
from player import Player

class Hand:

    def __init__(self, entries: list[Entry], session):
        while entries[0].descriptor != "start":
            entries.pop(0)
        self.entries = entries
        self.session = session
        self.players_in_hand = set()
        self.stage = "preflop"
        self.preflopAggressor = None
        self.flopAggressor = None
        self.turnAggressor = None
        self.actions = set(["raise", "call", "check", "fold", "bet"])
        self.analyzeHand()

    def recap_hand(self):
        res = ""
        for entry in self.entries:
            res += entry.raw
            res += '\n'

        return res
    
    def analyzeHand(self):
        num_bet = 1
        checked_flop = set() #set of player_ids who check the flop
        won = set()
        for entry in self.entries:
            if entry.descriptor == "collect":
                for name, player_id in entry.name:
                    if player_id not in won:
                        self.session.get_player(player_id).pots_won += 1
                        won.add(player_id)
                

            if self.stage == "preflop":
                if entry.descriptor == "flop":
                    self.stage = "flop"
                    if self.preflopAggressor:
                        self.session.get_player(self.preflopAggressor).flops_pfr += 1
                    self.players_in_hand = set()
                    continue
                if entry.descriptor == "stack count":
                    for name, player_id in entry.name:
                        if player_id not in self.session.players:
                            self.session.add_player(player_id, Player(name, player_id))
                if entry.descriptor in self.actions:
                    for name, player_id in entry.name:
                        self.session.get_player(player_id).act_preflop(entry.descriptor, 
                                                                       num_bet + 1, 
                                                                       player_id not in self.players_in_hand)
                        self.players_in_hand.add(player_id)
                        if entry.descriptor == "raise":
                            self.preflopAggressor = player_id
                            num_bet += 1
            
            if self.stage == "flop":
                if entry.descriptor == "turn":
                    self.stage = "turn"
                    self.players_in_hand = set()
                    continue
                if entry.descriptor in self.actions:
                    for name, player_id in entry.name:
                        self.session.get_player(player_id).act_flop(entry.descriptor, 
                                                                    self.preflopAggressor, 
                                                                    player_id not in self.players_in_hand, 
                                                                    player_id in checked_flop)
                        self.players_in_hand.add(player_id)
                        if entry.descriptor == "check":
                            checked_flop.add(player_id)
                        if entry.descriptor == "bet" or entry.descriptor == "raise":
                            self.flopAggressor = player_id

            if self.stage == "turn":
                if entry.descriptor == "river":
                    self.stage = "river"
                    self.players_in_hand = set()
                    continue
                if entry.descriptor in self.actions:
                    for name, player_id in entry.name:
                        self.session.get_player(player_id).act_turn(entry.descriptor, 
                                                                    self.flopAggressor, 
                                                                    player_id not in self.players_in_hand)
                        self.players_in_hand.add(player_id)
                        if entry.descriptor == "bet" or entry.descriptor == "raise":
                            self.turnAggressor = player_id
            
            if self.stage == "river":
                if entry.descriptor in self.actions:
                    for name, player_id in entry.name:
                        self.session.get_player(player_id).act_river(entry.descriptor, 
                                                                     self.flopAggressor, 
                                                                     self.turnAggressor, 
                                                                     player_id not in self.players_in_hand)
                        self.players_in_hand.add(player_id)

        

            

            
    
