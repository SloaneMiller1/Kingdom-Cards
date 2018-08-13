# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define H = Character("Heart", color = "#ff99c2")

define De = Character("Dee", color = "#ff0000")

define Du = Character("Dum", color = "#ff0000")

define dendu = Character("Dee and Dum", color = "#ff0000")

define F = Character("Fish", color = "#fffffff")

define C = Character("Clover", color = "#4bec13")

define Ht = Character("Hatter", color = "#336600")

define S = Character("Spade", color = "#6699cc")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sky

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    default stick = False

    "You don’t know where you are but it hurts your eyes a lot and not just your eyes actually all your senses hurt. A lot!"
    "It feels like you had a sensory overload and its so bad you cant even get your eyes back open."


    dendu "HALT"

    De "Halt in the name-"
    Du "-Of the Heart Queen’s bodyguards!"

    scene bg heartcastle
    show deeanddum neutral at left
    show fish confused at center
    "You sit up instantly and look to see these so called bodyguards are…..actually really tiny."

    "Like 3 feet tall levels of tiny"


    De "Eeeewwww! what is that?"
    Du "I dunno they look like a fish."
    De "An ugly fish."

    "Fish uh….well you don’t think you look like one of those creepy lil’ things but hey what do you know?"

    De "Hey you-"
    Du "What is your name?"

    "Your name? Well dang you’re far too embarrassed to admit that you have no idea what it is anymore. You must’ve bumped your head when you got here."

    "Well you cant let them see your obvious stupidity so you blurt out the first word you can think of!"

    "And that word is Fish…"

    "Your name is now Fish ???? And you have no idea what is going on"

    show deeanddum fighting at left

    Du "SEE! I told you they were a fish!"
    De "Fishes don’t have legs stupid!"
    Du "I am not stupid you are!"

    "The duo seems to have forgotten all about you favoring poking each other with their sticks ."

    "Now is your chance to slip out and avoid they’re tiny rage."

    "You begin to inch your way out of their field of vision when a voice stops you cold."

    H "Boys? Where are you two? Did you find the thing that came out the well."

    "Oh god, that sounds like an actual adult you break into a full sprint when on of the twins sticks their stick in front of your feet causing you to hit the ground while the other throws a net on top of you."
    show fish net at center
    show deeanddum neutral at left
    De "Yes Ma’am"
    Du "We caught em!"

    "You see the bushes around you rustle and prepare for the worst."

    show heart worried at right

    H "Oh thank god what is it-"

    show heart shocked at right

    H "Oh what did you do to the poor creature!? The poor dear looks scared witless!"

    show fish cries at center
    show deeanddum scolded

    "Like you children being scolded (which you guess they kinda are) they quickly remove the net and scramble in front of you and the lady."

    show heart scolding at right

    H "There we are now. Honestly you two! I told you to be nice to whatever it was, I bet you two started fighting too didn’t you?"

    "Whoever this is doesn’t seem to be their mother due to absolutely zero resemblance but she certainly commanded the same respect."

    De "We’re sorry"
    Du "Queen Heart we just"
    De "Wanted to have some fun!"

    "They pout like small children and definitely not like bodyguards of queen- WAIT IS THAT THE QUEEN?!"

    "You don’t realize you are gawking until you see her look up and giggle presumably at you."

    "She waves her the two twins away before sitting down in front of you."
    hide deeanddum scolded

    show heart neutral at right

    "Heart: So your name is Fish? An odd name then again I suppose mine is fair weirder."

    "Your not sure what she means by a weird name I mean it’s not like she’s name heart….right???"

    show fish smiles at left

    show heart worried at right

    H "In any case are you alright? You look like you got hurt. I hope it wasn’t the twins."

    "Your arm has been hurting since you woke up here. As have your other senses but you don’t want her to know that!"

    "For one you don’t want her to worry about you and you also don’t wanna look too weak in case she’s dangerous."

    "Then again she did witness you get taken down by two 3 foot tall kids. -_-"
    show fish thinkie at left
    menu:

        "Oh yeeeeeaaaaah I’m tooooootally fiiiiiiine!":
            jump heartoneone
        "Tell the truth about your injuries":
            jump heartonetwo
        "Start making weird noises":
            jump heartonethree

