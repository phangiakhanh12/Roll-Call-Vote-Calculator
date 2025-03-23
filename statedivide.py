'''
A program that plots the number of members of the House of Representatives
that are either Democratic or Republican from 2003 to 2023 (inclusive).

Authors: Khanh Phan
Date Created: 11/21/2024
'''
from utilities import STATES, getVoteFileFromWeb
import matplotlib.pyplot as plt
def countRepresentatives(lines, state):
    '''
    This function is created to count the democrats and republicans in a state.
    Inputs: 
    lines: A xml file of a year and a vote call has been processed as a list of strings. This can be retrieved by
    the getVoteFileFromWeb function.
    state: a string, which is the name of a state in the US.
    Outputs:
    the number of democrats and republicans representatives for each (There are two integers values)
    '''
    dem_represent = 0
    rep_represent = 0
    the_state_string = "state=" + "\"" + state + "\""
    for line in lines:
        if "<recorded-vote>" in line:
            if the_state_string in line:
                if "party=\"D\"" in line:
                    dem_represent += 1
                elif "party=\"R\"" in line:
                    rep_represent += 1
    return dem_represent, rep_represent

def stateDivide(state):
    '''
    This function is created to make a list of democratic and republicans for a state within a time range of 2004 - 2023.
    Input: state (the name of the state as a string)
    It will loop through each year and calling getVoteFileFromWeb and countRepresentatives to add the values of each year
    to a list
    Outputs: two lists of democratics representatives and republicans representatives.
    '''
    index_of_the_state = STATES.index(state)
    the_state_name = STATES[index_of_the_state]
    dem_represent_list = []
    rep_represent_list = []
    for years in range (2004, 2024):
        blueprint_string = "https://clerk.house.gov/cgi-bin/vote.asp?year=" + str(years) + "&rollnumber=" + str(1)
        file_to_read = getVoteFileFromWeb(blueprint_string)
        dem_represent, rep_represent = countRepresentatives(file_to_read, the_state_name)
        dem_represent_list.append(dem_represent)
        rep_represent_list.append(rep_represent)
    return dem_represent_list, rep_represent_list

def PlotstateDivide ():
    '''
    This function is kind of like the main function. It is called just for graphing the data with matplotlib.pyplot
    It uses the data from the two functions above and uses methods of the matplotlib.pyplot module to create a comprehensible
    graph of democrats and republicans of a state for each year. To know the data of different states, users have to change the
    input in line 66.
    '''
    years_list = []
    for _ in range (2004, 2024):
        years_list.append(_)
    
    '''
    You can change  the input in line 66 to know the democrats and republicans representatives of different states.
    '''
    the_surveyed_state = "OH"
    dem_represent_list, rep_represent_list = stateDivide(the_surveyed_state)

    plt.plot(years_list, dem_represent_list, label = "Democrats", color = "blue")
    plt.plot(years_list, rep_represent_list, label = "Republicans", color = "red")

    plt.xlabel("Years")
    plt.ylabel("Number of Representatives")

    plt.title(f"Distribution of Congressional Representatives for {the_surveyed_state} from 2004 - 2023")

    plt.xticks(range(2004, 2024, 1))
    plt.yticks(range(0, 16, 1))

    plt.legend()

    plt.show()

PlotstateDivide()