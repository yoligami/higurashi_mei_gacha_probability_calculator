import matplotlib.pyplot as plt
import numpy as np

from probability_calculator import calculate_star_six_probability, calculate_SSR_probability, calculate_SSR_probability_without_SSR_confirmed_section

def draw_star_six_possibility_line_chart():
    x = range(10, 610, 10)
    for possibility in [0.005, 0.02 / 3, 0.01]:
        y = map(lambda count: calculate_star_six_probability(count, possibility), x)
        annotate_x = 130
        annotate_y = calculate_star_six_probability(annotate_x, possibility)
        plt.plot(x, list(y), label = "probability: {:.2%}".format(possibility))
        plt.xticks(range(0, 610, 20))
        plt.yticks(np.arange(0.0, 1.0, 0.02))
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x - 130, annotate_y - 0.05 if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
        annotate_x = 300
        annotate_y = calculate_star_six_probability(annotate_x, possibility)
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x - 130, annotate_y if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
        annotate_x = 600
        annotate_y = calculate_star_six_probability(annotate_x, possibility)
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x - 130, annotate_y if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
    plt.legend()
    plt.grid(True)
    plt.show()

def draw_SSR_possibility_line_chart():
    x = range(10, 310, 10)
    for possibility in [0.005, 0.02 / 3, 0.01]:
        y = map(lambda count: calculate_SSR_probability(count, possibility), x)
        annotate_x = 30
        annotate_y = calculate_SSR_probability(annotate_x, possibility)
        plt.plot(x, list(y), label = "probability: {:.2%}".format(possibility))
        plt.xticks(range(0, 310, 10))
        plt.yticks(np.arange(0.0, 1.0, 0.02))
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x + 50, annotate_y - 0.05 if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
        annotate_x = 130
        annotate_y = calculate_SSR_probability(annotate_x, possibility)
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x - 50, annotate_y if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
        annotate_x = 300
        annotate_y = calculate_SSR_probability(annotate_x, possibility)
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x - 50, annotate_y if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
    plt.legend()
    plt.grid(True)
    plt.show()

def draw_SSR_possibility_without_SSR_confirmed_section():
    x = range(10, 310, 10)
    for possibility in [0.005, 0.02 / 3, 0.01]:
        y = map(lambda count: calculate_SSR_probability_without_SSR_confirmed_section(count, possibility), x)
        annotate_x = 10
        annotate_y = calculate_SSR_probability_without_SSR_confirmed_section(annotate_x, possibility)
        plt.plot(x, list(y), label = "probability: {:.2%}".format(possibility))
        plt.xticks(range(0, 310, 10))
        plt.yticks(np.arange(0.0, 1.0, 0.02))
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x + 50, annotate_y - 0.05 if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
        annotate_x = 100
        annotate_y = calculate_SSR_probability_without_SSR_confirmed_section(annotate_x, possibility)
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x - 50, annotate_y if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
        annotate_x = 300
        annotate_y = calculate_SSR_probability_without_SSR_confirmed_section(annotate_x, possibility)
        plt.annotate('{}: {:.2%}'.format(annotate_x, annotate_y),
                     xy=(annotate_x, annotate_y), xytext=(annotate_x - 50, annotate_y if possibility == 0.005 else annotate_y + 0.05),
                     arrowprops = dict(facecolor ='green',shrink = 0.05))
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    draw_star_six_possibility_line_chart()
    draw_SSR_possibility_line_chart()
    draw_SSR_possibility_without_SSR_confirmed_section()
