import urllib.request
import webbrowser


def random_wiki():
    while True:
        # open a json format file of random wiki articles
        link = urllib.request.urlopen("https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace"
                                      "=0&rnlimit=10&format=json")
        # turn into a string
        data = link.read().decode("ascii")
        link.close()

        # get the id and title from the contents of the page
        for i in range(10):
            # look for patterns in the content
            start_id = data.find("id") + 4
            end_id = data.find("ns") - 1
            id_number = data[start_id: end_id]
            data = data[end_id:]

            start_title = data.find("title") + 8
            end_title = data.find("},{")
            title = data[start_title: end_title]
            data = data[end_title:]

            # ask user for input
            print("Would you like to read about %s?" % title)
            answer = input("Press y to read. Press enter to continue browsing. Press q to quit.\n")

            if answer == "y":
                webbrowser.open_new_tab("http://en.wikipedia.org/wiki?curid=" + id_number)
            elif answer == "q":
                exit(0)
            else:
                continue


random_wiki()








