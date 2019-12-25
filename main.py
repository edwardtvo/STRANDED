

import sys
import time
import os

score=100
q = '\n'

def type(statement):
    for x in statement:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.069)

def delay(x):
    time.sleep(x)

def something_else():
    return "Sorry, you inputted something else. Please input only number 1 or 2"

def game_over(): #the game over function
    delay(1)
    print q
    game_over= "- - - - G A M E O V E R - - - - -"
    print game_over
    print q
    delay(3)
    dead="James\'s dead. You failed to rescue him from the island"
    print dead
    print q
    delay(5)
    scoree="Your score: 0"
    print scoree
    print q
    delay(3)
    try_again="Try again?"+q+q+"1. Yes" +q+"2. No" +q
    print try_again
    print q
    question=raw_input("?: ")
    if question =="1":
        python = sys.executable
        os.execl(python, python, * sys.argv)
    elif question=="2":
        type("Welp, it\'s sad to see you leave, but thank you for trying out my game! I hope you take another round again to try to save James from the stranded island, or if not then have a great day!"+q)
        delay(2)
        sys.exit()





#------------I N T R O-------------------------------




lol= q+q+"+ ------------------------ + " +q+q
print lol.center(50)

delay(2)

type("Welcome player. What's your name?: ")

namee = raw_input()
name=namee[0].upper()+namee[1:].lower() 
#to properly format the name input for future use

type("Well, %s, my name is Edward. And welcome to my game." % name + '\n')

time.sleep(2)

type("As you know, decisions have consequences." + "\n")
time.sleep(2)
type("And you'll be making a whole lot of decisions in this game." +'\n')
time.sleep(2)
type("So, choose them wisely." +'\n' +'\n')
time.sleep(2)
type("Welcome to S T R A N D E D ( ) " +'\n' +'\n')
time.sleep(4)

#------------- S T A R T G A M E------------------------

type('You woke up to your cell phone ringing. It\'s 3AM in the morning. It\'s your brother James. You picked up your phone to hear your brother crying:' + '\n' +'\n')

time.sleep(1)

type('James: Hey %s! Uhm.. I need help with something..' % name + '\n')

time.sleep(2)

type("%s: Yeah sure, but why are you crying? Tell me what happened" % name +'\n')
time.sleep(1)
type("James: I..I fell off my cruise ship and woke up on a beach..I was sitting on the rails.. and then a strong wind came by..and I fell and I..I woke up here" +'\n')
time.sleep(0.8)
game5="%s: James! Are you ok? Where are you?" % name + '\n'
type(game5)

time.sleep(2)

game6="James: I..I'm on a stranded island" +'\n' +'\n'
type(game6)
time.sleep(4)

print '----- Game instructions: -----' + '\n'
time.sleep(2)
print 'Decide how James\' fate unfold on the stranded island' +q
time.sleep(4)
print "When needed, pick a decision by inputting number 1 or 2 into the console"+q
time.sleep(5)
print "From an intial score of 100, for each choice you make, you will be granted or deducted points accordingly"+q
time.sleep(5)
print "Your choices will have consequences later on. Pick them wisely" +q
print "---------------------------"





#----------------------------D A Y 1--------------------------------





delay(4)
print q
type("- - - D A Y 1 - - -")
delay(2)
print q

game7="%s: Okay James. Calm down. Just calm down" % name + q
game8="James: Ok. Calming down" + q
game9="%s: Good. Now, do you have your pocket knife I told you to bring before your trip?" % name +q
game10="James: Wait a second I have to look for it in my pocket...Yes! Yes I have!" +q
game11="%s: Okay good. You will need it so don\'t. lose. the knife. Next, walk around to see if there\'s any coconut trees around" % name +q
game12="James: Walking around...Hey, I found one!" +q
game13="%s: Great!" % name +q
game14="James: But.. it is too high. I don\'t know if I can climb it"+q
game15="%s: Uhm...how about.." % name+q

type(game7);delay(1);type(game8);delay(1);type(game9);delay(1);type(game10);delay(1);type(game11);delay(1);type(game12);delay(1);type(game13);delay(1);type(game14);delay(1);type(game15);delay(2)



