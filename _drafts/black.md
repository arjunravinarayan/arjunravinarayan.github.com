---
layout: post
title: "Taint tracking cash"
category: 
tags: []
---

Before the word "bitcoin" turns you off from this entire post, let me
emphasize that this isn't about bitcoin, but about the deep economic
implications of adding one small feature to cash. Bitcoin has that
property, and it's [so hot right
now](http://www.youtube.com/watch?v=CV_hDyfmEw4), so I'm shamelessly
riding that bandwagon. 

Over on Hacking Distributed, [Emin Gün
Sirer](http://www.cs.cornell.edu/people/egs/) has a fantastic blog
post on [Cash-Boycotts: How to Use Bitcoins for Social
Change](http://hackingdistributed.com/2013/11/21/bitcoin-cash-boycott/). You
really should read it in it's entirety. The post starts by discussing
countless failed consumer boycotts:

> ... boycotts can't work unless a significant fraction of the
> consumers are involved. Let's face it, demand is mostly inflexible
> -- when your kid is screaming for that Tickle-Me-Elmo, you'll buy
> it, even if it means that someone else's kid in Bengladesh is
> slightly more likely to die in a warehouse fire as a result. Even
> when BP opened a gaping hole in the earth's mantle that was gushing
> a thick brown liquid of death into the ocean, approximately nobody
> changed their driving habits. Consumers mostly do not care about
> social causes, as evidenced by the sad number of signatures on
> change.org for even the worthiest petitions. And consumption is a
> terminal activity that starts and ends at the point of sale. There
> is no leverage; the advertising engines are too good, too strong,
> and the consumer sheep are already going baaa louder than you can
> say 'hey let's do things differently.'

> What we need is a network effect, one by which a small group of
> cognoscenti can leverage their power and exert a force on an even
> larger populace to do the right thing.

It then discusses how bitcoin's are different from cash because each
bitcoin encodes an entire *transaction history* of where the bitcoin
has been. This makes for a novel kind of boycott: tainted money, which
allows you to taint a piece of currency forever after. It's not just
Koch products you boycott, but any dollar bill that ever went through
the Kochtopus:

> So, the Pultars had a crazy idea: why not, instead of boycotting a
> company's products, boycott their cash flow? For this, all we need
> is a currency that records where the money has been. The idea is
> that, if someone hands you a dollar bill that he got from the Koch
> brothers, you could say, with righteousness dripping from your
> voice, "your money's no good here."

I encourage you to read the entire article; it's a great blog post
about boycotts and the social processes around them, even if you don't
care about bitcoin. Unfortunately, Gün Sirer's bitcoin boycotts are
doomed to fail. To get to that point, I'm going to make a diversion to
talk about black money.

Black Money
----

Black money is the concept of "off the books" cash holdings, namely,
money that's tainted by past transactions in the [black
market](http://en.wikipedia.org/wiki/Black_market). Many countries
have varying sizes of black markets (there has been a movement to
normalize them as "underground economies", reflecting the fact that
they are entire economies, not just narrow markets). If you are from
the United States or Northern Europe, the local underground economy is
relatively small: picking up Mexican day laborers outside a Home Depot
and paying them in cash, or restaurant servers underreporting
tips. This is small change. But in places like the south of Italy or
in developing countries like India, states are weak and cannot track
all transactions or enforce tax collection. But even weak states can
be strong in certain sectors of the economy and tax officials would
start asking questions if money crops up without legitimate
sources. Thus we get the problem of [black
money](http://en.wikipedia.org/wiki/Indian_black_money): sometimes you
want to trade your ill gotten gains for stuff, but your money isn't
good for it. Wouldn't it be nice to clean that money up?

In India, there is a parallel off-the-books banking system called the
[Hundi](http://en.wikipedia.org/wiki/Hundi) system. It works much like
the [Hawala](http://en.wikipedia.org/wiki/Hawala) international shadow
banking system (and is even integrated with for cross-border
transactions) --- you go up to a trusted merchant and hand them a
suitcase of cash. The bills are counted, everyone drinks some chai,
and agrees upon an interest rate and duration. You rest easy because
the Hundi would *never* screw you. And if you want money sent to your
cousin who has fallen ill in Calcutta, he'll have it arranged. Hundi
merchants operate banks. And with banks come interest rates, wire
transfers, loans, everything.

But you *still* can't mix the two monies! Now you've got two bank
accounts, two balances, two interest rates, and two ledgers. Well,
that's what you get for dealing with the shady side of the
economy... Surely there must be a way...?

The first way is to *launder* black money into white. This takes the
form of masquerading as a legitimate business transaction, with a
little something on the side. I sell you something innocent (like a
car) for a larger than usual amount of money. I also tack on some
black money (to make up the difference). So I've given you black
money, but you've given me white. And you can also account it as white
money on your ledger. Technically there is still a paper trail (where
did you get such an expensive car to sell?) but this is where the weak
state comes in: the Indian equivalent of the IRS doesn't have the
resources to follow up such long trails.

Laundering money comes at a high cost: the buyer still has to pay
capital gains taxes on your "car sale", so that will be factored into
the price. Presumably you only resort to such tactics during a
liquidity crisis... Much easier to horde the black money and spend it
on groceries and taxis and slowly dilute it out. Besides, there's the
whole deal with the cars. Who the hell wants an extra car sitting on
their driveway?

The second easier way to get rid of black money is to *tumble* black
money with white. Tumbling requires executing a simultaneous
double-sided contract (one legal, one underground). We exchange white
assets and black assets. The trouble is... what 



One "white money" transaction that keeps the capital gains
low, and the remaining in black. The white money is regular money, but
the black money needs to be disposed off. There is an implicit lower
valuation on the black money, since it cannot be used for all purposes
(and indeed, in future transactions you will try and negotiate up the
percentage of the transaction that is done "in black" to get rid of
your excess black money holdings). There are few ways to launder black
money into white money, one of the principle ones being lottery
tickets with winning numbers. (Since the lottery winners would like to
avoid taxes and will take your black money, giving you a perfect
excuse to suddenly have

You would soon see the formation of separate currencies (clean cash
vs. tainted cash) with exchange rates between them (since there will
be supply/demand imbalances in doing cash swaps). Presumably a
separate currency valuation will develop for each form of taint:
Koch-taint, blood-diamond-taint, ATT taint, all-of-the-above-taint,
etc. The relative valuation of tainted money vs. clean money would
depend on the total purchasing power of the bloc trying to impose the
blockade (and the cost they pay to impose such a blockade would again
be reflected in that price differential). I'm sure there's a neat
closed form solution in here somewhere that draws from the
macroeconomics literature...

