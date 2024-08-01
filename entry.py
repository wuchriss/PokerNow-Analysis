import re
#from https://github.com/foster-chen/PNParser
class Entry:

    def __init__(self, entry):
        self.raw = entry
        self.name = self._get_name(entry)
        self.descriptor = self._define_descriptor()
    
    
    @staticmethod
    def _get_name(entry: str, return_hash=True):
        full_names = re.findall(r'"([^"]*)"', entry)
        return [full_name.split(" @ ") for full_name in full_names] if return_hash else [[full_name.split(" @ ")[0]] for full_name in full_names]
        
    def _define_descriptor(self):
        descriptor_lookup = {
            "checks": "check",
            "calls": "call",
            "folds": "fold",
            "bets": "bet",
            "raises": "raise",
            "Uncalled": "uncalled",
            "Undealt cards": "rabbit",
            "shows a": "show",
            "ending hand": "end",
            "starting hand": "start",
            "Player stacks": "stack count",
            "collected": "collect",
            "Your hand": "own hand",
            "ante": "ANTE",
            "posts a small": "SB",
            "posts a big": "BB",
            "Flop": "flop",
            "Turn": "turn",
            "River": "river",
            "stack from": "add stack",
            "adding": "add stack",
            "approved the player": "join",
            "enqueued": "terminate",
        }
        for key, descriptor in descriptor_lookup.items():
            if key in self.raw:
                return descriptor
        return "admin"