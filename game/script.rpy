# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define H = Character("Heart", color = "#990033")

define De = Character("Dee", color = "#ff0000")

define Du = Character("Dum", color = "#ff0000")

define dendu = Character("Dee and Dum", color = "#ff0000")

define F = Character("Fish", color = "#fffffff")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    "You don’t know where you are but it hurts your eyes a lot and not just your eyes actually all your senses hurt. A lot!"
    "It feels like you had a sensory overload and its so bad you cant even get your eyes back open."

    dendu "HALT"

    De "Halt in the name-"
    Du "-Of the Heart Queen’s bodyguards!"

    "You freeze up instantly and look to see these so called bodyguards are…..actually really tiny."

    "Like 3 feet tall levels of tiny"


    De "Eeeewwww! what is that?"
    Du "I dunno they look like a fish."
    De "An ugly fish."

    "Fish uh….well you don’t think you look like one of those creepy lil’ things but hey what do you know?"

    De "Hey you-"
    Du "What is your name?"

    "Your name? Well dang you’re far too embarrassed to admit that you have no idea what it is anymore. You must’ve bumped your heading when you got here."

    "Well you cant let them see your obvious stupidity so you blurt out the first word you can think of!"

    "And that word is Fish…"

    "Your name is now Fish ???? And you have no idea what is going on"

    Du "SEE! I told you they were a fish!
    De "Fishes don’t have legs stupid!
    Du "I am not stupid you are!

    "The duo seems to have forgotten all about you favoring poking each other with their sticks ."

    "Now is your chance to slip out and avoid they’re tiny rage."

    "You begin to inch your way out of their field of vision when a voice stops you cold."

    H "Boys? Where are you two? Did you find the thing that came out the well."

    "Oh god, that sounds like an actual adult you break into a full sprint when on of the twins sticks their stick in front of your feet causing you to hit the ground while the other throws a net on top of you."

    De "Yes Ma’am"
    Du "We caught em!"

    "You see the bushes around you rustle and prepare for the worst."

    H "Oh thank god what is it-"

    H "Oh what did you do to the poor creature!? The poor dear looks scared witless!"

    "Like you children being scolded (which you guess they kinda are) they quickly remove the net and scramble in front of you and the lady."

    H "There we are now. Honestly you two! I told you to be nice to whatever it was, I bet you two started fighting too didn’t you?"

    "Whoever this is doesn’t seem to be their mother due to absolutely zero resemblance but she certainly commanded the same respect."

    De "We’re sorry"
    Du "Queen Heart we just"
    De "Wanted to have some fun!"

    "They pout like small children and definitely not like bodyguards of queen- WAIT IS THAT THE QUEEN?!"
    "You don’t realize you are gawking until you see her look up and giggle presumably at you."

    "She waves her the two twins away before sitting down in front of you."

    "Heart: So your name is Fish? An odd name then again I suppose mine is fair weirder."

    "Your not sure what she means by a weird name I mean it’s not like she’s name heart….right???"

    "Heart: In any case are you alright? You look like you got hurt. I hope it wasn’t the twins."

    "Your arm has been hurting since you woke up here. As have your other senses but you don’t want her to know that!"

    "For one you don’t want her to worry about you and you also don’t wanna look too weak in case she’s dangerous."

    "Then again she did witness you get taken down by two 3 foot tall kids. -_-"