decisionA=q + "1. Just try to climb it. And chop some coconuts and leaves down" + q + "2. Can you walk past where you are for some distance? Maybe there\'s a lower tree for you to climb." +q

print decisionA


#Extra dialogue for A1
a1_1="James: Okay. Climbing the tree..." +q
a1_12="*thud*"+q
a1_2="%s: Hey what\'s wrong?" % name +q
a1_3="James: Ow! I fell. The rocks scratched my arms %s. I.. I don\'t think I want to fall here again" % name +q
a1_4="%s: Oh, there\'s rocks there? Ok don\'t climb there. Can you walk past where you are some distance? Maybe there\'s an easier tree to climb" % name +q


while True:
    A=raw_input("?:")
    if A not in ("1","2"):
        print something_else()
    else:
        break

print '\n'
if A=="1":
    score=score-2
    type(a1_1)
    delay(3)
    type(a1_12)
    delay(1)
    type(a1_2)
    delay(1)
    type(a1_3)
    delay(1)
    type(a1_4)
    delay(1)



game15="James: Okay, walking further...Found one! It\'s a low tree, I don\'t need to climb it!" +q
game16="%s: Great! Now cut some leaves and coconuts as well" % name +q
game17="James: Alright. Uhm.. how many coconuts should I take? They look heavy.."+q
game18="%s: Uhm.." % name +q

type(game15)
delay(1)
type(game16)
delay(1)
type(game17)
delay(1)
type(game18)
delay(2)

decisionB=q+"1. Take 4 coconuts" + q + '2. Take 6 coconuts' +q+q

print decisionB

while True:
    B=raw_input("?:")
    if B not in ("1","2"):
        print something_else()
    else:
        break

if B=="1":
    score=score-2

game19=q+"James: Alrighty" +q
game20="%s: You need the coconuts for both food and water. The coconuts\' water is for drinking and the white meat inside the coconuts is for eating" % name +q
game21="James: Got it"+q
game22="%s: Okay James. Is it afternoon yet? Is the sun coming down?" % name +q
game23="James: Not yet. But it\'s about to" +q
game24="%s: Great. You need to find a shelter. Find somewhere dry to sleep tonight" % name +q
game25="James: Uhm I think I saw a cave next to the shore where I woke up. How about there?"+q
game26="%s: Uhm..." % name  +q

type(game19); delay(1); type(game20); delay(1); type(game21); delay(1); type(game22); delay(1); type(game23); delay(1); type(game24); delay(1); type(game25);delay(2)

decisionC=q+"1. Yes. Head there now" +q + "2. Can you travel forward for some distance? Maybe there\'s another cave in the jungle that\'s dry" +q
print decisionC

while True:
    C=raw_input("?:")
    if C not in ("1","2"):
        print something_else()
    else:
        break


if C == "1":
    score=score-1
    type(q+"James: Okay, heading back"+q)
    delay(1)
    type("%s: Text me when you get there" % name+q)
    delay(1)
elif C == "2":
    score=score+3
    type(q+"James: Are you sure? I think it\'s almost afternoon. What if there\'s no cave in the jungle?"+q)
    type("%s: I would hope there is one. The cave near the shore, seawater can get into it and drown or wet you in the middle of the night. It\'s better to stay dry" % name +q)
    type("James: Well, in that case.." +q)






delay(3)
game27="James: Okay I got to the cave! Welp, not as comfy as a motel room..." +q
game28="%s: Oh just shush. Now, you need to make a fire. You got the pocket knife?" % name +q
game29="James: Yes"+q
game30="%s: Just like how I taught you to make a fire. But you need something to burn on. Are there any wood pieces you see around?"% name+q
game31="James: There are some driftwood nearby. I also saw some tree branches on the ground where I chopped down coconuts. I think there\'s still enough sunlight to go to the tree branches. Or should I just pick up some driftwood?" +q
game32="%s: Uhmm.." % name +q+q

