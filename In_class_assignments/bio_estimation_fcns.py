# Biogeme
import biogeme.biogeme as bio
from biogeme import models
from biogeme.expressions import log, exp, bioMultSum, exp,PanelLikelihoodTrajectory

def estimate_mnl(V, AV, CHOICE, database, model_name):
    '''
    Function to estimate the MNL model

    Parameters:
    V: a dictionary containing the utility functions for each alternative
    AV: a dictionary containing availability conditions
    CHOICE: an integer containing the choice variable
    database: database object
    model_name: name of the model

    Returns:
    results: estimation results
    '''

    # Define the choice model: The function models.logit() computes the MNL choice probabilities of the chosen alternative given the V. 
    prob = models.logit(V, AV, CHOICE)

    # Define the log-likelihood by taking the log of the choice probabilities of the chosen alternative
    LL = log(prob)
   
    # Create the Biogeme object containing the object database and the formula for the contribution to the log-likelihood of each row using the following syntax:
    biogeme = bio.BIOGEME(database, LL)
    
    # The following syntax passes the name of the model:
    biogeme.modelName = model_name

    # Some object settings regaridng whether to save the results and outputs 
    biogeme.generate_pickle = False
    biogeme.generate_html = False
    biogeme.save_iterations = False

    # Syntax to calculate the null log-likelihood. The null-log-likelihood is used to compute the rho-square 
    biogeme.calculate_null_loglikelihood(AV)

    # This line starts the estimation and returns the results object.
    results = biogeme.estimate()
     
    return results


def estimate_LC(V, AV, nu, CHOICE, database,model_name):
    
    '''
    Function to estimate the LC models

    Parameters:
    V: a list of dictionaries containing the utility functions for each class
    AV: a dictionary containing availability conditions
    nu is a list of value function for the class membership model
    CHOICE: choice variable
    database: database object
    model_name: name of the model

    Returns:
    results: estimation results
    '''
    # Determine the number of classes
    n_classes = len(V)

    # Compute the probabilities of the chosen alternative conditional the class
    prob = []
    for i in range(n_classes):
        prob.append(models.logit(V[i], AV, CHOICE))
        
    # Compute likelihood of the sequence of choices for each individual, conditional on the class
    Pseq = []
    for i in range(n_classes):
        Pseq.append(PanelLikelihoodTrajectory(prob[i]))

    # Compute class membership probabilities for each individual using the value function nu 
    P_class = {k: models.logit({j: nu[j] for j in range(n_classes)}, None, k) for k in range(n_classes)}
    
    # Compute the unconditional likelihood of the sequence of choices for each individual
    Prob_indiv = bio.bioMultSum([P_class[i] * Pseq[i] for i in range(n_classes)])
    
    # Take the log of the likelihood function and sum over all individuals
    LL = log(Prob_indiv)

    # Create the Biogeme object containing the object database and the formula for the contribution to the log-likelihood of each row using the following syntax:
    biogeme = bio.BIOGEME(database, LL)

    # The following syntax passes the name of the model:
    biogeme.modelName = model_name

    # Some object settings regaridng whether to save the results and outputs 
    biogeme.generate_pickle = False
    biogeme.generate_html   = False
    biogeme.save_iterations = False

    # Syntax to calculate the null log-likelihood. The null-log-likelihood is used to compute the rho-square 
    biogeme.calculate_null_loglikelihood(AV)

    # This line starts the estimation and returns the results object.
    results = biogeme.estimate()
    return results


def print_results(results):
    
    # Print the estimation statistics
    print(results.short_summary())

    # Get the model parameters in a pandas table and  print it
    beta_hat = results.get_estimated_parameters()
    
    # Round the results to suitable decimal places
    beta_hat = beta_hat.round(4)
    beta_hat['Rob. t-test']  = beta_hat['Rob. t-test'].round(2)
    beta_hat['Rob. p-value'] = beta_hat['Rob. p-value'].round(2)
    print(beta_hat)