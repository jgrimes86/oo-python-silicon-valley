from .funding_round import FundingRound

class VentureCapitalist:

    all = []

    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @classmethod
    def tres_commas_club(cls):
        return [vc for vc in cls.all if vc.total_worth > 1000000000]

    def offer_contract(self, startup, funding_round, investment):
        FundingRound(startup, self, funding_round, investment)
    
    def funding_rounds(self):
        return [round for round in FundingRound.all if round.venture_capitalist == self]
    
    def portfolio(self):
        startups = []
        for round in self.funding_rounds():
            if round.startup not in startups:
                startups.append(round.startup)
        return startups

    def biggest_investment(self):
        sorted_rounds = sorted(self.funding_rounds(), key=lambda round: round.investment, reverse=True)
        return sorted_rounds[0].investment

    def invested(self, domain):
        total_in_domain = 0
        for round in self.funding_rounds():
            if round.startup.domain == domain:
                total_in_domain += round.investment
        return total_in_domain