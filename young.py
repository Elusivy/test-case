import urllib.request as req
import json
from tkinter import *

young_man = ['Max', 99]
young_woman = ['Mary', 99]


res = req.urlopen("http://testlodtask20172.azurewebsites.net/task").read()
res = json.loads(res)

for human in res:
    id = human['id']
    res1 = req.urlopen("http://testlodtask20172.azurewebsites.net/task/" + id).read()
    res1 = json.loads(res1)

    name = res1['name']
    sex = res1['sex']
    age = res1['age']

    if sex == 'male':
        if age < young_man[1]:
            young_man[0] = name
            young_man[1] = age
    else:
        if age < young_woman[1]:
            young_woman[0] = name
            young_woman[1] = age

root = Tk("Youngest people")

l1 = Label(root, text = "Youngest man - " + young_man[0] + ", he's " + str(young_man[1]))
l2 = Label(root, text = "Youngest woman - " + young_woman[0] + ", she's " + str(young_woman[1]))

l1.pack()
l2.pack()

root.mainloop()




