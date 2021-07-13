import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help='type')
parser.add_argument("--principal", type=float, help='loan', default=False)
parser.add_argument("--periods", type=int, help='months', default=False)
parser.add_argument("--payment", type=float, help='payment', default=False)
parser.add_argument("--interest", type=float, help='int')
args = parser.parse_args()
over = 0

if args.interest:

    if args.type == 'diff':
        if (args.principal and args.periods) and (args.principal > 0 and args.periods > 0):
            k = args.interest / 1200
            ans = 0
            for i in range(1, args.periods + 1):
                d = args.principal / math.ceil(args.interest) + k * (
                            args.principal - args.principal * (i - 1) / math.ceil(args.interest))
                ans += math.ceil(d)
                print('Month ' + str(i) + ': payment is ' + str(math.ceil(d)) + '\n')
            print('\n Overpayment = ' + str(math.ceil(ans) - math.ceil(args.principal)))
        else:
            print('Incorrect parameters.')


    elif args.type == 'annuity':

        i = args.interest / 1200
        if args.principal == False:
            if (args.payment and args.periods) and (args.payment > 0 and args.periods > 0):
                loan = args.payment / ((i * (i + 1) ** args.periods) / ((1 + i) ** args.periods - 1)) - 1
                print('Your loan principal = ' + str(round(loan)) + '!')
                over = args.payment * args.periods - loan
            else:
                print('Incorrect parameters.')
        if args.payment == False:
            if (args.principal and args.periods) and (args.principal > 0 and args.periods > 0):
                payment = args.principal * ((i * (i + 1) ** args.periods) / ((1 + i) ** args.periods - 1))
                print('Your monthly payment = ' + str(math.ceil(payment)) + '!')
                over = math.ceil(payment) * args.periods - args.principal
            else:
                print('Incorrect parameters.')
        if args.periods == False:
            if (args.payment and args.principal) and (args.payment > 0 and args.principal > 0):
                months = math.ceil(math.log(args.payment / (args.payment - i * args.principal), (1 + i)))
                if months > 12:
                    print(f"It will take {months // 12} years to repay this loan!" if months % 12 == 0 else
                          f"It will take {months // 12} years and {months % 12} months to repay this loan!")
                elif months == 12:
                    print(f"It will take 1 year to repay this loan!")
                else:
                    print(f"It will take 1 month to repay this loan!" if months == 1 else
                          f"It will take {months} months to repay this loan!")
                over = months * args.payment - args.principal
            else:
                print('Incorrect parameters.')
        if over > 0:
            print('\n Overpayment = ' + str(round(over)))
else:
    print('Incorrect parameters.')
