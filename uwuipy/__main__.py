from uwuipy import Uwuipy
from os import getenv
import argparse


try:
    import readline

except:
    pass


def main():
    parser = argparse.ArgumentParser(
        prog="uwuipy",
        description="UwUiPy uwuifies text. Runs a REPL if there is no message specified at CLI",
    )

    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=None,
        help="The seed used to randomize the following factors. [default: current timestamp]",
    )

    parser.add_argument(
        "-S",
        "--stutterchance",
        type=float,
        default=0.1,
        help="The chance of adding a stutter. [default: 0.1]",
    )

    parser.add_argument(
        "-f",
        "--facechance",
        type=float,
        default=0.05,
        help="The chance of appending a face. [default: 0.05]",
    )

    parser.add_argument(
        "-a",
        "--actionchance",
        type=float,
        default=0.075,
        help="The chance of appending an action. [default: 0.075]",
    )

    parser.add_argument(
        "-e",
        "--exclamationchance",
        type=float,
        default=1,
        help="The chance of replacing ! with an exclamation. [default: 1]",
    )

    parser.add_argument(
        "-n",
        "--nsfwactions",
        default=False,
        action="store_true",
        help="Enable NFSW actions. [default: False]",
    )

    parser.add_argument(
        "-p",
        "--power",
        default=3,
        type=int,
        help="The uwuification strength. [default: 3 — max is 4]",
    )

    parser.add_argument("message", nargs=argparse.REMAINDER, help="The text to uwuify")
    args = parser.parse_args()

    uwu = Uwuipy(
        args.seed,
        args.stutterchance,
        args.facechance,
        args.actionchance,
        args.exclamationchance,
        args.nsfwactions,
        args.power,
    )

    if len(args.message):
        print(uwu.uwuify(" ".join(args.message)))
        return

    while True:
        try:
            print(uwu.uwuify(input(getenv("PS2", ">>> "))))

        except (EOFError, OSError, KeyboardInterrupt):
            break


if __name__ == "__main__":
    main()
