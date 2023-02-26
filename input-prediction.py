import argparse

parser = argparse.ArgumentParser()

# Take in 6 argeumets from the user
parser.add_argument("name", help="Your name")
parser.add_argument("first", help="First place")
parser.add_argument("second", help="Second place")
parser.add_argument("third", help="Third place")
parser.add_argument("fourth", help="Fourth place")
parser.add_argument("fifth", help="Fifth place")
parser.add_argument("sixth", help="Sixth place")

args = parser.parse_args()

echo = f"Your predictions are: {args.first}, {args.second}, {args.third}, {args.fourth}, {args.fifth}, {args.sixth}"
print(echo)

