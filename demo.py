import json
from audioblast import audioblast

reclist = audioblast.traits(max_page=2)

print(reclist[0])