type(game27);delay(1);type(game28);delay(1);type(game29);delay(1);type(game30);delay(1);type(game31);delay(1);type(game32);delay(2.4)

decisionD=q+"1.Just pick up some driftwood. We don\'t know when the sun will set down, it might be dark if you go too far from the cave"+q+"2. If you can go to the tree branches as quickly as you can. Those are better for the fire"+q

print decisionD
while True:
    D=raw_input("?:")
    if D not in ("1","2"):
        print something_else()
    else:
        break

if D =="1":
    score=score-6
    type("James: Okay I will go get some driftwood"+q)
    delay(1)
    type("%s: Okay" % name +q)
    delay(2)
    type("James: Okay, the driftwood were so hard to catch fire, some of them are wet. I have to do... give me one second"+q)
elif D =="2":
    score=score+1
    type("James: Well then, if tree branches are better for the fire" +q)
    delay(1)
    type("%s: Yes. The driftwood if they are wet, that\'s not good for the fire" % name +q)
    delay(1)

delay(3)
game33="James: Okay, got the fire going" +q
game34="%s: Now you should get some sleep, better rest for what's to come tomorrow" % name +q
game35="James: Got it. Good night" +q
game36="%s: Sleep well" % name +q

type(game33);delay(1);type(game34);delay(1);type(game35);delay(1);type(game36);delay(1)
print q +q

delay(3)

if D=="1":
    
    type("- - 4 hours later - -"+q)
        
    delay(2)
            
    d1_1="James: Hey %s, I panicked and called you but I calmed down now" % name+q
    d1_2="%s: Hey, what's wrong? It's still the middle of the night at the island right?" % name +q
    d1_3="James: I think the fire went out" +q
    d1_4="%s: Must be the wet driftwood. Dang it, you should have got some dry tree branches. You can't go outside right now, it's too dark right?" % name +q
    d1_5="James: Heck yeah it's too dark. I can't even see anything in the cave!" +q
    d1_6="%s: I think it's best for you to stay awake. You don't know if any animals are nearby" % name +q
    d1_7="James: I'm scared, %s ..." % name +q
    d1_8="%s: Try to sit in one place. Take out the flashlight on your phone if you need to. Stay quiet and observe and listen around. If there's anything suspicious, text me" % name +q
    d1_9="James: Okay, got it. If there's anything I will text you" +q
    d1_10="%s: I'm here always if you need me. Take care" % name +q
                                                    
    type(d1_1);delay(1);type(d1_2);delay(1);type(d1_3);delay(1);type(d1_4);delay(1);type(d1_5);delay(1);type(d1_6);delay(1);type(d1_7);delay(1);type(d1_8);delay(1);type(d1_9);delay(1);type(d1_10)






#--------------------------D A Y 2-------------------------------







delay(2)
print q
type("- - - D A Y 2 - - -"+q+q)

game37="James: %s?" % name +q
game38="%s: James? Great James, you survived one night!" % name +q
game39="James: Yeah but, I\'m kinda thirsty now, I just drank up all my coconut water. And I don\'t think I want to drink sweetened water for the rest of my time here" +q
game40="%s: Let\'s go find some fresh water then. But first, prepare your left-over coconut shells. Smoothen the insides of those to hold water" % name +q
game41="James: Got it. Should I bring anything else?" +q
game42="%s: Definitely your pocket knife, and..." % name +q

delay(2);type(game37);delay(1);type(game38);delay(1);type(game39);delay(1);type(game40);delay(1);type(game41);delay(1);type(game42);delay(1)


decisionE=q+"1. Also bring some tree branches too. Might need that for special occasions"+q+"2. Nope. Don\'t bring too much you only have two hands" +q
print decisionE

while True:
    E=raw_input("?:")
    if E not in ("1","2"):
        print something_else()
    else:
        break

if E=="1":
    score=score+2
elif E=="2":
    score=score-5
game43="%s: Now head away from the beach. Go inside the jungle, see if you can find any bodies of fresh water" % name +q
game44="James: Okay. But hey uh, there\'s two paths to go into the jungle" +q
game45="%s: How are the two paths?" % name +q
game46="James: One is muddy, it must have rained. The other is full of rocks and trees" +q
game47="%s: Muddy, huh? There might not be firm ground there. The rocky path can also scratch you" % name +q
game48="James: What route should I take?" +q
game49="%s: Uhm.." % name +q

