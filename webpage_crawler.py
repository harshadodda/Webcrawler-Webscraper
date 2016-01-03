import requests
from bs4 import BeautifulSoup
"""
Crawls through the pokemon database and extracts and displays data in the following order:
dexNumber name type1 [type2]
Note: type2 is optional
"""
def webpagespyder():

    url = 'https://www.pokedit.com/download/default-pkm/pokemon-black/'  # url of the database to be mined
    sourcecode = requests.get(url)  # request to connect to the url given
    plaintext = sourcecode.text  # takes only the source text and leaves off extras
    beautifulsoupobject = BeautifulSoup(plaintext, "html.parser")  # beautifulsoup object initialized

    # this loop goes through all of the <tr> tags and displays the data specified, the variable tabledata is each
    # row in the table
    for tabledata in beautifulsoupobject.findAll('tr'):

        dexnumber = tabledata.find('td', class_='dex').string  # dexnumber is the string in the
        # <td> with the 'dex' class

        pkmname = tabledata.find('td', class_='pkm-table-name').string  # pkmname is the string in the
        # <td> with the 'pkm-table-name' class

        typepkm = tabledata.find_all('span', class_='pkm-type')  # takes all <span> tags with the class
        # 'pkm-type' and turns each of them into a ResultSet object for each name. This acts like a list
        # so we cannot print the string contained within the <span> tag using the .string method we were
        # using earlier. We must iterate through the list

        print(dexnumber, pkmname, end=" ")  # prints the dexnumber and pkm name side by side for each row in the table

        for row in typepkm:  # iterates through the list of ResultSet object
            text = row.findAll(text=True)  # strips away everything but the text in the span tag

            for item in text:  # there may be more than one type so it prints all the types side by side
                print(item, end=" ")  # the 'end=" "' clause makes it so that there is no new line character at the
                # end of the print statement

        print()  # newline character will be printed so separate entries will be on different rows on the table

webpagespyder()
