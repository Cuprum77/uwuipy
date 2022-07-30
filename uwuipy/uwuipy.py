import re
import random as rand

class uwuipy:
    
    __uwuPattern = [['[rl]', 'w'], 
                ['[RL]', 'W'], 
                ['n([aeiou])', 'ny$1'],
                ['N([aeiou])', 'Ny$1'],
                ['N([AEIOU])', 'NY$1'],
                ['ove', 'uv']]

    __actions = ['***blushes***',
                 '***whispers to self***',
                 '***cries***',
                 '***screams***',
                 '***sweats***',
                 '***twerks***',
                 '***runs away***',
                 '***screeches***',
                 '***walks away***',
                 '***sees bulge***',
                 '***looks at you***',
                 '***notices buldge***',
                 '***starts twerking***',
                 '***huggles tightly***',
                 '***boops your nose***']

    __exclamations = ['!?',
                      '?!!',
                      '?!?1',
                      '!!11',
                      '?!?!'] 

    __faces = ["(・\`ω\´・)",
               ";;w;;",
               "OwO",
               "UwU",
               "\>w\<",
               "^w^",
               "ÚwÚ",
               "^-^",
               ":3",
               "x3"]

    def __UwuifyWords(self, _msg):
        # split the message into words
        words = _msg.split(' ')
        
        # itterate over each individual word
        # sure you could regex the entire thing, but then you lose
        # the ability to ignore certain cases, like pings and urls
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            # skip URLs
            if re.search('((http:|https:)//[^ \<]*[^ \<\.])', word):
                continue
            # skip pings
            if word[0] == '@':
                continue
            # for each pattern in the array
            for pattern in self.__uwuPattern:
                # attempt to use the pattern on the word
                word = re.sub(pattern[0], pattern[1], word)
            
            # add the modified word to the original words array
            words[idx] = word
            
        # return the joined string
        return ' '.join(words)

    def __UwuifySpaces(self, _msg, _seed, _stutterChance, _faceChance, _actionChance):
        # split the message into words
        words = _msg.split(' ')
        
        # itterate over each individual word
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            
            # create a random float
            rand.seed(_seed)
            randNum = rand.random()
            # get the character case for the second letter in the word
            NextCharCase = word[1].isupper() if len(word) > 1 else False
            _word = ''
            
            # if we are to add stutters, do it
            if randNum <= _stutterChance:
                # creates a random number between 1 and 2
                stutterLen = rand.randrange(1, 3)
                # add as many characters to the stutter as stutterlen dictates
                for j in range(stutterLen + 1):
                    _word += (word[0] if j == 0 else (word[0].upper() if NextCharCase else word[0].lower())) + "-"
                    
                # add in the whole word, but make sure the case matches the next rest of the word
                _word += (word[0].upper() if NextCharCase else word[0].lower()) + word[1:]
                
            # if we are to add a face, do it
            if randNum <= _faceChance:
                _word = (_word if _word else word) + ' ' + self.__faces[rand.randrange(0, len(self.__faces))]
                
            #if we are to add an action, do it
            if randNum <= _actionChance:
                _word = (_word if _word else word) + ' ' + self.__actions[rand.randrange(0, len(self.__actions))]
                
            # replace the word in the array with the modified if it exists, if not add the original word back
            words[idx] = (_word if _word else word)
            
        return ' '.join(words)
            
    def __UwuifyExclamations(self, _msg, _seed, _exclamationChance):
        # split the message into words
        words = _msg.split(' ')
        rand.seed(_seed)
        
        # itterate over each individual word
        for idx, word in enumerate(words):
            # skip empty entries
            if not word:
                continue
            # skip if an exclamation is not present or the random number is greater than the chance
            if (not re.search('[?!]+$', word)) or rand.random() > _exclamationChance:
                continue
            
            # strip the exclamation from the word, add new exclamations and return it to the words array
            index = rand.randrange(0, len(self.__exclamations))
            word = re.sub('[?!]+$', '', word) + self.__exclamations[index]
            words[idx] = word
        
        # return the joined string
        return ' '.join(words)

    def __init__(self, seed : int = None, stutterChance : float = 0.3, faceChance : float = 0.2, 
                 actionChance : float = 0.1, exclamationChance : float = 1):
        
        # input protection to make sure the user stays within allowed parameters
        if stutterChance > 1.0 or stutterChance < 0.0:
            raise Exception("Invalid input value for stutterChance, supported range is 0-1.0")
        if faceChance > 1.0 or faceChance < 0.0:
            raise Exception("Invalid input value for faceChance, supported range is 0-1.0") 
        if actionChance > 1.0 or actionChance < 0.0:
            raise Exception("Invalid input value for actionChance, supported range is 0-1.0") 
        if exclamationChance > 1.0 or exclamationChance < 0.0:
            raise Exception("Invalid input value for exclamationChance, supported range is 0-1.0") 
         
        self.seed = seed
        self.stutterChance = stutterChance
        self.faceChance = faceChance
        self.actionChance = actionChance
        self.exclamationChance = exclamationChance

    def uwuify(self, msg):
        msg = self.__UwuifyWords(msg)
        msg = self.__UwuifySpaces(msg, self.seed, self.stutterChance, self.faceChance, self.actionChance)
        msg = self.__UwuifyExclamations(msg, self.seed, self.exclamationChance)
        
        return msg