menu:
    "Oh yeeeeeaaaaah I’m tooooootally fiiiiiiine!":
        jump heart.one.one
    "Tell the truth about your injuries":
        jump heart.one.two
    "Start making weird noises":
        jump heart.one.three

        label heart.one.one:
        "You plaster on a huge smile in hopes of fooling her but alas it doesn't seem to work as she casts you a mildly disapproving glare."
        H "Lying won’t do you any good. You’ve been squinting and clutching your arm the entire time you’ve been standing in front of me."
        "Wow she actually noticed that? Now you feel really bad for lying"
            jump choice.one.end


    label choice.one.end
    H "Well Sensory overload is usually common when an outsider comes down here to visit."

    H "Most of our citizens are accustomed to the energy surges that flow through everything we tend to forget it’s a hard thing to adjust to.""

    H "I can take care of that and your arm if you’d kindly follow me inside?"

    F "Inside? Inside where?"

    H "Inside my castle of course.""

    "She point upwards and you turn you gaze to see an enormou castle sprouting towards the sky.""

    "How on earth had you missed that earlier?!""

    "Heart grabs the arm that isn’t in pain and she drags you inside."

    "As soon as you hit the inside of the castle’s wire gates your find your drowning in the smell of chocolate and roses."

    "It overwhelms you for a good while and you have to shut your eyes and senses off and stumble blindly behind the Heart Queen."

    "You can feel yourself stumbling up a set of stairs and through a door."

    "When you reopen your eyes your in a sitting room with a plate of cookies labelled ‘eat me’ and a mug labelled ‘drink me’."

    "It seems incredible suspicious."

    H "Here have a seat while I get something for your arm. Feel free to eat the cookies of the coco it’ll help with your sensory problems."

    "Oh thats what they are!"

    "You are still a bit skeptical but Heart seems to notice this and takes a big out of one of the cookies before leaving."

    "Seems good enough for you!"

    "You take a huge chop out of one of the cookies and a huge drink from the mug."

    "Almost instantly you feel your headache stop and the overload of your senses calming down!"

    "Man this stuff is awesome."

    "While you keep shoving your face with cookies Heart comes back and grabs your hurt arm."

    H "Alright now this just goes on like this and….done!"

    "She slides what looks like a flexible cast over your arm that makes it not hurt as much when you move it."

    "You thank her though it sounds more like garbles since there’s still cookie in your mouth"

    H "You’re very welcome- mouth closed while you chew please."

    H "Now then seeing as you came through the well I can assume that you’re looking for a way home?""

    "You nod though you don't actually remember where home is or what home is but hey you wont tell her that."

    H "Well unfortunately you can't really leave her unless you get the Card Keys from each the kingdoms."

    H "Its a safety measure we installed to ensure that no one from here can leak into your world and cause the same panic that happened the second time Alice came through.

    "Judging from her grimace it must not have been pretty so you spare her the pain of asking about it."

    H "Now I’m more than capable of handing you mine but as for the others you may find it...difficult to reach them."

    H "You see we’re all a bit...tense at the moment."

    "You ask if it had anything to do with the explosion you saw a little ways off."

    H "seems to go pale at this and starts to mumble to herself."

    H "Goodness I didn’t think they were this close already."

    "She suddenly stands and flashes you a tense smile.

    H "Well…. we do want to get you home as soon as possible. I’m sure your family misses you greatly."

    H "Clover’s Kingdom is the closest to mine so that’s best where you start!"

    H "Oh but of course it won’t be safe to send you off alone. Clover’s Kingdom is uneasy at the moment."

    H "Well then ! I suppose I will have to just go with you!"

    "You feel rude for this but you can’t help but ask why she doesn’t just send her guards with you"

    H "O-Oh...ah, well...I love Dee and Dum but...they aren’t always the most, capable of the bunch."

    H "Besides its a fast trip and I haven’t seen my dear Clover in a while"

    "Heart starts pulling you out of the castle once again and has you follow her through the wood"

    H "Don’t worry this is a relatively safe path we’ll be there in no more than 15 minutes"

    "The forest is setting off all kinds of alarm bells in your head so you decide to hold part of Hearts dress and get through as fast as possible"

    "All in quiet for a time and you think you’ve made it to safety when a cluster of three beings surround both you and Heart."

    "They fiends have diamonds on their chest and point weapons towards Heart and you but saying nothing."

    "You feel panic flooding your veins as a split second decision is forces in front of you"
    <Choice two>


    # This ends the game.

    return