label heartoneone:
    show fish lies at left
    "You plaster on a huge smile in hopes of fooling her but alas it doesn't seem to work as she casts you a mildly disapproving glare."

    show heart scolding at right

    H "Lying won’t do you any good. You’ve been squinting and clutching your arm the entire time you’ve been standing in front of me."
    show fish cries at left
    "Wow she actually noticed that? Now you feel really bad for lying"
    jump heartoneend

label heartonetwo:
    "You spill about all your injuries including the odd way you were reacting to the world around you."
    show fish cries at left
    show heart coverface at right

    "Heart seems to nod a few times before pulling you into a gentle embrace"

    H "You poor dear Dee and Dum must’ve not made it any better. I have to give them a talking to for how they handle other people."

    "Huh? she actually seems really nice for a stranger you literally just met."

    "After a minute though she lets the hug go."
    jump heartoneend

label heartonethree:
    "You panic and start making random noises similar to an angry dying cat."
    show fish confused at left
    show heart neutral at right
    "Surprisingly this doesn’t seems to phase Heart as she simply smiles and shakes her head."

    H "I’m gonna take that as a busted arm and sensory/information overload correct?"

    "Your taken back by how accurate she is in her assessment."
    jump heartoneend

label heartoneend:

    show heart thinking at right
    H "Well Sensory overload is usually common when an outsider comes down here to visit."

H "Most of our citizens are accustomed to the energy surges that flow through everything we tend to forget it’s a hard thing to adjust to."

H "I can take care of that and your arm if you’d kindly follow me inside?"
show fish confused at left
"Inside? Inside where?"

H "Inside my castle of course."

"She point upwards and you turn you gaze to see an enormous castle sprouting towards the sky."

"How had you missed that earlier?!"
show fish smiles at left
"Heart grabs the arm that isn’t in pain and she drags you inside."

scene bg thronebed
show fish confused at left
show heart thinking at right

"As soon as you hit the inside of the castle’s wire gates your find your drowning in the smell of chocolate and roses."

"It overwhelms you for a good while and you have to shut your eyes and senses off and stumble blindly behind the Heart Queen."

"You can feel yourself stumbling up a set of stairs and through a door."

"When you reopen your eyes your in a sitting room with a plate of cookies labelled ‘eat me’ and a mug labelled ‘drink me’."
"It seems incredible suspicious."

show heart neutral at right

H "Here have a seat while I get something for your arm. Feel free to eat the cookies of the coco it’ll help with your sensory problems."

"Oh thats what they are!"

"You are still a bit skeptical but Heart seems to notice this and takes a big out of one of the cookies before leaving."

hide heart neutral
show fish smiles at left
"Seems good enough for you!"
show fish nomnom at left
"You take a huge chop out of one of the cookies and a huge drink from the mug."

"Almost instantly you feel your headache stop and the overload of your senses calming down!"

"Man this stuff is awesome."

show heart thinking at right

"While you keep shoving your face with cookies Heart comes back and grabs your hurt arm."

H "Alright now this just goes on like this and….done!"
"She slides what looks like a flexible cast over your arm that makes it not hurt as much when you move it."
"You thank her though it sounds more like garbles since there’s still cookie in your mouth"

show heart scolding at right

H "You’re very welcome- mouth closed while you chew please."

show heart thinking at right
show fish cries at left
H "Now then seeing as you came through the well I can assume that you’re looking for a way home?"

"You nod though you don't actually remember where home is or what home is but hey you wont tell her that."

H "Well unfortunately you can't really leave her unless you get the Card Keys from each the kingdoms."

H "Its a safety measure we installed to ensure that no one from here can leak into your world and cause the same panic that happened the second time Alice came through."

"Judging from her grimace it must not have been pretty so you spare her the pain of asking about it."

show heart coverface at right

H "Now I’m more than capable of handing you mine but as for the others you may find it...difficult to reach them."

H "You see we’re all a bit...tense at the moment."

