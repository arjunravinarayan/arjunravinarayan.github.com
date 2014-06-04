---
layout: page
title: "Can We Please Stop Discussing Valuations?"
---

Valuations are a red herring. But the valley is full of noise about
valuations. This is because it is an easy, reductive narrative to
push. Every company can be reduced to a single number: its total
market value. 

This is wrong because startups raise money using more complex
contracts than public corporations do. Calculating the market value of
a public corporation is simple: it is the total number of stock issued
by the company, multiplied by the share price. Taking the example of
IBM, its current share price at the time of writing is $184.37 per
share. There are slightly over 1.01 billion shares issued. So the
company is worth 186 billion as a whole. Startup valuation
calculations take that same theory and do a similar projection: it is
the total number of stock issued by a startup multiplied by the price
paid by the latest investors to buy some stock.

Now incidentally, Some commentators object to doing this math because
there isn't sufficient liquidity to justify projecting out, especially
when the money is raised on a small slice of equity. But that's not
quite right. You'd also get the same issues if you tried to dump all
the outstanding stock of a large liquid company like IBM. The price of
184.37 was calculated based on the last clearing trade for a single
share of IBM stock at closing today. If you happened to want to sell 1
billion of those shares, you'd probably find that the price would come
down, at least in the short or medium term. Thus, insofar as we are
using startup valuations to compare them in size to public corporation
market values, the lack of liquidity at large volumes is not the
issue. Public corporations have the exact same problem (although
startups would probably have that problem to larger extents given that
IBM is relatively more liquid). The real problem is that startups
raise money using complex contracts that are not the same as issuing
common stock.

Before we get to the startup contracts, there is another way that
public corporations raise money that we need to discuss: debt. When a
company like IBM wants money, it can either issue more stock, or issue
more debt. In theory, neither of those should have any effect on
price. If IBM has an iron-clad value of 186 billion that is crystal
clear and obvious to everyone, then the fact that IBM issues an extra
40 million shares at $184.37 each shouldn't move the needle at all:
the new combined company of 1.05 billion shares consists of the old
company (which we all agree is worth exactly 186 billion) plus an
extra $7.4 billion in the bank. Similarly, if the company raises $7.4
billion dollars of debt, it shouldn't move the needle on the stock
price. The company now owes $7.4 billion to bond-holders, but it has
$7.4 billion in the bank. Of course there's the small matter of
interest rates, and the fact that nobody really agrees on clear
valuations, but as long as we're handwaving, that's how it is: public
corporations raise money all the time, either through stock, or debt,
or distributed money by paying back the bonds, or share buy-backs, or
issuing dividends. In principle, these actions *do not change the
underlying value of the firm*.

Why are there two ways to give money to a firm, if they don't really
affect the valuation? It's because different investors have different
concerns. If you are worried about the downside and you want to
protect your investment, you want to lend the firm money in the form
of debt. Corporations want to raise money from both groups of
investors. Bondholders take solace in the fact that corporations have
to pay back debt or declare bankruptcy - those are their only two
options. But debt holders never get anything more. If the company is
wildly successful, they just get their initial principal back plus the
agreed upon interest. Debt holders are more concerned about downside
protection, but there's limited upside. Equity holders lose money
faster, but they also get the full upsides of rising value.

Startups are different. They seldom (if ever) issue debt. Primarily
because they're high risk anyway: the only thing in it is the
upside. And only seasoned investors get into the gig anyway: they're
after upside. So startups don't sell debt. But the option as presented
above (and as exercised by public corporations) is not binary. You can
make a contract "more debt-like", and thus pose less of a risk to an
investor. Yes startups do not issue bonds the way IBM does. But they
do issue boutique contracts to venture capitalists, with many
different terms. The best place to see this is in the helpful tool
["The Transparent Term
Sheet"](http://www.foundersfund.com/termsheet/), on the Founders Fund
website. There are a few knobs that investors can tweak besides
valuation: liquidation preferences, participating preferred stock, and
even some more scummy ones that some VCs use to dupe founders that I
won't talk about, like pre-money option pools. But the net effect is
that these knobs can be tweaked to make the resulting contract more
"debt-like" and less "equity-like".

It is here that the main conflict comes up: founders want a high
valuation, investors want a low one (so that they get more of the
company for the same dollar investment). So, in exchange for higher
valuations, VCs squeeze the contract to be more "debt-like", and thus
have a lower risk profile to the investor, so that they can justify
the high valuation. But this is not the same as issuing common stock
at a higher valuation! If a startup, let's call it UberForDucks, wants
to raise 10 million dollars, VCs might be willing to give them a
valuation of $100 million if everyone had common stock with no
additional provisions (Hypothetically that is. It stilql makes sense
for investors to demand things like a 1x liquidation preference for
incentive compatibility reasons). But UberForDucks are persistent, and
want more bread crumbs. The VCs are willing to go to $120 million, but
with a 2x liquidation preference. This means that effectively, if the
company sells for less than $20 million, the VCs get everything. If
the company sells for any amount higher, the VCs get the first $20
million. Depending on the contract, the VCs get to share the remainder
equally, or the VCs get a decreased share until it equalizes to the
equal ratio of 1:12. But effectively, this contract is more
"debt-like" at low valuations, and more "equity-like" at higher
valuations. It's a linear combination of debt and equity, which is
*not the same thing as issuing common stock*. So multiplying out the
valuation simply makes no sense, because you're taking the marginal
stock which is a qualitatively different partially debt-like contract,
and multiplying it over all the non-debt-like contracts (i.e. the
common stock).


    Error   : incompatible types
    found   : vc.TermSheet.BoutiqueContract
    required: gov.SEC.CommonStock
    in line :
       int marketcap = debtquity * pricepershare;

And so we get stupid TechCrunch headlines with really big eye popping
numbers.