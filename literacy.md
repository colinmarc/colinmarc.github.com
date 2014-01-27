Microwave Literacy 
==================

<p class="date"><em>May 2012</em></p>

*(this is a quasi-rebuttal to Jeff Atwood's post
["Please Don't Learn to Code."](http://www.codinghorror.com/blog/2012/05/please-dont-learn-to-code.html). If you're bored of the topic, you might want to stop
reading. I'll try to be broader.)*

I know hundreds, maybe thousands of languages. I'm not talking about spoken
languages, or programming languages, although I'll talk about those in a bit.
I'm talking about languages of operation.

What does that mean? Well, I know how to talk to my phone. I know how to talk
to my microwave. And my TV. Individual apps on my phone have their own
languages (one of the problems that android has yet to solve), and I know each
of them.

There are common elements of these languages, to be sure; I know a button when
I see it, and a menu, and an 'x' in a circle usually means close or quit. Just
as there are common elements in Latin-based languages, there are common
elements to user interface design.

Imagine, for a second, a world where spoken languages were far less
standardized. Instead of being able to write and speak english everywhere in
the U.S., each state has its own language. Actually, every town and city has
its own language. As you travel around, each time you visit a new place, you
learn the local phrases and expressions you need.

That's where we are with the technology in our lives. While written language is pretty
solidified, the languages of operation are horribly fragmented and rapidly
evolving. The car I'm in right now has some dashboard interface that is
completely incomprehensible until you spend 30 minutes with it.  It's easier
than learning korean, but still difficult. 

And I don't think that's just a user interface problem. I think it's a
**literacy** problem. Devices and people don't share any common language.

There is one language that me, my TV, my microwave, and the dashboard in this
car all speak, in one form or another: code. Well, sort of. 

Let me back up a second. Let's say I want to pop some popcorn for a night of
sniffling over *The Notebook*. My microwave's interface is extremely low-level.
The information it really wants is "how long do I cook this for? How much power
do I use?". To give it that information, I press a bunch of digits - I mess that
part up pretty often. I'm converting the information into mechanical symbols,
and then entering those symbols physically, and then the microwave is
converting that information back into the concepts it understands.

You probably see where I'm going with this. Of course, it wouldn't really be
practical to type in the ip address of my microwave into my phone, and then
type this:

	{ 'time': 200, 'power': 3 }

and then hit send. But effectively, that would allow a separation of concerns.
Now there are two parts to the process of popping popcorn. The microwave speaks
exactly the concepts it needs to, and I can communicate those concepts however
I want: hand-written JSON, a web/mobile app (microwave.ly?), brain-reading
alien slugs that connect to wifi, whatever. To a programmer, the benefits of
this are obvious.

(This doesn't just apply to devices, of course. People have been writing web
apps services with APIs and reaping the benefits for years.)

What would convice Mr. and Mrs. Microwave to make that microwave? It's simple -
everyone needs to learn to code.

If everyone understood programming, at least a little, manufacturers would feel
safe exposing an API and creating simpler devices. I think, given the choice,
they'd rather not have to worry about crafting a terrible a user interface.
You would see more devices being networked and hackable, and that's a really
good thing for everyone.

And you will! This isn't meant to be a call to action. We surround ourselves
with devices and services, so I think that we'll naturally develop a language
to speak with them. That said, knowing how to program puts you ahead of the
curve. So please, learn to code!

