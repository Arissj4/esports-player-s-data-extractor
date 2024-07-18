from Lib import libs


def find_name(details):
    name = "Name:"
    rn = "Romanized Name:"
    index_name = ""
    if rn in details:
        index_name = details.index(rn)
        return details[index_name + 1]

    elif name in details:
        index_name = details.index(name)
        return details[index_name + 1]
    else:
        return "No Information"


def birth(details):
    brh = "Birth:"
    if brh in details:
        index_brh = details.index(brh)
        return details[index_brh + 1]
    else:
        return "No Information"


def Country(details):
    cuy = ["Country:", "Nationalities:", "Nationality:"]
    for i in range(len(cuy)):
        if cuy[i] in details:
            index_cuy = details.index(cuy[i])
            c_name = details[index_cuy + 1]
            return c_name[1:]
    else:
        return "No Information"


def status(details):
    sta = "Status:"
    if sta in details:
        index_sta = details.index(sta)
        s = details[index_sta + 1]
        if "Active" in s:
            return "Active"
        elif "Inactive" in s:
            return "Inactive"
        elif "Retired" in s:
            return "Retired"
    else:
        return "No Information"


def team(details):
    tm = "Team:"
    if tm in details:
        index_tm = details.index(tm)
        return details[index_tm + 1]
    else:
        return "No Information"


def role(details):
    rl = ["Role(s):", "Role:"]
    for i in range(len(rl)):
        if rl[i] in details:
            index_rl = details.index(rl[i])
            return details[index_rl + 1]
    else:
        return "No Information"


def earn(details):
    er = ["Approx. Total Earnings:", "Approx. Total Winnings:"]
    for i in range(len(er)):
        if er[i] in details:
            index_er = details.index(er[i])
            return details[index_er + 1]
    else:
        return "No Information"


def id(details):
    id = "Alternate IDs:"
    if id in details:
        index_id = details.index(id)
        return details[index_id + 1]
    else:
        return "No Information"


def hero(details, game):
    img_list = []
    for imgs in details.findAll("img"):
        img_list.append(imgs["alt"])
    # for lnk in details.findAll("a"):
    #     l.append(lnk["title"])
    while "" in img_list:
        img_list.remove("")

    title_list = []
    a_tag = details.findAll("a")
    for ti in a_tag:
        title_list.append(ti.get("title"))

    while None in title_list:
        title_list.remove(None)

    if game in ["counterstrike", "pubg", "rocketleague"]:

        return "No special characters"

    else:
        game_name = game
        hero_csv = libs.pd.read_csv("csv/Heroes.csv")
        hero_list = hero_csv[game_name]
        li = list(hero_list)

        img_name = ""
        hero_li_img = []
        for i in range(0, len(img_list)):
            if img_list[i] in li:
                hero_li_img.append(img_list[i])
                img_name = img_name + img_list[i] + ","
        img_name = img_name[:-1]

        if not hero_li_img:
            title_name = ""
            hero_li_title = []
            for i in range(0, len(title_list)):
                if (title_list[i] in li) and (title_list[i] not in hero_li_title):
                    hero_li_title.append(title_list[i])
                    title_name = title_name + title_list[i] + ","
            title_name = title_name[:-1]

        if hero_li_img:
            return img_name
        elif hero_li_title:
            return title_name
        else:
            return "No Information"


def achiv(details):
    b = []
    hoursTable = details.find_elements_by_css_selector("table.wikitable tbody tr")
    for i in hoursTable:
        a = ""
        td_ho = i.find_elements_by_css_selector("td")
        for j in td_ho:
            if j.text != "" and j.text != " ":
                a += j.text + "|" + " "
        b.append("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
        b.append(a)
    return b
