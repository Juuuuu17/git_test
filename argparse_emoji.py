import argparse

parser = argparse.ArgumentParser(
                    prog = 'Mon programme qui écrit un emoji',
                    description = 'Ecrit des emojis',
                    )

parser.add_argument('emoji')           # positional argument
parser.add_argument('-n', '--number',type=int, choices=range(3, 16), default=5)      # option that takes a value

args = parser.parse_args()
# print(args.emoji, args.number)

for i in range(args.number):
    print(args.emoji, end="")
    