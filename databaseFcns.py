# Place any necessary imports here
import sqlite3
import parsers
import parsers

#WORKED WITH Steve, Lucas, Zach, Marrisa

####################################################
# Part 0
####################################################

# Move your parsers.py file to your Problem Set 7
# directory. Once you've done so, you can use the 
# following code to have access to all of your parsing
# functions. You can access these functions using the 
# parsers.<function name> notation as in: 
# parsers.countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')
#import parsers.py

####################################################
# Part 1
####################################################

def populateDatabase(databaseName, wordCounts, metaData):
    # Write a function that will populate your database
    # with the contents of the word counts and us_presidents.csv
    # to your database. 
    # Inputs: A string containing the filepath to your database,
    #         A word count dictionary containing wordcounts for 
    #         each file in a directory,
    #         A metadata file containing a dictionary of data
    #         extracted from a supplemental file
    # Outputs: None
    return 0

# Test your code here
    parsers.database_gen(databaseName)
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    for file in wordCounts:
        for word in file:
            c.execute(''' INSERT INTO SOTUWordCount_DT(filename, Word, Count) values ({0},{1},{2})'''
            c.execute( '''INSERT INTO US_Presidents_DT(Index, number, start_date, end_date, president, prior) values({0},{1},{2},{3},{4},{5},{6})'''
    conn.commit() 
    conn.close()
    return 0


populateDatabase("Presidents_SOTU.db", parsers.countWordsMany("./state-of-the-union-corpus-1989-2017"), "us_presidents.csv")

####################################################
# Part 2
####################################################

def searchDatabase(databaseName, word): 
    # Write a function that will query the database to find the 
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained 
    #          the highest count of the target word
    return 0
                      
Select dictict president, word_counts, word
From "president_Speech"
Where "word" = "any_word_that_you_are_looking_for"
order by word_counts ASC


def computeLengthByParty(databaseName): 
    # Write a function that will query the database to find the 
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each 
    #          of the two major political parties.
    return 0
                    
SELECT party, Presidents, AVG(words),
FROM "president_Speech",
GROUP BY "party";