type(game43);delay(1);type(game44);delay(1);type(game45);delay(1);type(game46);delay(1);type(game47);delay(1);type(game48);delay(1);type(game49);delay(3)

decisionF=q+"1. Take the muddy path" +q+"2. Take the rocky path" +q
print decisionF

while True:
    F=raw_input("?:")
    if F not in ("1","2"):
        print something_else()
    else:
        break

type(q+"%s: And call me when you get to a body of water" % name +q)
delay(2)

if F == "1":
    type(q+"- - 20 minutes later - -"+q+q)
    delay(2)
    type("James: %s!" % name +q)
    delay(1)
    type("%s: What? James?" % name +q)
    delay(1)
    type("James:I..I'm stuck in... quicksand.." +q)
    delay(1)
    type("%s: No you can't! Wiggle out of it James!" % name +q)
    delay(1)
    type("James: It got to my neck %s. I just want to say goodbye to you. Thank you for helping me all these times.." % name +q)
    delay(1)
    type("%s: No, please James! No.." % name +q)
    delay(3)
    game_over()
print q
type("- - - a while later - - -")
delay(3)
print q

game50="James: Okay %s, I got out of the rocky road. Made a few scratches but I\'m fine. And wait I see something... Wow it\'s a lake!" % name +q
game51="%s: Oh great! Get some fresh water from the coconut shells you brought. Those might sustain you for a while" % name +q
game52="James: Got it. Also, is it a good idea to stay and have a swim in the lake? I really stink, kinda" +q
game53="%s: Is there still sunlight left? You've trekked for a while now right? It must be afternoon" % name +q
game54="James: Yeah it\'s in the afternoon. But I think there's enough sunlight. I really need a bath now" +q

type(game50);delay(1);type(game51);delay(1);type(game52);delay(1);type(game53);delay(1);type(game54);delay(2)

decisionG=q+"1. I think it\'s better to head back. The sun might be setting down faster than we think" +q+"2. Knock yourself out James. You\'ve been through enough, take a swim to recover your stamina"+q

print decisionG
while True:
    G=raw_input("?:")
    if G not in ("1","2"):
        print something_else()
    else:
        break

def if_E1():
    type("%s: Aww, you should have brought a wooden branch from in the morning. You could make a torch with your pocket knife and the wood." % name +q)
    delay(1)
    type("James: Uhm I'm scared.. I hear noises %s. I..I think I hear footsteps.." % name +q)
    delay(1)
    type("%s: Hang in there James... Dang it, you shouldn\'t have stayed in the lake. I know it must be dark quick" % name +q)
    delay(1)
    type("James: Oh no...I heard a bear..." +q)
    delay(1)
    type("%s: Stay put James, don\'t mov.." % name +q)
    type("James: Arghh!!" +q)
    type("%s: James!" % name +q)
    game_over()

def if_E2():
    type("%s: You got your spare wooden branch right? Make a torch out of that. You know how to do it?" % name+q)
    delay(1)
    type("James: Yeah, give me one second..."+q)
    delay(2)
    type("James: Ok I made the torch. Yay! I can see now!" +q)
    delay(1)
    type("%s: Now quickly head back to the cave. You might meet a bear or something else if you stay out in the wild at night" % name +q)
    delay(1)
    type("James: Okay. I'm heading back now, will call you when I got back" +q)
    delay(1)
    type("%s: Alright" % name +q)
    delay(1)


if G =="1":
    score=score+3
    type("James: Okay then. It gets dark really fast here, I don\'t know why" +q)
    delay(1)
    type("%s: Then go now, you won't have much time" % name +q)
    delay(1)
    type("James: Okay. I'm heading back now, will call you when I got back"+q)
    delay(1)
    type("%s: Alright" % name +q)
    delay(1)
