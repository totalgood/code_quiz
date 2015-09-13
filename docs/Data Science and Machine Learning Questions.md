How would you build the amazon recommendation engine?
- cluster users by their buying and browsing habits and send recommendations that they bought or viewed
- logistic regression with feature vector of demographics and amazon analytics and purchases as target/prediction

How would you build the amazon recommendation engine for anonymous user at the library?
- just straight database query of users that bought or viewed the things that you viewed, ranked by geographic similarity

What's a good distance metric for a high dimensional vector like a bag of words frequency vector or Amazon user feature vector?
- cosine distance rather than Euclidean distance (everything is far apart above a few dimensions)

What is overfitting?
- when your test set accuracy is poor but your recall (training set accuracy) is good

What is meant by the Null hypothesis?
- the opposite or absence of your hypothesis being true
- P-value measures the consistency of the null hypothesis with your experimental results so you want low p-value in order to gain confidence in your hypothesis

What is P-value?

What would your database structure be for a car that had multiple add-on features like alloy wheels that various different makes of cars might be linked too (and multiple features might be linked to the same car make and model as well).  See
