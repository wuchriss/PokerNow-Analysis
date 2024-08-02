class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.hands_tracked = 0
        self.hands_vpiped = 0
        self.flops_pfr = 0 #numbers of hands to the flop where you are the pfr
        self.pfr = 0
        self.three_bet = 0
        self.possible_three_bet = 0
        self.four_bet = 0
        self.possible_four_bet = 0
        self.five_bet = 0
        self.possible_five_bet = 0
        self.c_bet = 0
        self.possible_c_bet = 0
        self.flop_check_raise = 0
        self.possible_flop_check_raise = 0
        self.flops = 0
        self.turns = 0
        self.rivers = 0
        self.pots_won = 0
        self.double_barrel = 0 #betting turn given that you are the flop aggressor
        self.possible_double_barrel = 0
        self.triple_barrel = 0
        self.possible_triple_barrel = 0

    def act_preflop(self, descriptor, num_bet, new_in_pot): #can fold, check, raise, call
        if new_in_pot:
            self.hands_tracked += 1
        if num_bet == 2:
            self.possible_three_bet += 1
        if num_bet == 3:
            self.possible_four_bet += 1
        if num_bet == 4:
            self.possible_five_bet += 1
        if descriptor == "fold" or descriptor == "check":
            return
        if descriptor == "raise":
            if num_bet == 2:
                self.three_bet += 1
            if num_bet == 3:
                self.four_bet += 1
            if num_bet == 4:
                self.five_bet += 1
            if new_in_pot:
                self.hands_vpiped += 1
                self.pfr += 1
        if descriptor == "call":
            if new_in_pot:
                self.hands_vpiped += 1
                

    def act_flop(self, descriptor, preflopRaiser, new, checked):
        if new:
            self.flops += 1
        if checked:
            self.possible_flop_check_raise += 1
        if self.id == preflopRaiser:
            if descriptor == "bet":
                self.c_bet += 1
                self.possible_c_bet += 1
            if descriptor == "check":
                self.possible_c_bet += 1
        if descriptor == "raise" and checked:
            self.flop_check_raise += 1

    def act_turn(self, descriptor, flopAggressor, new):
        if new:
            self.turns += 1
        if flopAggressor == self.id:
            if descriptor == "bet":
                self.double_barrel += 1
                self.possible_double_barrel += 1
            if descriptor == "check":
                self.possible_double_barrel += 1

    def act_river(self, descriptor, flopAggressor, turnAggressor, new):
        if new:
            self.rivers += 1
        if flopAggressor == self.id and turnAggressor == self.id:
            if descriptor == "bet":
                self.triple_barrel += 1
                self.possible_triple_barrel += 1
            if descriptor == "check":
                self.possible_triple_barrel += 1

    def calculate_percentage(self, numerator, denominator):
        return round((numerator / denominator * 100), 1) if denominator else 0

    def get_player_statistics_string(self):
        self.vpip_pct = self.calculate_percentage(self.hands_vpiped, self.hands_tracked)
        self.pfr_pct = self.calculate_percentage(self.pfr, self.hands_tracked)
        self.three_bet_pct = self.calculate_percentage(self.three_bet, self.possible_three_bet)
        self.four_bet_pct = self.calculate_percentage(self.four_bet, self.possible_four_bet)
        self.five_bet_pct = self.calculate_percentage(self.five_bet, self.possible_five_bet)
        self.flop_check_raise_pct = self.calculate_percentage(self.flop_check_raise, self.possible_flop_check_raise)
        self.c_bet_pct = self.calculate_percentage(self.c_bet, self.possible_c_bet)
        self.double_barrel_pct = self.calculate_percentage(self.double_barrel, self.possible_double_barrel)
        self.triple_barrel_pct = self.calculate_percentage(self.triple_barrel, self.possible_triple_barrel)
        self.flops_as_pfr_pct = self.calculate_percentage(self.flops_pfr, self.flops)

        return (
            f"Name: {self.name}\n"
            f"ID: {self.id}\n"
            f"Hands Played: {self.hands_tracked}\n"
            f"Pots Won: {self.pots_won}\n"
            f"\nPercentages:\n"
            f"VPIP: {self.vpip_pct:.2f}%\n"
            f"PFR: {self.pfr_pct:.2f}%\n"
            f"3-Bet: {self.three_bet_pct:.2f}%\n"
            f"4-Bet: {self.four_bet_pct:.2f}%\n"
            f"5-Bet: {self.five_bet_pct:.2f}%\n"
            f"C-Bet: {self.c_bet_pct:.2f}%\n"
            f"Flops as PFR: {self.flops_as_pfr_pct:.2f}%\n"
            f"Flop Check-Raise: {self.flop_check_raise_pct:.2f}%\n"
            f"Double Barrel: {self.double_barrel_pct:.2f}%\n"
            f"Triple Barrel: {self.triple_barrel_pct:.2f}%\n"
        )
    
    def get_player_stats(self):
        self.get_player_statistics_string()
        return {
            "Name": self.name,
            "Hands Played": self.hands_tracked,
            "Pots Won": self.pots_won,
            "VPIP (%)": self.vpip_pct,
            "PFR (%)": self.pfr_pct,
            "3-Bet (%)": self.three_bet_pct,
            "4-Bet (%)": self.four_bet_pct,
            "5-Bet (%)": self.five_bet_pct,
            "C-Bet (%)": self.c_bet_pct,
            "Flops as PFR (%)": self.flops_as_pfr_pct,
            "Flop Check-Raise (%)": self.flop_check_raise_pct,
            "Double Barrel (%)": self.double_barrel_pct,
            "Triple Barrel (%)": self.triple_barrel_pct
        }

    def get_player_attributes(self):
        return (
            f"Name: {self.name}\n"
            f"ID: {self.id}\n"
            f"Hands Tracked: {self.hands_tracked}\n"
            f"Hands VPIPed: {self.hands_vpiped}\n"
            f"Flops as PFR: {self.flops_pfr}\n"
            f"PFR: {self.pfr}\n"
            f"3-Bet: {self.three_bet}\n"
            f"4-Bet: {self.four_bet}\n"
            f"5-Bet: {self.five_bet}\n"
            f"C-Bet: {self.c_bet}\n"
            f"Flop Check-Raise: {self.flop_check_raise}\n"
            f"Possible Flop Check-Raise: {self.possible_flop_check_raise}\n"
            f"Flops: {self.flops}\n"
            f"Turns: {self.turns}\n"
            f"Rivers: {self.rivers}\n"
            f"Pots Won: {self.pots_won}\n"
            f"Double Barrel: {self.double_barrel}\n"
            f"Possible Double Barrel: {self.possible_double_barrel}\n"
            f"Triple Barrel: {self.triple_barrel}\n"
            f"Possible Triple Barrel: {self.possible_triple_barrel}\n"
        )
    
    def get_pfr_vpip(self):
        return (self.pfr_pct, self.vpip_pct)
        



