getwd()
[1] "/Users/haroldchang/Documents/GitHub/problem-set-7-HaroldChamg"
> titanic_data <- read.csv(file="titanic.csv", head= True, sep=",")
Error in read.table(file = file, header = header, sep = sep, quote = quote,  : 
  object 'True' not found
> titanic_data <- read.csv("titanic.csv", head= TRUE, sep=",")
> titanic_data
