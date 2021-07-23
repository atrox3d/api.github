import sys
import argparse


def get_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-user',
        '--user',
        type=str,
    )
    parser.add_argument(
        '-token',
        '--token',
        type=str,
    )
    parser.add_argument(
        '-exportfile',
        '--exportfile',
        type=str
    )
    parser.add_argument(
        '-urlapi',
        '--urlapi',
        type=str
    )
    parser.add_argument(
        '-templateurlprivate',
        '--templateurlprivate',
        type=str
    )
    parser.add_argument(
        '-templateurlpublic',
        '--templateurlpublic',
        type=str
    )
    parser.add_argument(
        '-private',
        '--private',
        type=bool,
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-public',
        '--public',
        type=bool,
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-all',
        '--all',
        type=bool,
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-printurl',
        '--printurl',
        type=bool,
        action='store_true',
        default=False
    )
    parser.add_argument(
        '-perpage',
        '--perpage',
        type=int
    )
    return parser


def parse_arguments(parser=get_parser(), args=sys.argv[1:]):
    return parser.parse_args(args)


if __name__ == '__main__':
    parser = get_parser()
    print(parser.parse_args())
    parser.print_help()
    args = parser.parse_args()
    for arg in iter(vars(args)):
        print(arg, getattr(args, arg))
    print(vars(args))
