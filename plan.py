from _ import interact, readTalkFile, checkcmd


def talk():
    checkcmd()
    interact(readTalkFile())
"""
# Exchange Name #

// Converse
told:
    - Hey
    - You suck

response:
    - Hello 
   - You smell


------------------------
// Save User Property
feed:
    - my name is
    - my name,
    - I am called
    - this is   // this's ??

feedback:
    - Got It!!
    //- Hello {"USER_NAME"}
    //- Hi {"USER_NAME"}


// Utilize The Property
question:
    - remember me?

answer:
    - yes master your name is {"USER_NAME"} !

---------------------------------

ExchangeName = (KeyPhr, Response)
KeyPhr(,,,,)
    - my name is
    - my name,
    - I am called
    - this is   // this's ??

Response(,,,)
Response:
    - Hello {"USER_NAME"}
    - Hi {"USER_NAME"}
"""
