from lib import *

# code here
# e.g.
s1 = Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
s2 = Startup( 'Goats R Us', 'Totes McGoats', 'www.gru.com')

vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
vc2 = VentureCapitalist( 'Count Chocula', 2000000000 )
vc3 = VentureCapitalist( 'Willy Wonka', 1500000000 )

fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )
fr2 = FundingRound( s1, vc2, 'Seed', 500075.00)
fr3 = FundingRound( s2, vc3, 'Series A', 45.50)
fr4 = FundingRound( s1, vc2, 'Series A', 1500000)
fr5 = FundingRound( s2, vc1, 'Seed', 49039)





# do not remove
import ipdb; ipdb.set_trace()
