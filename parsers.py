################################################################################
# PART #1
################################################################################


# Cooperated with Lucas, Annastasia, Steve, and Marrissa
import string
import os
from os import listdir
import csv
import json



def countWordsUnstructured(filename):
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    
    # Test your part 1 code below.
    wordCounts={}
    datafile = open(filename)
    for word in datafile.read().split():
        for mark in string.punctuation:
                word = word.replace(mark,"")
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts [word] =+ 1

    return wordCounts
countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1990.txt')

################################################################################
# PART 2
################################################################################
    
def generateSimpleCSV(targetfile, wordCounts): 
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
   
    with open (targetfile, "w") as csv_file:
         
        write = csv.writer(csv_file)
         
        write.writerow(['Word', 'Word_Count'])
       
        for key,value in wordCounts.items():
            write.writerow([key,value])
    
    csv_file.close()
     
    return csv_file
    
# Test your part 2 code belo
    
    
generateSimpleCSV("targetfile.csv", countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt'))

################################################################################
# PART 3
################################################################################
def countWordsMany(directory): 
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each text file in the directory
    
# Test your part 3 code below

    list = listdir(directory)
    countdict = {}
    for file in list:
        All_WC = countWordsUnstructured(directory + '/' +file)
        countdict[file] = All_WC
    return countdict
All_WC_DIC = countWordsMany('./state-of-the-union-corpus-1989-2017')
#print(All_WC_DIC)

    

################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile): 
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
# Test your part 4 code below
    #CSVfile=open(targetfile, 'w')
    #CSVfile.write("filename, Word, Count\n")
    #for wordfile, dict in wordCounts.items():
        #for word, count in dict.items():
            #CSVfile.write(wordfile + "," + str(word) + #","+str(count)+"\n")
        #CSVfile.close()
        #return CSVfile
    with open (targetfile, 'w') as csv_file:
        
        write = csv.writer(csv_file)
        
        write.writerow(['Filename', 'Word', 'Word_Count'])
        
        for key,value in wordCounts.items():
            write.writerow([key,value])
            
    csv_file.close()
     
    return csv_file

generateDirectoryCSV(All_WC_DIC, "targetfile2.csv")
    
################################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile): 
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    
# Test your part 5 code below
    JS = open(targetfile,'w')
    JS.write(str(wordCounts).replace("\'","\""))
    JS.close()
    return JS
generateJSONFile(All_WC_DIC, "JS_TARGETFILE.json")
################################################################################
# PART 6
def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word

    largest_file = ""
    largest_count = 0
    with open(csvfile) as csv_file:
        file_read = csv.reader(csv_file)
        for line in file_read:
            if line[1] == word and int(line[2]) > largest_count:
                largest_count = int(line[2])
                largest_file = line[0]
    csv_file.close()
    return largest_file

## change the name of the word
print(searchCSV("targetfile2.csv", "That"))

    
def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# Test your part 6 code to find which file has the highest count of a given word

    largest_file = ""
    largest_count = 0
    processed = 0
    with open(JSONfile) as json_file:
        read_data = json.load(json_file)
        for file in read_data:
            processed += 1
            if word in read_data[file] and read_data[file][word] > largest_count:
                largest_count = read_data[file][word]
                largest_file = file
        json_file.close()
    return largest_file

## change the name of the word
print(searchJSON("JS_TARGETFILE.json", "That"))


#Problem 7



#import sqlite3

#Table 1:  "word_Counts"

    #Column 1: "file_name" text
    #Column 2: "word" text
    #Column 3: "word_count" Integer
    

#Table 2:  "US_Presidents"

    #Column 1: "name" text
    #Column 2: "word" text
    #Column 3: "word_count" Integer
    #Column 4: "year" Integer
    #Column 5: "gender" Integer
    
    
    





#conn = sqlite3.connect('presidents_speech.db')
#c = conn.cursor()

#c.execute('''(CREATE TABLE word_Counts (file_name, word , word_count )''')

#c.execute('''(CREATE TABLE US_Presidents (name, word , word_count,year,gender )''')

#conn.commit()
        
# Close the connection
#conn.close()