# calculate the probability of the selected SSR in actual rolls.
# To make things easier, here are some extra settings.
# 1. I would only count the 10 rolls since it is relatively rare to use
# a single roll in the gacha.
# 2. I would only calculate the possiblity of "get the SSR" and 
# "get the star 6 SSR", these are the number people mainly concerned.
# 3. In higurashi mei, we have 3 different gacha arrangements:
# normal one, the steps one, and the SSR confirmed one.
# By default, I would set the star 6 SSR as "SSR confirmed -> step -> normal"
# For "get the SSR", I would also count the case where SSR confirmed is not used.

from ten_rolls_calculator import one_output_possibility_SSR_confirmed, one_output_possibility_regular, other_output_possibility, zero_output_possibility_SSR_confirmed, zero_output_possibility_regular

def number_of_SSR_rolls_and_normal_rolls(number_of_rolls):
    if number_of_rolls >= 130:
        return [5, number_of_rolls // 10 - 5]
    elif number_of_rolls >= 80:
        return [4, number_of_rolls // 10 - 4]
    elif number_of_rolls >= 30:
        return [3, number_of_rolls // 10 - 3]
    else:
        return [number_of_rolls // 10 , 0]

def number_of_SSR_rolls_and_normal_rolls_without_SSR_confirmed_gacha(number_of_rolls):
    if number_of_rolls >= 100:
        return [2, number_of_rolls // 10 - 2]
    elif number_of_rolls >= 50:
        return [1, number_of_rolls // 10 - 1]
    else:
        return [0, number_of_rolls // 10]

def facotrical_calculator_array(number):
    result = [1] * (number + 1)
    for x in range(1, number + 1):
        result[x] = result[x - 1] * x
    return result

def SSR_confirmed_gacha_probability_calculator(single_roll_possibility, number_of_SSR_rolls):
    result = [0] * 4
    facotrical_array = facotrical_calculator_array(number_of_SSR_rolls);
    zero_count_possibility = zero_output_possibility_SSR_confirmed(single_roll_possibility)
    one_count_possibility = one_output_possibility_SSR_confirmed(single_roll_possibility)
    two_count_possibility = other_output_possibility(2, single_roll_possibility)
    three_count_possibility = other_output_possibility(3, single_roll_possibility)
    for single_count in range(4): # single selected SSR appeared count in 10 rolls
        for double_count in range(2): # double selected SSR appeared count in ten rolls
            for triple_count in range(2): # triple selected SSR appeared count in ten rolls
                zero_count = number_of_SSR_rolls - single_count - double_count - triple_count
                total_SSR_counts = single_count + double_count * 2 + triple_count * 3
                if total_SSR_counts >= 4 or zero_count < 0:
                    continue
                result[total_SSR_counts] += (facotrical_array[number_of_SSR_rolls] // \
                    facotrical_array[single_count] // facotrical_array[double_count] // \
                        facotrical_array[triple_count] // facotrical_array[zero_count]) * \
                            zero_count_possibility ** zero_count * one_count_possibility ** \
                                single_count * two_count_possibility ** double_count * \
                                    three_count_possibility ** triple_count
    
    return result

def regular_gacha_probability_calculator(single_roll_possibility, number_of_regular_rolls):
    result = [0] * 4
    facotrical_array = facotrical_calculator_array(number_of_regular_rolls);
    zero_count_possibility = zero_output_possibility_regular(single_roll_possibility)
    one_count_possibility = one_output_possibility_regular(single_roll_possibility)
    two_count_possibility = other_output_possibility(2, single_roll_possibility)
    three_count_possibility = other_output_possibility(3, single_roll_possibility)
    for single_count in range(4): # single selected SSR appeared count in ten rolls
        for double_count in range(2): # double selected SSR appeared count in ten rolls
            for triple_count in range(2): # triple selected SSR appeared count in ten rolls
                zero_count = number_of_regular_rolls - single_count - \
                    double_count - triple_count
                total_SSR_counts = single_count + double_count * 2 + triple_count * 3
                if total_SSR_counts >= 4 or zero_count < 0:
                    continue
                result[total_SSR_counts] += (facotrical_array[number_of_regular_rolls] // \
                    facotrical_array[single_count] // facotrical_array[double_count] // \
                        facotrical_array[triple_count] // facotrical_array[zero_count]) * \
                            zero_count_possibility ** zero_count * one_count_possibility ** \
                                single_count * two_count_possibility ** double_count * \
                                    three_count_possibility ** triple_count
                            
    return result

def calculate_star_six_probability(number_of_rolls, single_roll_possibility):
    [number_of_SSR_rolls, number_of_normal_rolls] = \
        number_of_SSR_rolls_and_normal_rolls(number_of_rolls)
    unable_to_get_star_six_probability = 0
    SSR_confirmed_gacha_probability_array = \
        SSR_confirmed_gacha_probability_calculator(single_roll_possibility, number_of_SSR_rolls)
    regular_gacha_probability_array = \
        regular_gacha_probability_calculator(single_roll_possibility, number_of_normal_rolls)

    for x in range (0, 4):
        for y in range (0, x + 1):
            SSR_rolls_count, regular_rolls_count = y, x - y
            unable_to_get_star_six_probability += \
                SSR_confirmed_gacha_probability_array[SSR_rolls_count] * \
                    regular_gacha_probability_array[regular_rolls_count]
    
    return 1 - unable_to_get_star_six_probability

def calculate_SSR_probability(number_of_rolls, single_roll_possibility):
    [number_of_SSR_rolls, number_of_normal_rolls] = \
        number_of_SSR_rolls_and_normal_rolls(number_of_rolls)
    SSR_confirmed_gacha_probability_array = \
        SSR_confirmed_gacha_probability_calculator(single_roll_possibility, number_of_SSR_rolls)
    regular_gacha_probability_array = \
        regular_gacha_probability_calculator(single_roll_possibility, number_of_normal_rolls)
    
    unable_to_get_SSR_probability = \
        SSR_confirmed_gacha_probability_array[0] * regular_gacha_probability_array[0]

    return 1 - unable_to_get_SSR_probability 

def calculate_SSR_probability_without_SSR_confirmed_section(number_of_rolls, single_roll_possibility):
    [number_of_SSR_rolls, number_of_normal_rolls] = \
        number_of_SSR_rolls_and_normal_rolls_without_SSR_confirmed_gacha(number_of_rolls)
    SSR_confirmed_gacha_probability_array = \
        SSR_confirmed_gacha_probability_calculator(single_roll_possibility, number_of_SSR_rolls)
    regular_gacha_probability_array = \
        regular_gacha_probability_calculator(single_roll_possibility, number_of_normal_rolls)
    
    unable_to_get_SSR_probability = \
        SSR_confirmed_gacha_probability_array[0] * regular_gacha_probability_array[0]

    return 1 - unable_to_get_SSR_probability

def main_function():
    for x in [0.005, 0.02 / 3, 0.01]:
        print("current single roll possibility: %.5f" % x)
        for y in range(10, 910, 10):
            print('current number of rolls: %3d' % y)
            if y <= 300:
                print('possibility to get SSR without SSR confirmed section: {:.10f}'.format(
                    calculate_SSR_probability_without_SSR_confirmed_section(y, x))
                )
                print('possibility to get SSR: {:.10f}'.format(
                    calculate_SSR_probability(y, x))
                )
            print('possibility to get star 6 SSR: {:.10f}'.format(
                calculate_star_six_probability(y, x))
            )

if __name__ == '__main__':
    main_function()