"You ask if it had anything to do with the explosion you saw a little ways off."

"Heart seems to go pale at this and starts to mumble to herself."

H "Goodness I didn’t think they were this close already."

show heart neutral at right

"She suddenly stands and flashes you a tense smile."

H "Well…. we do want to get you home as soon as possible. I’m sure your family misses you greatly."

H "Clover’s Kingdom is the closest to mine so that’s best where you start!"

show heart thinking at right

H "Oh but of course it won’t be safe to send you off alone. Clover’s Kingdom is uneasy at the moment."

show heart neutral at right

H "Well then ! I suppose I will have to just go with you!"
show fish confused at left
"You feel rude for this but you can’t help but ask why she doesn’t just send her guards with you"

show heart worried at right

H "O-Oh...ah, well...I love Dee and Dum but...they aren’t always the most, capable of the bunch."

H "Besides its a fast trip and I haven’t seen my dear Clover in a while"
show fish smiles at left
"Heart starts pulling you out of the castle once again and has you follow her through the wood"

scene bg forest at right
show fish cries at left
show heart neutral at right

H "Don’t worry this is a relatively safe path we’ll be there in no more than 15 minutes"

"The forest is setting off all kinds of alarm bells in your head so you decide to hold part of Hearts dress and get through as fast as possible"

"All in quiet for a time and you think you’ve made it to safety when a cluster of three beings surround both you and Heart."
show fish shock at left
show heart coverface at right

"The fiends have diamonds on their chest and point weapons towards Heart and you but saying nothing."

"You feel panic flooding your veins as a split second decision is forced in front of you"
show fish thinkie at left
menu:

    "Run the heffle fluff away":
        jump hearttwoone
    "Try to fight":
        jump hearttwotwo
    "hide behind heart":
        jump hearttwothree

label hearttwoone:

hide heart coverface
show fish cries at center
"Your flight or fight instincts kick in and you choice flight."
"You shoot away from Heart and the scary men and run as fast as you can away from them."
"Your not sure where you’re going or how long you run but you don’t stop until you are unable to  hear Heart’s voice crying out for you."
"Only then do you stop, take a good look at your surroundings and...Fluff where are  you right now?"
"Which way did you come from?"
jump gameover

label hearttwotwo:
$ stick = True
hide heart coverface
show fish fite at center
"Your flight or fight instincts kick in and you grab the nearest object."
"Which happens to be a stick."
"Oh well work with what you have."
"You shut your eyes and step in front of Heart and wave the stick wildly trying to hit one of the guys or scare them away."
show fish shock at left
"When you open your eyes again all three guys on the guard knocked unconscious"
"Wow you didn’t think you were that goo- "
show heart fighting at right
"Nope you turn to find Heart holding a bow a pointed towards the ground fully loaded"
"You take another glance at the guys under you and see they all actually have arrows struck through their hearts"
H "Its alright dearling. You were very brave."
show fish lies at left
"Oh well...yeah you gues you were!"
jump hearttwoend

label hearttwothree:
show fish cries at center
"Your flight or fight instinct kick in and you choose neither."
"Instead you choice to coward timidly behind Heart and screech."
show heart fighting at right
"Heart seems rather used to this and instead of cowering too like you expected she claps her hands and summons a bow."
"She points it towards one of the men before releasing an arrow of pink energy into his chest and it’s ricochets off trees until all three men are down"
H "Morons…"
show heart worried at right
show fish shock at center
H "Oh gosh are you alright that must have been so scary!"
"...you make the decisions to never piss off Heart...ever…"
jump hearttwoend

label hearttwoend:
show heart thinking at right
show fish lies at left
H "Come on let’s keep moving forward"

show fish confused at left

"You follow heart through the rest of the woods as she unsummons her bow by snapping it against her knee"

" ...scary"

show heart neutral at right

show fish lies at left

"You decide to distract from the looming fact that you just watched this woman…(teen?) beat up 4 guy single handedly in a poofy overkill skirt by inquiring about her weapon."

H "Oh yes all of the Rulers of Suite have a weapon and are able to summon."

"Rulers of Suite? You ask if she means Suites as in the faces on cards."

