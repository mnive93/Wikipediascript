import wikipedia
def collect_datasets():
    topics = {}
    topics['Economics and Finance'] = 'economics.txt'
    topics['International Business'] = 'international.txt'
    topics['Comics'] = 'comics.txt'
    topics['Fiction'] = 'fiction.txt'
    topics['Poetry'] = 'poetry.txt'
    topics['Computer Science'] = 'computerscience.txt'
    topics['Homosexuality'] = 'homo.txt'
    topics['Wedding'] = 'wedding.txt'
    topics['Love'] = 'love.txt'
    topics['Nutrition'] = 'nutrition.txt'
    topics['Medicine'] = 'medicine.txt'
    topics['Space Science'] = 'space.txt'
    topics['Earth Science'] = 'earth.txt'
    topics['Life Science'] = 'life.txt'
    topics['Physical Fitness'] = 'fitness.txt'
    topics['Architecture'] = 'arch.txt'
    topics['Choreography'] = 'choreo.txt'
    topics['Bollywood'] = 'bollywood.txt'
    topics['Hollywood'] = 'hollywood.txt'

    for topic,file in topics.iteritems():
        print "Searching %s"% topic
        f = open(file,'wb')
        page  = wikipedia.page(topic)
        f.write(page.content.encode('utf-8'))
        f.close()

collect_datasets()




