# Create a sample of 50 numbers which are normally distributed.
probs <- rnorm(100)
probs <- probs + 0.5
probs <- probs[probs > 0]
probs <- probs[probs < 1]
data = data.frame(Probabilities = probs)
write.csv(data, file = "./data.csv", row.names=FALSE)