show heart worried at right

H "Well, unless yours are different than ours I believe so!"

"Huh so that’s why she’s named heart."

"You continue to ponder this for the short remainder of your trip until heart breaks you train of thought"

show fish smiles at left

show heart neutral at right

H "Well here we are! Welcome to the Clover kingdom!"

scene bg hearted

jump cloverstart

label gameover:

    scene bg gamover
    "   "
    label cloverstart:
    "You arrive and look up and..."
    "Honestly you're not even sure you left the forest."

    "This looks to be more of a clearing in the forest than a kingdom."

    "Although as you continue to look around it becomes a little clearer to you that this is a city of some sort."

    "You can see that many of the trees have been carved out into houses and many things similar to hanging bird nests also being used as homes."

    H "Watch where you walk now the people of Clover’s Kingdom tend to move incredibly fast under foot."

    "You again cling onto heart’s skirt as she gently guides you through the town where animals seem to be running back and forth."

    "She guides you towards clear through the town and between a walkway made of tall bushes."

    H "Clover lives inside the maze along with most of her citizens so it’ll take us a minute to reach her."

    "You can feel dread rising in your stomach. You suck at mazes."

    "You should really try to remember how heart got you in the maze in case you have to get out on your own."

    "Heart leads you through the maze."

    "She makes a left turn, then she goes forward then she makes two right turns and another left turn."

    "Alright you seem to be keeping a pretty good track of where you guy are headed."

    "Now if you could just shake off the feeling that you two are being follow that would be gre-"

    "You spot a pair of green eyes in the bush and start shaking and tugging on hearts skirt."

    H "What’s wrong Fish?"

    "You point towards the eyes only to find them gone."

    "And that is very scary, like on no longer being able to find a spider you saw 2 minutes ago scary!"

    "You begin to cling to heart’s arm a bit like a koala (are there koalas here?) while she attempts to remove you."

    H "Fish, for Jokers sakes what's wrong?!"

    "You continue pointing spastically towards the bushes that once held the glowing greens eyes trying to get her to see your worry until something else catches your attention."

    "Its...a sound? A faint sound but its slowly growing louder."

    "It almost sounds like-"

    C "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
    C "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
    C "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    "You turn towards the sound of the noise and see a blur of red and green tackle heart to the ground."

    "Rather than doing the sensible thing of crying or screaming heart merrily starts to laugh"

    H "Hello there Little Clo Clo. Must you do that everytime you see me? You’ll break me back one of these days"

    C "I know I know but...AAAA IT’S BEEN TOO LONG I MISSED YOU!!"

    "The green and red child puts Heart in a choke hold of a hug while heart once again seems unfazed as though its a normal thing for her."

    "This goes on for a while before Clover finally takes notice of you."

    C "Ooooh you brought a friend?! Are they one of Spade’s? They look like one of Spades with the weird eyes and lips and hair and-"

    H "Clover it’s not nice to insult someone! This is Fish they came through the Well and they need the keys to get back through it."

    C "Oooooooh...they’re an outsider. Weird they don’t look anything like Alice."

    H "Well perhaps outsiders look different depending on where they’re from just like here."

    "You really appreciate Heart’s constant defending of you."

    "Maybe she’ll travel with you through the rest of the kingdoms."

    "Then you’re sure to stay safe."

    C "Oh! Heart are you going to stay? I haven’t seen you in so long and I really wanna have another tea party."

    C "...preferably one that doesn’t end like last time.."

    H "I’m sorry Clover but I only came to leave Fish with you. I’ve already been gone an hour and my people aren't the most….self reliant."

    "Noooo!! there goes your chance of a worry free trip."

    C "Awww no fair!"

    "Clover starts stomping her feet and pouting and you begin to question if she’s really the ruler of an entire kingdom."

    "Heff she barely looks any older than twelve."

    H "Clover, that kind of behavior doesn’t get you anywhere with me you know that."

    "How Heart manages to remain so passive when faced with a child like Clover you’re not quite sure."

    C "....It works with Hatter."

    H "Then I’ll have to talk with him about that. In the meantime take care of Fish and please do try to reconcile with diamond."

    H "I don’t blame you for their choices but...at least try to reconcile."

    "Clover sees off put by this and he pout turns more into an expression of shame."

    "You think it’s best to not bring that up around her."

    "Heart pats you on the head as if you were a child before walking away."

    C "So you want the Clover key right?"

    "You nod enthusiastically and hold out your hands wanting to just take the key and leave."

    "Clover looks at your outstretched hands and laughs"

    C "Well I can’t give you the key right now! I’m not so young that I don’t understand the key rules!"

    "You lower your hands and tilt your head asking what the Key Rules are."

    C "Huh? You don’t know them? I thought for sure Heart would’ve explained them before putting you through the trials."

    "What trails?!"

    C "She didn’t make you do the trails?! Ugh that is so unfair how come she gets to bend the rules and I don’t?!"

    "Part of you wants to point out that it’s because she’s a kid but somehow you think that’ll offend her."

    "Besides you’re far more concerned with what the trials is."

    C "Well see we aren’t actually supposed to give the keys away for free."

    C "If we did then it would be too easy to get the keys and we’d have the same problems as before."

    C "So we have to put everyone who wants the keys through a trial of some sort to prove that you’ve earned them."

    "What?! Heart never put you through any trial!"

    C "Yeah I think Heart pitied you a lot."

    C "So more than likely she’ll make up an excuse about how she tested you with something really insufficient."

    "Oh...Well you are not sure how to feel about that. On one hand you’re thankful for her not making you fight but on the other hand the pity kinda stings."

    "No matter! You are perfectly capable of whatever trial a twelve year old can cook up."

    C "So traditionally I think the Kingdom Clover used to make people get safely through the maze."

    "…...except that…."

    C "But a maze would be kinda boring and you already came through it once with Heart."

    C "So I’m thinking…….."

    C "A BATTLE!!!!!!!!!!!!!!!!!!!!!!!"

    "………..what?"

    C "Yes a battle would be prefect!"

    C "It’ll be the perfect chance to practice if I have to battle against an enemy!"

    "So you are just her practice dummy?"

    "Why does that scare you so much?"

    "Still, if you have to fight her to get out of this crazy world and go home then so be it!"

    C "Oh come on I’ll take you down to the arena!"

    "Clover grabs your hand and drags you swiftly away through even more of the maze until she practically runs headfirst into an iron gate."

    C "Here it is!"

    "She pushes the gates open with a both hands in an over dramatic movement and you suddenly regret everything."

    "The arena is a large field of grass shaped like a giant four leafed clover with weapons littering the outer edges."

