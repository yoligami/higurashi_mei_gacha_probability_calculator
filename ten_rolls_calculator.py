# calulate the possibility of SSR you want, in different numbers
# for a single 10 draw.

def zero_output_possibility_regular(single_roll_possibility):
    without_special_treat = ((1 - single_roll_possibility) ** 9 - 0.75 ** 9) * \
        (1 - single_roll_possibility)
    with_special_treat = 0.75 ** 9 * (1 - single_roll_possibility * 4)
    return without_special_treat + with_special_treat

def zero_output_possibility_SSR_confirmed(single_roll_possibility):
    without_special_treat = ((1 - single_roll_possibility) ** 9 - 0.95 ** 9) * \
        (1 - single_roll_possibility)
    with_special_treat = 0.95 ** 9 * \
        ((0.05 - single_roll_possibility) / 0.05)
    return without_special_treat + with_special_treat

def one_output_possibility_regular(single_roll_possibility):
    appeared_in_first_nine_possibility = (1 - single_roll_possibility) ** 9 \
        * single_roll_possibility * 9
    appeared_in_last_with_speical_treat = 0.75 ** 9 * single_roll_possibility \
        * 4
    appeared_in_last_without_special_treat = \
        (((1 - single_roll_possibility) ** 9) - 0.75 ** 9) * single_roll_possibility
    return appeared_in_first_nine_possibility + appeared_in_last_with_speical_treat \
        + appeared_in_last_without_special_treat

def one_output_possibility_SSR_confirmed(single_roll_possibility):
    appeared_in_first_nine_possibility = (1 - single_roll_possibility) ** 9 \
        * single_roll_possibility * 9
    appeared_in_last_with_speical_treat = 0.95 ** 9 \
        * (single_roll_possibility / 0.05)
    appeared_in_last_without_special_treat = \
        (((1 - single_roll_possibility) ** 9) - 0.95 ** 9) * single_roll_possibility
    return appeared_in_first_nine_possibility + appeared_in_last_with_speical_treat \
        + appeared_in_last_without_special_treat

def other_output_possibility(output_times, single_roll_possibility):
    times_appearing = 1
    for x in range(1, output_times + 1):
        times_appearing = times_appearing * (11 - x) / x
    return (single_roll_possibility ** output_times) * \
        ((1 - single_roll_possibility) ** (10 - output_times)) * times_appearing

def calculate_possiblity(output_times, single_roll_possibility, need_special_treat):
    if output_times == 0:
        return zero_output_possibility_SSR_confirmed(single_roll_possibility) \
            if need_special_treat else \
                zero_output_possibility_regular(single_roll_possibility)
    elif output_times == 1:
        return one_output_possibility_SSR_confirmed(single_roll_possibility) \
            if need_special_treat else \
                one_output_possibility_regular(single_roll_possibility)
    else:
        return other_output_possibility(output_times, single_roll_possibility)

if __name__ == '__main__':
    for x in [0.005, 0.02 / 3, 0.01, 0.02]:
        print("current single roll possibility: %.5f" % x)
        for y in range(0, 11):
            print("number of SSR %2d" % y)
            print("probability with SSR confimed 10 rools: %.10f" % \
                calculate_possiblity(y, x, True))
            print("probability with regular 10 rools: %.10f" % \
                calculate_possiblity(y, x, False))