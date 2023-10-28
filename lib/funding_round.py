class FundingRound:

    all = []

    def __init__(self, startup, vc, funding_round, investment):
        self.startup = startup
        self.venture_capitalist = vc
        self.type = funding_round
        self.investment = investment
        FundingRound.all.append(self)
    

