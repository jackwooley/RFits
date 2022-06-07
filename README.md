# RFits
RFits is a way to randomly select outfits from the existing clothes in your closet. This code currently has all my clothes in it lol so if you'd like to use it, you'll need to update it with your clothing.

The function `inmycloset()` is where you replicate your closet in R. There are 9 potential arguments; pass in a list of individual strings using R's `c()` function, i.e., `myshirts = c('blue shirt', 'white shirt', ...).

`ootd()` selects the *O*utfit *O*f *T*he *D*ay (hence "ootd"). It takes T/F values for each argument; pass T to indicate the clothes categories you want it to randomly select from. It generally won't select dirty/used clothes, since each time an outfit is generated, the used clothes are appended to the dataframe `dirty`. Exceptions are made for things like pants, jackets, and hats that can be worn multiple times without washing. 

Running `inmycloset` will reset the closet, and erases the dataframe of dirty clothes if it exists and puts all the clothes back in their original categories. 
