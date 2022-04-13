import nltk, re
from nltk.corpus import wordnet as wn
print('::  Assignment 2\n::  Noble Menchaca')

#find the Lowest Common Hypernym for giant panda, dog, tortoise.
panda = wn.synset('giant_panda.n.01')
dog = wn.synset('dog.n.01')
tort = wn.synset('tortoise.n.01')
motorcar = wn.synset('motor_vehicle.n.01')

print(panda.lowest_common_hypernyms(dog))
print(panda.lowest_common_hypernyms(tort))
print(dog.lowest_common_hypernyms(tort))

# find the minimum path depth between the 3 animals
print(wn.synset('carnivore.n.01').min_depth())
print(wn.synset('vertebrate.n.01').min_depth())
print(wn.synset('vertebrate.n.01').min_depth())

# find minimum semantic similarity between the 3 animals
print(panda.path_similarity(dog))
print(panda.path_similarity(tort))
print(dog.path_similarity(tort))

#Supergloss function
def supergloss(syn):
    string = ''
    paths = syn.hypernym_paths()
    for item in paths[0]:
        deff = str(item.definition())
        lemma = item.lemma_names()
        string += str(lemma)
        string += ' : '
        string += deff
        string += '\n'
    return string


print(supergloss(motorcar))

print('__Part3__')
'''
Write regular expressions that will search 2 kinds of strings
    A. the determiners "a", "an", "the" not capital sensitive
    B. Mathematical expressions with integers and + and *
Test these with 10 strings for each
'''
strings = [
    'A few days ago I found a new recipe for a delicious sounding dessert',
    'The recipe was for an Orange Ricotta Pound Cake',
    'I\'ve been wanting to try a baking recipe with ricotta',
    'And this was the perfect opportunity',
    'What a tasty treat for the weekend',
    'I checked my fridge and found all necessary ingredients',
    'Most times I\'m missing something small like vanilla',
    'after measuring out all my materials',
    'I began to mix together flours and fruit and cheese',
    'Soon enough I had this flavorful breakfast item to pair with my coffee']

strings2 = [
    'I\'m afraid I\'m not motivated enough to write up excuses to use mathematical operations',
    'Instead I will say that I\'ve been really enjoying cooking\\baking recently',
    'so much so that I\'ve been bookmarking food blogs from all around the web to try new things',
    'It has gotten to the point where I need to have nested folders to organize all the recipes I save',
    'some for Thai food, for Indian, Japanese, some for dessert... but mostly I love breakfast recipes.',
    'OKay back to business, here are math expressions 33+234 234+56 11+00001 9cc9+090',
    'And some more expressions 99+1 99*999 math math math 987+123',
    'Seriously though I\'m thinking about what to make next 55+45 12+68',
    'I just bought a bunch of strawberries on sale 7575+2342 998***909',
    'I\'ll probably look up more recipes after I\'m done with this 9+1 1+msm0 +234+23 *3254*2345 123 24 1'
]
print('\n\n__Determiner Finder__')
for i in range(len(strings)):
    tokens = nltk.word_tokenize(strings[i])
    determiners = [w for w in tokens if re.search('^(A|a)n*$', w) or re.search('^(T|t)he$', w)]
    print('determiners for string '+ str(i+1) + '    :  ' + str(determiners))

print('\n\n___Math Expressions__')
for i in range(len(strings2)):
    tokens = nltk.word_tokenize(strings2[i])
    maths = [w for w in tokens if re.search('^[0-9]+(\+|\*)[0-9]+$', w)]
    print('math statements for string '+ str(i+1) + ':  ' + str(maths))
