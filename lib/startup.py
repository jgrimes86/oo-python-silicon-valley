from .funding_round import FundingRound
from .venture_capitalist import VentureCapitalist

class Startup:
   
   all = []

   def __init__(self, name, founder, domain):
      self.name = name
      self.founder = founder
      self.domain = domain
      
      Startup.all.append(self)
   
   pivot_called = True

   def pivot(self, new_name, new_domain):
      self.pivot_called = True
      self.name = new_name
      self.domain = new_domain

   def get_domain(self):
      return self._domain
   
   def set_domain(self, new_domain):
      if self.pivot_called == True:
         self._domain = new_domain
         self.pivot_called = False

   domain = property(get_domain, set_domain)

   @classmethod
   def find_by_founder(cls, founder):
      filtered_startups = [startup for startup in cls.all if startup.founder == founder]
      return filtered_startups
   
   @classmethod
   def domains(cls):
      return [startup.domain for startup in cls.all]

   def sign_contract(self, vc, funding_round, investment):
      FundingRound(self, vc, funding_round, investment)

   def startup_funding(self):
      return [round for round in FundingRound.all if round.startup == self]

   def num_funding_rounds(self):
      return len(self.startup_funding())

   def total_funds(self):
      total_investment = 0
      for round in self.startup_funding():
         total_investment += round.investment
      return total_investment

   def investors(self):
      list_of_investors = []
      for round in self.startup_funding():
         if round.venture_capitalist not in list_of_investors:
            list_of_investors.append(round.venture_capitalist)
      return list_of_investors
   
   def big_investors(self):
      list_of_investors = []
      for round in self.startup_funding():
         if (round.venture_capitalist not in list_of_investors) and (round.venture_capitalist in VentureCapitalist.tres_commas_club()):
            list_of_investors.append(round.venture_capitalist)
      return list_of_investors
