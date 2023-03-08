def respond(message) -> str:
    msg = message.lower()
    
    // bot responses, i plan to use csv file or whatever for this later on
    if msg == 'alpha':
        return 'Αα'
    elif msg == 'beta':
        return 'Ββ'
    elif msg == 'gamma':
        return 'Γγ'
    elif msg == 'delta':
        return 'Δδ'
    elif msg == 'epsilon':
        return 'Εε'
    elif msg == 'zeta':
        return 'Ζζ'
    elif msg == 'heta':
        return 'Ηη'
    elif msg == 'theta':
        return 'Θθ'
    elif msg == 'iota':
        return 'Ιι'
    elif msg == 'kappa':
        return 'Κκ'
    elif msg == 'lambda':
        return 'Λλ'
    elif msg == 'mu':
        return 'Μμ'
    elif msg == 'nu':
        return 'Νν'
    elif msg == 'xi':
        return 'Ξξ'
    elif msg == 'omimcron':
        return 'Οο'
    elif msg == 'pi':
        return 'Ππ'
    elif msg == 'rho':
        return 'Ρρ'
    elif msg == 'sigma':
        return 'Σσς'
    elif msg == 'tau':
        return 'Ττ'
    elif msg == 'upsilon':
        return 'Υυ'
    elif msg == 'phi':
        return 'Φφ'
    elif msg == 'chi':
        return 'Χχ'
    elif msg == 'psi':
        return 'Ψψ'
    elif msg == 'omega':
        return 'Ωω'
    elif msg == '!help':
        return 'Input a greek letter and I will provide the symbol'

    #return 'Sorry, I do not seem to know that'
