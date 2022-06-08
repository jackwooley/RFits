# RFits
RFits is a way to randomly select outfits from the existing clothes in your closet. This code currently has some clothes in it as example data, so be sure to update it with your own clothing.

The function `inmycloset()` is where you replicate your closet in R. There are 9 potential arguments; pass in a list of individual strings using R's `c()` function, i.e., `myshirts = c('blue shirt', 'white shirt', ...)`.

`ootd()` selects the *O*utfit *O*f *T*he *D*ay (hence "ootd"). It takes T/F values for each argument; pass T to indicate the clothes categories you want it to randomly select from. It won't select dirty/used clothes from some categories, since each time an outfit is generated, the used clothes are appended to the dataframe `dirty`. Exceptions are made for things like pants, jackets, and hats that can be worn multiple times without washing. It has example code demonstrating how to include logical tests to customize your outfits and avoid certain combinations. This is mainly for practicality reasons so you don't end up wearing basketball shorts and Timberlands or other questionably practical combinations of clothes. The idea behind this, though, is that RFits will pick an outfit out for you without regard for how well the clothes match, so the logical tests should be kept to a minimum in order to achieve this effect.

Running `inmycloset` will reset the closet, and erases the dataframe of dirty clothes if it exists and puts all the clothes back in their original categories.

The main script is named `bigdripgiddy2.R` as a tribute to my brother's friend who's nicknamed "Big Drip Giddy".

In the future, I'd like to remove the hard-coded logical tests from `ootd()` and make it more modular/easily customizable. Once that's done, the plan is to refactor the code in Python to make it more widely usable. Any suggestions or edits are more than welcome :)
