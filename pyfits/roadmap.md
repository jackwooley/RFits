 - all the skeleton functions have their basic functionality down.
 - move the input statements to the main() function instead of each individual function?
 - another one to let you modify it if you want to (open the json and append to the keys
you want to modify)
 - main() function that will take in a firsttime/othertime/modify parameter that allows
you to create or modify the closet file if you want (or an `input()` statement with set
options)
 - tolower() the inputs, if not in a set of approved ones retry it
 - from there have three paths: an update one, a 'leave the same' one, and a first time/
reset one
 - add dirty laundry functionality
    - takes new_fit dictionary in
    - a little bit of pseudocode:
      `dirty_laundry = {}`
      `for i in new_fit.keys():`
        `dirty_laundry[i].append(new_fit[i])`
      

    - if `new_fit[category_i]` in `dirty_laundry[category]`
 - write a function for append mode that you can pass a list of clothes keys to, it'll
open the json as a dictionary, for each key in *args (? or is it **kwargs?) it'll append
values to it (something like
            for i in [keys]:
                input(f'all clothes of {i} type you want to append')
                for j in new_values: closet_dict[i].append(j))
    - new_values from input statements
