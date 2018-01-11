from datetime import date
from collections import OrderedDict

# Gets total spending and avg days/visit for a category
def parse_category(obj, category):
    dates = []
    sum = 0
    print(category)
    for purchase in obj[category]:
        entry = list(purchase)

        sum += entry[1]

        d = entry[0].split("-")
        dates.append(date(int(d[0]), int(d[1]), int(d[2])))

    avg = 0
    dates.sort()
    for i in range(len(dates) - 1):
        avg += (dates[i] - dates[i + 1]).days

    if len(dates) > 0:
        val = avg / (len(dates))
        return(sum, abs(val))
    else:
        return(sum, 0)

# Parses all categories
def parse_data(obj):
    ret = {}
    for category in obj:
        c = parse_category(obj, category)
        ret[category] = c
    return ret

# Classifies warning and issue categories
def process(obj):
    parsed_data = parse_data(obj)
    sorted_data = OrderedDict(sorted(parsed_data.items(), key=lambda t: t[0]))
    print(sorted_data)
    sum = 0
    for entry in sorted_data:
        sum += sorted_data[entry][0]
    print("Total: {}".format(sum))

    status = {}
    for category in sorted_data:
        v = list(sorted_data[category])
        status[category] = ["", ""]
        if category != "other":
            if v[1] == 0 or v[1] >= 2.5:
                status[category][1] = "Good";
            elif v[1] < 2.5 or v >= 1:
                status[category][1] = "Warning";
            else:
                status[category][1] = "Bad";

            if (v[0] * 1.0) / sum > .25:
                status[category][0] = "Bad"
            else:
                status[category][0] = "Good"

    for category in status:
        print(category)
        print("Frequency: {}, Amount: {}".format(status[category][1], status[category][0]))
        print("---")
    #print(status)