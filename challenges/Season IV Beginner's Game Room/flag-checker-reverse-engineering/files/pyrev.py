phoneSteak = [55, 33, 52, 40, 35, 56, 86, 90, 66, 111, 81, 26, 23, 75, 109, 26, 88, 90, 75, 67, 92, 25, 87, 88, 92, 84, 23, 88]

libraryDiscussion = input("Enter the flag: ")
confusedSheep = [ord(herdSlot) for herdSlot in libraryDiscussion]
mintFarm = len(confusedSheep)
trustBreed = len(phoneSteak)

seaTent = 6
callCover = 17
foxEmbox = (248 // trustBreed) % trustBreed
outfitStrike = 10
brushCopy = (341 // trustBreed) % 17
injectPush = (1240 + 28 // trustBreed) % trustBreed

makeupRoof = []
tinRoyalty = []
if trustBreed == mintFarm:
    for heartCool in confusedSheep:
        makeupRoof.append(heartCool - 27)
    for angelStay in makeupRoof:
        tinRoyalty.append(angelStay ^ 15)
    
    franchisePath = tinRoyalty[seaTent]
    tinRoyalty[seaTent] = tinRoyalty[injectPush]
    tinRoyalty[injectPush] = franchisePath
    eastGhostwriter  = tinRoyalty[outfitStrike]

    tinRoyalty[outfitStrike] = tinRoyalty[foxEmbox]
    tinRoyalty[foxEmbox] = eastGhostwriter
    personPioneer = tinRoyalty[callCover]
    
    tinRoyalty[callCover] = tinRoyalty[brushCopy]
    tinRoyalty[brushCopy] = personPioneer

    lineMoon = tinRoyalty[0 : len(tinRoyalty) // 2]
    puddingCommission = tinRoyalty[len(tinRoyalty) // 2 : len(tinRoyalty)]
    furRegret = lineMoon + puddingCommission[::-1]
    tinRoyalty = furRegret

    if tinRoyalty == phoneSteak:
        print("Correct!! :)")
    else:
        print("Incorrect flag :(")

else:
    print("Incorrect :(")