if stick:

    C "I would offer you a weapon but I think you're pretty good with that stick of yours so I’ll use a stick too!"

    C "That way it’s fair!"

    "You nod. That does sems fair and non lethal- DEAR GOD WHY DOES SHE HAVE A TREE BRANCH?!"

    "Clover had apparently thought that a fallen tree branch two times both of your sizes was the same as your little stick."

    "Before you get a chance to argue she smiles with way too much joy for a girl about to fight"

    C "Ready...set….go!"

    "She takes a wild swing at you and you dodge to the best of your ability somehow not managing to get hit"

    "She swings again this time throwing the branch at you as well"

    "That manages to hit you."

    "The branch knocks you bad but thankfully you scamper away from it easily"

    "Clutching your stick tighter you start to swing it wildly while screeching and running towards Clover."

    "And when you open your eyes again."

    "You haven’t landed a single hit on her…"

    "But she is sitting on the ground with tears in her eyes."
    jump stickend

else:
    "Clover drags you over to a stack of weapons and smiles at you way too innocently for someone who just dragged you to a sky high pile of weapons."

    C "Here feel free to pick a weapon!"

    "You feel your hands start to get all sweaty as you start shifting through the pile."

    "You’re not even sure what half these weapons are a lot of them look like they were made to used by giants."

    "Which honestly you wouldn't doubt at this point."

    "You reach the bottom of the pile before you find...a little dagger!"

    "This is perfect just your size and you know how to use it."

    "You are quick to snatch up the dagger and head towards the center of the arena where Clover is waiting."

    C "Alright are you ready?"

    "You nod and mimic a fighting stance."

    C "Alright Ready...Set….."

    "Oh wait it just occurred to you clover isn’t holding any sort of weapon."

    C "Go!"

    "Clover forms her hands into the symbol of a club before clapping them together similar to how heart summoned her bow. As she does this the light from the clap begins to form….oh god no!"

    "You feel yourself having a mini flashback to Heart explaining how every Suite Ruler has a unique Weapon."

    "And it appears that Clover’s….are bombs."

    "You barely get a chance to run before Clover is hurling a bomb straight at you."

    "You barely manage to dodge before she hurdles another and another and another."

    "You have no idea how you’re going to survive this. Clover doesn't seem like the type to kill you on purpose. Then again she does seem highly accident prone."

    "You dodge one final time before it seems like Clover ran out of bombs."

    "Taking the opportunity you run towards her with your dagger and start slashing wildly with your eyes closed"

    "When you open them again you haven't landed a single hit on her….and yet she's lying on the grass"

    jump stickend

