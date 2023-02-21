paths = {
  "model" : "./models/model.joblib",
  "vectorizer": "./models/word_to_vec.joblib"
}


single_value_cols = ["title", "synopsis", "type"]
list_value_cols = ["genders", "producers", "studio"]

fields_name = single_value_cols + list_value_cols

nltk_ressources = {
  "stopwords" : "corpora/stopwords",
  "punkt" : "tokenizers/punkt"
}


test_predict = {
  "params" : {
    "title" : "Cowboy Bebop",
    "synopsis":"""In the year 2071, humanity has colonized several of the planets and moons of the solar system leaving the now uninhabitable surface of planet Earth behind. The Inter Solar System Police attempts to keep peace in the galaxy, aided in part by outlaw bounty hunters, referred to as "Cowboys." The ragtag team aboard the spaceship Bebop are two such individuals. \r\n  \r\nMellow and carefree Spike Spiegel is balanced by his boisterous, pragmatic partner Jet Black as the pair makes a living chasing bounties and collecting rewards. Thrown off course by the addition of new members that they meet in their travels—Ein, a genetically engineered, highly intelligent Welsh Corgi; femme fatale Faye Valentine, an enigmatic trickster with memory loss; and the strange computer whiz kid Edward Wong—the crew embarks on thrilling adventures that unravel each member\'s dark and mysterious past little by little. \r\n \r\nWell-balanced with high density action and light-hearted comedy,  Cowboy Bebop  is a space Western classic and an homage to the smooth and improvised music it is named after. \r\n \r\n[Written by MAL Rewrite]""",
    "type":"TV",
    "genders":"['Action', 'Adventure', 'Comedy', 'Drama', 'Sci-Fi', 'Space']",
    "producers":"['Bandai Visual']",
    "studio":"['Sunrise']",
  },
  "result" : 7.7
}

test_stress = {
  "nb_request" : 10,
  "time":60
} 
