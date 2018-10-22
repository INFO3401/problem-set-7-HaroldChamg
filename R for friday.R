titanic_data <- read.csv("titanic.csv", head= TRUE, sep=",")
titanic_data
summary(titanic_data)

#Problem 6
titanic_data$Age
table(titanic_data$Sex)
table(titanic_data$Survived)
table(titanic_data$Survived, titanic_data$Sex)
names(titanic_data)

#Problem 7
prop.table(titanic_data$Survived)
prop.table(table(titanic_data$Survived,titanic_data$Age))

#Problem 8
Age <- table(titanic_data$Survived,titanic_data$Sex)
Age
prop.table(Age,1)
prop.table(Age,2)


#Problem 9

titanic_data$Age[titanic_data$Age < 18] <- 1


aggregate(Survived ~ Sex, data=titanic_data, FUN=mean)



aggregate(Survived ~ Sex, data=titanic_data, FUN=mean)

titanic_data$age<-0

titanic_data$age[titanic_data$Age < 18] <- 1


aggregate(Survived ~ age, data=titanic_data, FUN=mean)











































































































