elif G =="2":
    score=score-4
    type("James: Yay! Paradise pool here I come!" +q)
    delay(1)
    type("%s: Be careful. Be sure to call me later" % name+q)
    print q
    delay(3)
    type("- - - 2 hours later - - -"+q+q)
    delay(2)
    type("James: Hey %s, I'm done swimming. But it's getting dark now.."% name +q)
    type("%s: What? Really?" % name +q)
    type("James: Yeah, and I can't really see the way out back to the cave.."+q)
    delay(3)
    if E=="2":
        if_E1()
    elif E=="1":
        if_E2()
        score=score-1




print q
delay(3)
if C=="1":
    type("James: Uh %s.." % name+q)
    delay(1)
    type("%s: What James? You got to the cave right?" % name +q)
    delay(1)
    type("James: Yes, but..it\'s..it\'s flooded. Seawater is all over the place now..." +q)
    delay(1)
    type("%s: Dang it.. we should have found somewhere else that\'s dry. Well.. go look for someplace else that\'s dry, maybe another cave is nearby?" % name +q)
    delay(1)
    type("James: Ok...I\'m on my way.."+q)
    delay(2)
    type(q+"- - minutes later - - -"+q)
    delay(2)
    type("James: I found another cave! It\'s in the jungle but at least it\'s not flooded" +q)
    delay(1)
else:
    type("James: I got to the cave!" +q)

type("%s: Great. Now try to get some sleep. And be sure to make another fire" % name +q)
delay(1)
type("James: Already taken care of the fire. Now I\'m going to sleep"+q)
delay(1)
type("%s: Alright, good night! And don't let anything bite!" % name)
delay(4)








#-----------------------------D A Y 3-----------------------------









print q+q
type("- - - D A Y 3 - - -")
delay(3)
print q

game55="James: Hi %s! I just woke up!" % name +q
game56="%s: Oh great James! You just survived another night!" % name +q
game57="James: Yeah, I was lucky no animals attacked me last night" +q
game58="%s: Well let's hope you don't have to survive any other night on that island, or whatever that place is" % name +q
game59="%s: Okay, now I'm going to ask you to.." % name +q
game60="James: Wait, shhhh... I heard something.." +q
#delay here
game61="James: Let me go look outside the cave" +q
#delay here
game62="James: Oh no, it\'s a bear.. it\'s wandering outside the cave" +q
#delay
game63="James: Oh no! It saw me! What do I do what do I do?!" +q

type(game55);delay(1.1);type(game56);delay(1.1);type(game57);delay(1.1);type(game58);delay(1.1);type(game59);type(game60);delay(3);type(game61);delay(3);type(game62);delay(2);type(game63)

decisionH=q+"1. Just get out of the cave! Run!" +q+"2. Get a rock or something! Aim and throw at the bear's head!"+q+q
print decisionH

while True:
    H=raw_input("?:")
    if H not in ("1","2"):
        print something_else()
    else:
        break

if H=="1":
    score=score-7
    type("James: *bear roars*"+q)
    delay(0.5)
    type("%s: Run faster James!" % name +q)
    delay(0.5)
    type("James: I. am. running!"+q+q)
                            
    delay(2)
    type("- -10 minutes later- -"+q+q)
    delay(1)
    type("James: Oh no... %s.." % name +q)



elif H=="2":
    score=score+2
    type("James: Taste my rock you bear!" +q)
    delay(0.7)
    type("*thud*"+q)
    delay(2)
    type("James: Taste another of my rock!"+q)
    delay(0.7)
    type("*thud*"+q)
    delay(1)
    type("James: Okay bye bear! I\'m outa here!" +q)
    delay(0.7)
    type("*running footsteps sounds*"+q)
    delay(1)
    type("%s: Wait, James! What happened to the bear?" % name +q)
    delay(1)
    type("James: I knocked it unconscious! Clearly I picked the heaviest rocks!" +q)
    delay(0.3)
    type("%s: That's ridiculous!" % name +q)
    delay(0.5)
    type("James: Right? And now I\'m running for my life and... oh no.."+q)