label stickend:
    C "that was really scary…"

    "Oh god no she’s crying!"

    "You drop the stick and scamper over to her hugging her and patting her head gently."

    C "Im sorry!  I didn’t really wanna fight you but I thought you would treat me more seriously if the trial was more risky."

    "You try to find something to say to reconcile her but...really what can you say.  She’s a twelve year old queen  who more than likely isn’t ever taken seriously. You can sympathize with her need for respect."

    C "Here. Take the key you were at least brave enough to try and fight me even if we didn’t finish it."

    "You gratefully take the key from her and stand up pulling her up with you."

    C "Thank you….Hey do you wanna have a tea party?"

    "Your a bit taken back by the question and your face must’ve given away your confusion."

    C "Yeah I haven’t had one with anyone who isn’t already a part of the Clover Kingdom since well….you know."

    "Oh that's right you forgot that there was a war going on and that Clover was a leader during that war."

    C "So what do you say? Is that a yes?"


menu:
    "Sure why not?":
        "Clovers mood seems to shift incredible fast as she begins to jump up and down holding you hands."
        jump cloverchoiceoneend
    "I’m sorry I have to keep going":
        C "Oh...its ok I understand"

        "Oh god no she’s tearing up again!"

        "You quickly change your answer to an overwhelming yes which seems to put a smile back on her face."
        jump cloverchoiceoneend
    "Say literally nothing":
        C "Im gonna take your silence as a yes!"
        "Oh wow she makes the difficulty of making choices easy!"
        jump cloverchoiceoneend

