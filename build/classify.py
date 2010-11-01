from build import generatePostList
from renderer import readFileContents
from reverend.thomas import Bayes

import json

guesser = Bayes()

for controlFilename in generatePostList("posts"):
    control = json.loads(readFileContents(controlFilename), encoding='utf-8')
    content = readFileContents(controlFilename.replace(".control", ""))

    for cat in control["categories"]:
        guesser.train(cat, content)

for controlFilename in generatePostList("posts"):
    control = json.loads(readFileContents(controlFilename), encoding='utf-8')
    content = readFileContents(controlFilename.replace(".control", ""))

    for guess in guesser.guess(content):
        if guess[1] > 0.05 and guess[0] not in control["categories"] and not guess[0] == "personal":
            print control["title"], guess[0]