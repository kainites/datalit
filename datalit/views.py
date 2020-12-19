from django.shortcuts import render

# Create your views here.

def lita(request):
    if 'litext' in request.GET.keys():

        text = request.GET['litext']
        words = text.split()
        paras = text.split('\n')
        paragraphs = []
        punctuation = '~!@#$%^&*()_+`-=[]{}|\/;\'.,<>?":"'
        dictwords = {}
        comwords = []
        vcws = [
        'the', 'a', 'and', 'but', 'is', 'was', 'had', 'have', 'been',
        'were', 'are', 'that', 'so', 'as', 'with', 'in', 'into', 'out',
        'i', 'of', 'to', 'from', 'my', 'me', 'your', 'you', 'it', 'its',
        'itself', 'she', 'her', 'hers', 'herself', 'they', 'their', 'them',
        'themself', 'theirself', 'he', 'him', 'his', 'himself', 'we', 'us', 
        'not', 'at', 'for', 'on', 'under', 'over', 'be', 'being', 'would',
        'will', 'could', 'can', 'have', 'had', 'may', 'or', 'and', 'but',
        'which', 'this', 'that', 'who', 'what', 'where', 'there', 'here',
        'by', 'from', 'to', 'than', 'then', 'an', 'when', 'like', 'mine',
        'do', 'should', 'could', 'shall', 'don\'t'
        ]

        for line in paras:
            if line != '\r' and line != '\n':
                paragraphs.append(line)
        # get the paragraphs into a list, each is a list value (?)

        paralen = len(paragraphs)
        wordslen = len(words)
        # get the number of paragraphs and words

        if wordslen < 5:
            comwords = ['please', 'enter', 'at least', 'five', 'words']
            return render(request, 'datalit/litsite.html', {'wcount' : wordslen, 'pcount' : paralen, 'comlist' : comwords[:5]})

        for word in words:
            while word[-1] in punctuation:
                word = word[:-1]
            while word[0] in punctuation:
                word = word[1:]
        # get the words to all be uncapitalised and without ending / starting punctuation
            
            if word not in dictwords:
                dictwords[str(word)] = 1
            else:
                comnum = dictwords[str(word)]
                comnum += 1
                dictwords[str(word)] = comnum
        # get the words to all be added to dictwords with their freuqncy of occurence
       
        for vcw in vcws:   
            if vcw.lower() in dictwords:
                dictwords.pop(vcw.lower())
            if vcw.upper() in dictwords:
                dictwords.pop(vcw.upper())
            if vcw.capitalize() in dictwords:
                dictwords.pop(vcw.capitalize())
        # get the dictionary to only have less commmon words

        comindex = sorted(dictwords.items(), key=lambda x: x[1], reverse=True)
        # get the tuples to be sorted in order and placed in a list
        print(comindex)

        count = 0
        for index in comindex:
            count += 1
            if count <= 5:
                comwords.append('{} ———— used {} times'.format(index[0], index[1]))
        # get the five most common words
        
        return render(request, 'datalit/litsite.html', {'wcount' : wordslen, 'pcount' : paralen, 'comlist' : comwords[:5]})

    return render(request, 'datalit/litsite.html', {'wcount' : 'what', 'pcount' : 'what', 'comlist' : 'what'})