label cloverchoiceoneend:
    C "Oh yay thank you thank you thank you!"

    "You nod along with her."

    C "Oh come on! I can introduce you to Hatter while I’m at it!"

    "Hatter? Man everyone here has such weird names. Then again yours in Fish so who are you to judge."

    "Clover grabs you by the arm and drags you out of the arena and once again through the annoying maze."

    "At this point your stop trying to keep track of how to get out and just prayer someone will help you when you wanna leave."

    C "I know the castle maze can get a little confusing but you can always scale the walls to get through!"

    "Oh….the whole maze is the castle? Well you suppose its safe from attacks."

    "Clover drags you along for a few more minutes while you roughly stumble around trying to keep up with her nimble feet."

    C "HERE WE ARE!"

    "She comes to an abrupt halt and you slam into her back though she doesn’t seems to flinch."

    "You stand outside the gates of yet another clearing with a low table and pillows on the ground."

    "The table is littered with foods you’ve never seen and at the end of the table in an odd man."

    Ht "Ah! Clover! I knew you’d be coming!"

    C "Hi Hatter! I brought a friend look!"

    "Clover squishes your cheeks together and you try to protest that your not a puppy dog."

    Ht "Hm...I see...what an odd little creature they would be right at home here I am sure!"

    "Why does everyone always think you look weird?"

    Ht "Well in any case sit! Have some tea! Its Licorice and Matcha you’ll love it!"

    "Huh, thats odd...then again you did see animals walking like people so what do you know."

    "You sit down beside Clover and take a sip of the tea...huh it actually isn’t too bad!"

    Ht "By the way my little lady. I thought you might want to know this before someone else tells you but-"

    C "Is it an update on the…..the war?"

    Ht "Yes it is in fact-"

    C "Then it can wait! After all war isn’t a nice thing to talk about when you have a friend over right? That’s what you tell me!"

    "It seems Clover really is avoiding this topic at all cost. Your insanely curious to figure out why but you also don’t want her to get angry at you."


    #2ND CHOICE CLOVER

    #1. Ask her to tell you more about the War

    #"You do your best to ask about war without sounding insensitive"

    #"You think you do a good job of it but the way she shrinks seems to tell you otherwise"

    #"You quickly attempt to take about your question but-"

    #C "No..it’s fine...You should at least know whats going on if you end up walking into one of the battle zones."

    #"She sets down her cup as does the Hatter."

    #C "Heart probably already told you that we have 4 kingdoms for each of the Card Suits."

    #C "Well one of those suits is Diamond and they are a few years older than me."

    #C ".....a while ago they asked if I would date them."

    #C "I didn't want to hurt their feelings so I said yes but I couldn’t do it for long and I broke it off after the second date."

    #C "They….They did not take it well."

    #C "They declared war on my kingdom and when Heart tried to step in they declared war on her and Spade too."

    #C "And know everyone and fighting and no one trusts me anymore to do anything...I guess it makes sense this is all my fault…."

    #"Oh, now it makes more sense why she wanted to be taken seriously."

    #"That doesn't seem very fair to you! It’s not Clover’s fault it’s not like she could make DIamond not declare a war!"

    #"And besides if the other kingdoms think anyone is immature and untrustworthy it should be Diamond and not Clover."

    #"Clover seems to relax a bit more at your affirmation thought you can tell it’s still eating at her.""

    #You decide to take a page from Heart’s book and hug her in hopes of it making her feel better.

    #She hugs you back and the hug only lasts a short time but she already looks to be in a better mood.

    #2. Change the topic to something happier

    #"You panic and quickly switch the topic to the first thing you see"

    #"Which happens to be the Mad Hatter so you ask him to tell you more about himself."

    #"Clover groans at slams her face into her hands at this but Hatter’s face lights up."

    #Ht "Ah well you see I was born on a lovely summer day during the year of the time when all the stars were aligned to the port side of the sky"

    #OH dear god what have you done?

    #You can not escape this

    #You can’t escape the long awkward and boring conversation.

    #You are forever trapped here along with Clover and she doesn’t look too happy about it.

    #GAMEOVER

    #3. Sip your tea

    #"You take the longest sip of  tea known to mankind."

    #"You sip until the cup is empty then you refill it and sip again."

    #"Wow this is a crazy long sip."

    #"But thankfully Hatter and Clover seem to be talking about something else so good for you for not making a choice!"

    #"They keep talking and ask you question from time to time and you do your best to keep your face full of food or tea to keep talking to a minimum."



    #END OF CHOICE
    #"Hatter coughs kind of awkwardly."

    #Ht "Well it’s getting awfully late and Im sure Fish will want to get home as soon as possible and from what I hear they have two more kingdoms to visit."

    #C "Unless they wanna stay for a little while?"

    #"You politely decline the offer using the excuse of wanting to get home as fast as possible."

    #C "seems a little put out by this but thank fully understanding."

    #C "Well in that case I guess I’ll escort you out that way you don't get lost!"

    #"Oh thank God! You did not want go in that maze alone!"

    #C "In fact it would probably be best if I take you all the way to the next kingdom!"

    #Ht "Your taking her to Spade? I thought you try to avoid her?"

    #"You watch Clover’s face drop a little."

    #C "Well...I mean...ok it’s not my fault she’s scary!!"

    #"Hatter doesn't laugh at Clover’s fear but rather nods in understanding."

    #Ht "That they are, Well it’s probably for the best you escort Fish to her. Lord knows what she’d do otherwise."

    #"Your suddenly feeling a lot less confident….."

#CHAPTER 2 END
