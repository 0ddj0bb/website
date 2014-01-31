title: Wireless CTF @Shmoocon 2014!
date: 2014-01-14
author: FrankTheTank
tags: shmoocon, conferences

This January I had the pleasure of attending the 10th annual [Shmoocon][shmoocon] in Washington D.C. I was pretty excited about a new event they started this year, the wireless CTF. I did some preparation, including loading up Kali on an old Dell D600 laptop because I figured I could put it into PROMISC mode, among other things.

Also by way of preparation, here is a few folks from LDN helping me prepare for my big event on Friday morning. So going into this thing, I'm already something like 5 or 6 beers into it. Huzzah!

![LDN Breakfast][ldn_breakfast]

So I went into this event expecting to crack some WEP, get past that and into a wired LAN, and not much else really. I did have a 15Gig dictionary ready to go, on the off chance there was any WPA/WPA2 going on. When I got to theroom I found out that there was *only* WPA/WPA2, and the dictionary we were to use was provided by the organizers of the event. My other problem was I that I was totally unaware/unprepared for anything Software Defined Radio (SDR) related. Once I started setting up my gear, such as it was, I also realized that the old laptop I brought only did 2.4GHz, and at least part of the challenge was on 5GHz. I was able to identify about 5 or 6 different WPA/WPA2 networks in the 2.4GHz range that were in play for the CTF. It seemed like there was a ton of interference in the room, lots of signals cranked up and stomping on each other, and I know for a fact that the organizers were actively causing mischief and doing things like blocking all wireless pineapples (still not sure why that was).

There is a great SDR dongle going for about $20 these days, the RealTek RTL2832U based RTL-SDR. Had I known sooner,I would definitely had one of these with me. No biggie, I was able to purchase on from a table at the con. Although it wasn't made clear, I think the SDR was meant to be used in two ways in this sort of competition. First, as a spectrum analyzer (because they aren't just going to tell you where the signals are that you should be analyzing), and second as a device to capture and decode various and sundry transmissions. As far as the spectral analysis goes, I think [this guy right here][youtube1] has exactly the right idea. A beagle bone black and an LCD combined with this dongle, that's a really nice dedicated spectrum analyzer.

The SDR also needed some kind of software to tune it with. People were mostly using [the GQRX package][gqrx] with their SDR's, and it also seemed like most of the people in the room were fairly new to this as well. The guys running the event were coming around and dropping huge hints towards the end on how to tune, what freq's to tune to, and even breaking out their olr slide decks and giving ad-hoc training on SDR and GQRX right there on the spot.

Other than maybe DefCon, I ma not sure when/where we will see events of this type again, but I had a ton of fun, learned a lot, and am definitely looking forward to the next one.

[shmoocon]: http://shmoocon.org
[ldn_breakfast]: /images/ldn_breakfast.jpg
[youtube1]: https://www.youtube.com/watch?v=6YhrKMBrJ2g
[gqrx]: http://gqrx.dk/