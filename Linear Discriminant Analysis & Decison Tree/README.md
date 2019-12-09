# Linear Discriminant Analysis 

Linear Discriminant Analysis (LDA) is a dimensionality reduction technique. As the name implies dimensionality reduction
techniques reduce the number of dimensions (i.e. variables) in a dataset while retaining as much information as possible. Linear discriminant analysis, normal discriminant analysis (NDA), or discriminant function analysis is a generalization of Fisher's linear discriminant, a method used in statistics, pattern recognition, and machine learning to find a linear combination of features that characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier, or, more commonly, for dimensionality reduction before later classification. In our case, LDA was leveraged to project our data onto a new space, spanned by the first two LDA eigenvectors, in order to seperate in a better way the diffent wine classes. Both LDA eigenvectors are fitted a decision tree, which classify any wine in three categories (CLass 1, Class 2, Class 3) with 100 % accuracy.

![image](https://user-images.githubusercontent.com/25617530/70447989-55879c00-1aa8-11ea-8743-503ae53186aa.png)


Result: 

![image](https://user-images.githubusercontent.com/25617530/70447707-dbefae00-1aa7-11ea-9416-bd788971cbc6.png)


