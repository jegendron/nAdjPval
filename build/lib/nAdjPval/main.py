
#%%########################################################################
# nAdjPval PYTHON PACKAGE
###########################################################################

# Now my software package will convert the p-values
    # INPUT: Regression results (reg1)
    # OUTPUT: Table of p-values


def nAdjPval(reg1):
    try:
        import numpy as np
        import scipy.stats       
        import pandas as pd
        pd.options.mode.chained_assignment = None  # default='warn'



        # Extract original n
        n1 = int(reg1.nobs)
        
        if(n1<=100):
            print()
            print("------------------------------------")
            print("n <= 100, n-Adjustment inappropriate")
            print("====================================")
            print()
        
        else:    
            # Extract original t-scores for ALL variables
            temp2 = reg1.tvalues
            oldTs = temp2.to_frame(name="t")
            #oldTs = oldTs.rename(columns={"index": "Variables"},  inplace=True)
            oldTs = oldTs.reset_index()
            
            
            
            # Extract the number of variables (will be used for d.f.)
            numVars = len(temp2)-1
            
            # Here we're going to change the t-score to if the sample was 100 (i.e. NOT overpowered)
            n2 = 100
            
            # Calculates the difference in the t-score (solely driven by sample size)
            percDiff = np.sqrt(n2)/np.sqrt(n1)
            
            # Pull original p-values, replace with new p-values
            temp1 = reg1.pvalues
            newPvals = temp1.to_frame(name="p-Values")
            newPvals = newPvals.reset_index()
            
            # This generates the n-adjusted p-values from the t-scores and d.f.
            for i in oldTs.index:
                tStat2 = oldTs['t'][i]*percDiff
                newPvals['p-Values'][i] = scipy.stats.t.sf(abs(tStat2), df=n2-numVars-1)*2
            
            
            
            ### This prints the n-adjusted p-values    
                # Ref: https://www.educba.com/python-print-table/
            
            print()
            print("------------------------------------------------------------------------------")
            print("n-Adjusted P-Values")
            print()
            
            for i in newPvals.index:
                if(newPvals['p-Values'][i]<=0.01):            
                    print("{:<10} {:<10}".format(newPvals['index'][i],str(round(newPvals['p-Values'][i],5))+"***"))
                elif(newPvals['p-Values'][i]<=0.05):            
                    print("{:<10} {:<10}".format(newPvals['index'][i],str(round(newPvals['p-Values'][i],5))+"**"))
                elif(newPvals['p-Values'][i]<=0.1):            
                    print("{:<10} {:<10}".format(newPvals['index'][i],str(round(newPvals['p-Values'][i],5))+"*"))
                else:
                    print("{:<10} {:<10}".format(newPvals['index'][i],str(round(newPvals['p-Values'][i],5))))
            
            print()
            print("*** WARNING: This assumes the mean and standard error are the same! ***")
            print()
            print("==============================================================================")
            print()
            
            my_df=newPvals.copy()
            my_df.columns.values[0] = "Variables"
            return(my_df)
    
    except AttributeError:
        print("Incorrect input type.")
        print("Please ensure you are inputting 1 regression result (i.e: input = sm.OLS(y, X).fit())")
        print()

    except TypeError:
        print("Correct input type, but incorrect amount of inputs.")
        print("Please ensure you are only inputting 1 regression result (i.e: input = sm.OLS(y, X).fit())")
        print()

    #except:
    #    print("Please ensure you are only inputting 1 regression result (i.e: input = sm.OLS(y, X).fit())")

#%%

#df = nAdjPval(reg1)



################################################################################
### DEBUGGING
################################################################################

# Successful Exceptions
# df = nAdjPval("Hi")
# df = nAdjPval(1)
# df = nAdjPval(None)

# Exceptions that are NOT caught, BUT will show an easy to understand error
    # https://stackoverflow.com/questions/62313554/try-except-doesnt-catch-typeerror-in-python#:~:text=Its%20because%202%20positional%20arguments,exception%20handler%20is%20not%20envolved.

# df = nAdjPval(reg1,reg1)
# df = nAdjPval()
