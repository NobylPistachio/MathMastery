

def translateDayOfWeek(day):
    match day:
        case "sun": return 0
        case "mon": return 1
        case "tues": return 2
        case "wed": return 3
        case "thurs": return 4
        case "fri": return 5
        case "sat": return 6
        case 0: return "sun"
        case 1: return "mon"
        case 2: return "tues"
        case 3: return "wed"
        case 4: return "thurs"
        case 5: return "fri"
        case 6: return "sat"
    raise Exception("Please use something from the following list of accepted inputs\n['sun','mon','tues','wed','thurs','fri','sat'] or 1-7")

def dayOfWeekRemainder(initialDay,days):
    "This works, but according to khanAcademy if it was monday and you go on a 1 day trip it will still be monday so take it as you will for trips"
    week = days//7
    day = days%7
    firstDay = translateDayOfWeek(initialDay)
    lastDayOfWeek = firstDay + day
    if lastDayOfWeek > 7:
        lastDayOfWeek -= 7
        week += 1
    return translateDayOfWeek(lastDayOfWeek)

def patternWithNumbers(listOfNum:list,rule):
    
    print(rule(1)) 

patternWithNumbers([2],lambda x: x+6)