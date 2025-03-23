import urllib.request as web

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def countVotesByParty(lines):
    '''
    Input: a xml file which has been processed as a list of strings
    It loops through every line in the file and find the Yes/No vote and the party of the person.
    Output: a list of four elements:
    democrats voting yes, democrats voting no
    republicans voting yes, republicans voting no
    '''
    dem_yes = 0
    dem_no = 0
    rep_no = 0 
    rep_yes = 0
    for line in lines:
        if "<recorded-vote>" in line:
            if "<vote>Yea</vote>" in line or "<vote>Aye</vote>" in line:
                if "party=\"D\"" in line:
                    dem_yes += 1
                elif "party=\"R\"" in line:
                    rep_yes += 1
            elif "<vote>Nay</vote>" in line or "<vote>No</vote>" in line:
                if "party=\"D\"" in line:
                    dem_no += 1
                elif "party=\"R\"" in line:
                    rep_no += 1
    return [dem_yes , dem_no, rep_yes, rep_no]


def isPartyLine(demYes, demNo, repYes, repNo):
    '''
    Input: demYes, demNo, repYes, repNo (which are processed by the countVotesByParty function above.)
    This will use conditions and operands to make the algorith of determining the requirement below:
    Output:
    A vote is called a party line vote if more than half of the voting members of one party vote in one way, and
    more than half of the voting members of the other party vote the other way. Hence, it will return True
    When the votes Yes or No is divided equally into two within a party, it is not a party line vote.
    Therefore, it will return False
    '''
    dem_half = (demYes + demNo) / 2
    rep_half = (repYes + repNo) / 2
    if demYes > dem_half and repNo > rep_half:
        return True
    elif demNo > dem_half and repYes > rep_half:
        return True
    elif repYes > rep_half and demNo > dem_half:
        return True
    elif repNo > rep_half and demYes > dem_half:
        return True
    elif demYes == demNo or repYes == repNo:
        return False



    
def getVoteFileFromWeb(url):
    '''
    This function downloads a temporary copy of a voting record file from the url
    and returns a list of lines representing each line in the file.
    
    Parameters: url: a string containing the address to download the voting data file from.

    Your url should be of the format: "https://clerk.house.gov/cgi-bin/vote.asp?year=<YEAR>&rollnumber=<NUMBER>"

    where <YEAR> and <NUMBER> are the year and roll-call number of the vote you want to obtain.

    Outputs: returns a list of the lines in the file obtained from the website
    '''
    webpage = web.urlopen(url)
    decodedLines = [line.decode('utf-8').rstrip() for line in webpage]
    webpage.close()
    return decodedLines
