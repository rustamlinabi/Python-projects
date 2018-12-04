"""
This code takes a news article and returns TL DR version of it, work in progress, inspired by respective reddit bot
"""

a=r"WASHINGTON (Reuters) - The United States on Thursday displayed pieces of what it said were Iranian weapons deployed to militants in Yemen and Afghanistan, a tactic by President Donald Trump’s administration to pressure Tehran to curb its regional activities. The second presentation of Iranian weapons by the Pentagon, many of which were handed over by Saudi Arabia, coincides with growing concern in Congress over USA military support for the Saudi-led coalition in Yemen’s civil war, which has led to a deep humanitarian crisis. Members of Congress have escalated their opposition to Saudi Arabia after the Oct 2 killing of Saudi journalist Jamal Khashoggi in its Istanbul consulate. Despite administration pleas to stick with the Saudis and thereby counter Iran, the Senate voted on Wednesday to advance a resolution to end military support for the Saudis in Yemen. If Iran were found to be shipping arms to Yemen, Afghanistan and other countries, it would be in violation of United Nations resolutions. Reuters was given advanced access to the military hangar at Joint Base Anacostia-Bolling just outside of Washington where the USA Defense Department put the fragments of weaponry on display and explained how it concluded that they came from Iran. “We want there to be no doubt across the world that this is a priority for the United States and that it’s in international interest to address it,” said Katie Wheelbarger, the principal deputy assistant secretary of defense for international security affairs. The presentation, the second such one in the last year, is part of a government-wide effort to follow through on Trump’s policy to take a far harder line toward Tehran. He pulled the United States out of the Iran nuclear deal and reimposed sanctions, in part for its “malign” regional activities. Iran has denied supplying the Houthis in Yemen with such weaponry and described the Pentagon’s previous arms display as “fabricated.” The Pentagon offered a detailed explanation of why it believed the arms on display came from Iran, noting what it said were Iranian corporate logos on arms fragments and the unique nature of the designs of Iranian weaponry. The United States acknowledged it could not say precisely when the weapons were transferred to the Houthis, and, in some cases, could not say when they were used. There was no immediate way to independently verify where the weapons were made or employed. This included a “Sayyad-2” surface to air missile (SAM), which the Pentagon said had been interdicted by the Saudi government in early 2018 enroute to Houthi militants in Yemen. The Pentagon cited a corporate logo of an Iranian defense firm in the warhead section, which was not displayed, and writing in Farsi along the missile as evidence that it was Iranian. A USA defense official, speaking on the condition of anonymity, acknowledged that the Pentagon did not know if the Houthis had actually used this type of missile before. The Houthis, who control Yemen’s capital Sanaa, have fired dozens of missiles into Saudi Arabia in recent months, part of a three-year-old conflict widely seen as a proxy battle between Saudi Arabia and Iran. Under a U.N. resolution that enshrines the Iran nuclear deal with world powers, Tehran is prohibited from supplying, selling or transferring weapons outside the country unless approved by the U.N. Security Council. A separate U.N. resolution on Yemen bans the supply of weapons to Houthi leaders. WAR IN AFGHANISTAN The United States has long accused Iran of providing weapons to Taliban militants in Afghanistan. In October, Washington targeted two individuals linked to the Quds Force of Iran’s Revolutionary Guards for providing material and financial support to the Taliban. The Pentagon displayed a number of “Fadjr” rockets, that it said had been provided to the Taliban. It said they were Iranian because of the unique markings on the rockets and the paint scheme, along with the markings on them. The Taliban is known to buy weapons on the black market and defense officials could not say why they were sure these missiles had not been simply bought by the Taliban. "

t=a.replace(", "," ").replace(". ", " ").replace("("," ").replace(")"," ").split(" ")
sent=a.split(". ")
l=[]
pat1= r"(\$[^\$]+\$)[\s\.]"
pat2= r"(\$[^\$]+\.\$)"
import re
tero=re.findall(pat1,a)

zero=re.findall(pat2,a)

unusd=["the","a","at","and","for","on","in","be","may","will","an"," ","of","that","is","was","to","or","","with","not","are","this","as","by", "etc","who", "have","work","job","other","but","my","it"]

l=[a.lower() for a in t if a.lower() not in unusd]
words=[]
comb=[]
tr=[a.lower() for a in t]
for n,z in enumerate(tr):
    try:
        comb.append(z+" "+tr[n+1])
    except:
        break
z={}
l=l+comb
for x in l:
    r=[0,0]
    r[0]=x
    r[1]=l.count(x)
    if r not in words:
        z[x]=l.count(x)
        words.append(r)
    else:
        continue
text=""
for x in sent:
    sentwor=x.replace(", "," ").replace("("," ").replace(")"," ").split(" ")
    sentword=[a.lower() for a in sentwor if a.lower() not in unusd]
    n=0
    for rer in sentword:
        for f in words:
            if rer==f[0]:
                n+=f[1]

    for l,t in enumerate(sentword):
        try:
            test=t+" "+sentword[l+1]
            for f in words:
                if test==f[0]:
                    n+=f[1]
        except:
            continue

    if n>(len(sentword)*3.5) and len(sentword)>3:
        #print(x+".")
        text=text+x+"."
print(len(text),len(a))
print(text)