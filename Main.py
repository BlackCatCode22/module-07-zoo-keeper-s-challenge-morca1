from Animal import Animal
from hyena import hyena
from lion import lion

from datetime import lion

# create lists of the species
list_of_hyenas = [Shenzi, Banzai, Ed, Zig, Bud, Lou, Kamari, Wema, Nne, Madoa, Prince Nevarah]
list_of_lions = [Scar, Mufasa, Simba, Kiara, King, Drooper, Kimba, Nala, Leo, Samson, Elsa, Cecil]
list_of_tigers = [Tony, Tigger, Amber, Cosimia, Cuddles, Dave, Jiba, Rajah, Rayas, Ryker]
list_of_bears = [Yogi, Smokey, Paddington, Lippy, Bungle, Baloo, Rupert, Winnie the Pooh, Snuggles, Bert]

# this is needed for the species
current_date = date.today()
current_year = current_date.year

def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif " winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"

def process_one_line(one_line):
    # create variable to help parse arrivingAnimals.txt

    a_species = ""
    a_sex = ""
    age_in_years = 99

    season = ""
    color = ""
    weight = ""
    orgin_01 = ""
    orgin_02 = ""

    print(one_line)
    groups_of_words = one_line.strip().split(",")
    print(groups_of_words)
    single_words = groups_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_sex = single_words[3]
    a_species = single_words[4]
    single_words = groups_of_words[1].strip().split(" ")
    season = single_words[2]
    color = groups_of_words[2].strip();
    weight = groups_of_words[3].strip();
    orgin_01 = groups_of_words[4].strip();
    orgin_02 = groups_of_words[5].strip();

    from_zoo = orgin_01 + "," + orgin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:
        # create a hyena object
        my_hyena = Hyena("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in the name and ID
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "My" + str(hyena.numOfHyenas).zfill(2)
        # add to the hyena list
        list_of_hyenas.append(my_hyena)

    if "lion" in a_species:
        # create a lion object
        my_lion = Lion("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in the name and ID
        my_lion.name = Lion.get_lion_name(my_lion)
        my_lion.animal_id = "My" + str(lion.numOfLions).zfill(2)
        # add to the lion list
        list_of_lions.append(my_lion)

    if "tiger" in a_species:
        # create a tiger object
        my_tiger = Tiger("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in the name and ID
        my_tiger.name = Tiger.get_tiger_name(my_tiger)
        my_tiger.animal_id = "My" + str(tiger.numOfTigers).zfill(2)
        # add to the tiger list
        list_of_tigers.append(my_tiger)

    if "bear" in a_species:
        # create a bear object
        my_bear = Bear("aName", "anID", birth_day, color, a_sex, weight, from_zoo, current_date)
        # fill in the name and ID
        my_bear.name = Bear.get_bear_name(my_bear)
        my_bear.animal_id = "My" + str(bear.numOfBear).zfill(2)
        # add to the bear list
        list_of_bears.append(my_bear)