delay(2)
game64="%s: What James?" % name +q
game65="James: I hit a rock wall. I don\'t know where I\'ve been running, this place is so strange" +q
game66="%s: Ookay...but is the bear still following you?" % name +q
game67="James: I don\'t think so... Oh wait nooo...the bear\'s coming! I can hear the footstep!!" +q

type(game64);delay(1);type(game65);delay(1);type(game66);delay(1);type(game67)

decisionL=q+"1.Find a tree and climb up there!" +q+"2.Find a bush and hide in there!"+q+q
print decisionL

while True:
    L=raw_input("?:")
    if L not in ("1","2"):
        print something_else()
    else:
        break

def if_M1():
    delay(2)
    type("*bear groans*" +q)
    delay(0.5)
    type("James: Oh no! The bear caught m..." +q)
    type("*phone drops on the ground*" +q)
    type("%s: Oh no..." % name +q)
    delay(2)
    game_over()

def if_M2():
    delay(3)
    type(q+"- -5 minutes later- -" +q+q)
    delay(1)
    type("James: I..I think the bear is gone..." +q)
    delay(1)
    type("%s: Oh thank goodness" % name +q)
    delay(1)
    type("James: Glad that\'s over.." +q)


if L=='1':
    score=score+2
    type(q+"James: Okay I'm climbing!" +q)
    delay(2)
    type("James: ... Oh no! * phone drops on the ground *" +q)
    delay(2)
elif L=="2":
    type("James: Okay I'm hiding!")
    delay(3)
    type(q+"*silence*"+q+q)
    delay(3)

decisionM=q+"1. Hello? James?!" +q +"2. *stays silent*"+q+q
if L=="2":
    print decisionM
        
    while True:
        M=raw_input("?:")
        if M not in ("1","2"):
            print something_else()
        else:
            break
            
    if M=="1":
        if_M1()
    elif M=="2":
        if_M2()
        score+=2

elif L=="1":
    print decisionM
        
    while True:
        M=raw_input("?:")
        if M not in ("1","2"):
            print something_else()
        else:
            break
            
    if M=="1":
        type("James: Oh no, the bear saw me! It\'s climbing the tree! Help %s!!" % name +q)
        type("%s: James!! No!!" % name +q)
        delay(3)
        game_over()
    if M=="2":
            if_M2()

game68="%s: Good job James. Now we have another task to do to get you out of there" % name +q
game69="James: Okay...I\'m listening" +q
game70="%s: You have to make a fire signal, it will catch the attention of any passing by ships or planes, or a rescue plane if they noticed you are missing" % name +q
game71="%s: First, prepare your pocket knife and some branches to make a fire" % name +q
game72="James: Got it"+q
game73="%s: Good. Next, find a clear area that is not covered by trees so that the smoke can be easily seen" % name +q
game74="James: I think the beach near my cave is fine, it doesn\'t have any trees blocking the smoke. Oh, and I can also go up to a hill, it\'s right next to the lake I took fresh water from" +q

type(game68);delay(1);type(game69);delay(1);type(game70);delay(1);type(game71);delay(3);type(game72);delay(1);type(game73);delay(1);type(game74);delay(2)

decisionN=q+"1. Just make the fire on the beach, it can be close to your cave" +q+"2. Go to higher ground, the smoke can attract better" +q
print decisionN
while True:
    N=raw_input("?:")
    if N not in ("1","2"):
        print something_else()
    else:
        break

if N=="2":
    score=score+1
    type(q+"James: If that\'s so, I will have to trek for a while" +q)
    delay(1)
    type("%s: If you\'re not tired, please do so. This will increase your chance of being discovered" % name +q)
    delay(1)
    type("James: Alright, I will see you in a couple of hours" +q)
    delay(6)
elif N=="2":
    type("James: Okay, I will talk to you later" +q)
    delay(1)
    type("%s: Take care" % name +q)
    delay(2)

