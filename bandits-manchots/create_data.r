# Create a sample of 100 numbers which are normally distributed.
probs <- rnorm(n=100, mean=0.3, sd=0.5)
probs <- probs[probs > 0]
probs <- probs[probs < 1]

# Create a sample of 100 numbers which are uniform distributed.
# probs <- runif(n=100, min=0, max=1)

# create a data frame
data <- data.frame(Probabilities = probs)
# Write in csv file
write.csv(data, file = "./data.csv", row.names=FALSE)

