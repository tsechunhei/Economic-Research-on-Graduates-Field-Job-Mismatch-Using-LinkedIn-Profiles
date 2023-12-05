demo = read.csv("dataALL.csv")
colnames(demo)[1] = "is_Mismatch"
str(demo)
class(demo$gradYear)
demo$gradYear = factor(demo$gradYear)
table(demo$is_Mismatch)
demo$is_Changefield =NULL

#Logistic Regression Model
logit = glm(is_Mismatch ~ .,family = binomial, data= demo)
summary(logit)

vif(logit)
logit2 = glm(is_Mismatch ~ .  -gradYear -is_Law -is_Master -schoolName -schoolName -num_Exp -num_Cert -num_Volunteering +is_Law:is_Master ,family = binomial, data= demo)
summary(logit2)

logit3 = glm(is_Mismatch ~ . -is_Master ,family = binomial, data= demo)
summary(logit3)

logit4 = glm(is_Mismatch ~  is_Law ,family = binomial, data= demo)
summary(logit4)

stargazer(models,
          type =  "text",
          keep.stat = c("n", "rsq"))

stargazer(logit, probit, LPM, 
          digits = 3,
          type = "latex", 
          header = FALSE,
          se = rob_se,
          model.numbers = FALSE,
          column.labels = c("(1)", "(2)", "(3)"))


stargazer(attitude)