game75="James: Alright, I got to my destination" +q
game76="%s: Now, make a fire. You know the drill" % name +q
game77="James: Aye" +q
game78="%s: After you got the fire going, make sure to put in the fire some grass and green sticks and branches. Those will make the smoke" % name +q
game79="James: Alrighty" +q
game80="%s: And after all of that, a single smoke column might not be enough. Take your shirt and wet it, then put it over the fire. Wait for a second and take the shirt off the fire. Repeating this sequence will make smoke puffs, they are more noticeable" % name +q
game81="%s: Just sit by the fire and occassionally make the smoke puffs. Hopefully, someone will notice that" % name +q
game82="James: Hey but, I can\'t sit here making smoke puffs forever. Who knows if someone will come, it could be weeks or months!" +q 
game83="%s: Haha don\'t worry, I called a rescue team two days ago. I gave them the path of the cruise ship you were on, hopefully they would be patrolling the area near you right now" % name +q 
game84="James: Ok thank goodness. I panicked so hard when I got here I forgot to tell you to bring help. Haha I thought I would build a raft and sail back to you with a beard and a pig friend!" +q 
game85="%s: Hah, don\'t be ridiculous" % name +q
game86="James: I was just joking. Okay, I should start making cloud puffs now. The smoke is ready I think!" +q 
game87="%s: Yes, please continue signalling. And, notice me when you see a plane or boat nearby" % name +q 
game88="James: Okay.." +q 
game89="- - - 2 hours later - - -" +q
game90="James: Hey %s!! I saw an airplane! It\'s coming at my direction!" % name +q 
game91="%s: Quick! Make some cloud puffs and do jumping jacks next to the fire!" % name +q 
game92="James: Heeeey!! Over heeeere!! Notice meeeeeee!! " +q 
game93="- - - 20 minutes later - - -" + q
game94="James: Hey %s! I got rescued!" % name +q 
game95="%s: Thank God! I\'m glad you\'re safe now!" % name +q
game96="James: Yeah I\'m heading back to mainland now. I\'ll see you if I can!" +q 
game97="%s: Just take care James. That\'s all I need." % name +q


type(game75);delay(1);type(game76);delay(1);type(game77);delay(1);type(game78);delay(1);type(game79);delay(1);type(game80);delay(1);type(game81);delay(1);type(game82);delay(1);type(game83);delay(1);type(game84);delay(1);type(game85);delay(1);type(game86);delay(1);type(game87);delay(1);type(game88);print q;delay(4);type(game89);print q;delay(4);type(game90);delay(1);type(game91);delay(3);type(game92);print q;delay(3);type(game93);print q;delay(1);type(game94);delay(1);type(game95);delay(1);type(game96);delay(1);type(game97);delay(1) 






#-------------------------END CREDITS--------------------------------






delay(2)
the_end=q+q+"- - - - T H E  E N D - - - -"+q+q
print the_end

delay(2)
score_display="Your score: %s/100" % score
print score_display



delay(3)

end1=q+"Hi %s! My name\'s Edward and thank you for playing my game! " % name

end2="Past all the cliche details and what not in this game "
end3="(like the unbelievable perfect phone service coverage on a stranded island), "
end4="I hope you enjoy my project! I would also encourage you to replay the game and make decisions that are diferent from your first (or latest) playthrough as "
end5="(stated in the beginning), "
end6="different decisions have different consequences. "
end7="Making different decisions the second round may boost your score! (As bad decisions minus points and good decisions grant points) "
end8="Again, thank you for playing S T R A N D E D ( ) !"

type(end1);delay(0.4);type(end2);delay(0.3);type(end3);delay(0.4);type(end4);delay(0.4);type(end5);delay(0.4);type(end6);delay(0.4);type(end7);delay(1);type(end8);delay(2);print q+q

lol1= q+q+"+ ------------------------ + " +q+q
print lol1.center(50)
delay(3)


#----------------------------E N D----------------------------------


game98="%s: Oh, and James?" % name +q
game99="James: Yeah?" +q
game100="%s: Charge your phone. It should have been dead right now" % name +q
game101="James: Oh yeah. Haha the phone situation is so ideal it\'s like we\'re in a fictional story.." +q

type(game98);delay(1);type(game99);delay(1);type(game100);delay(1);type(game101);print q+q+q+q 




































