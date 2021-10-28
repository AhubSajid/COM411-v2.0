def steps():
    likelihoods = [("step 1", 50), ("step2", 38), ("step3", 27), ("step4" , 99), ("step5", 4)]
    return likelihoods

def run():
    foundlist = steps()
    good_steps = []
    bad_steps = []
    for step in foundlist:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)
    print(len(good_steps))
    print(len(bad_steps))

run()