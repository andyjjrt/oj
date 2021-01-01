import argparse

from commands import login, update, submit, get

parser = argparse.ArgumentParser(
    prog="oj",
    description="CLI tool that helping you access CP Online Judge",
)
subcmd = parser.add_subparsers(dest='subcmd', help='methods', metavar='options')
subcmd.required = True

login_parser = subcmd.add_parser('login', help='Login to your oj accont')
update_parser = subcmd.add_parser('update', help='Update your contest and problem list')
submit_parser = subcmd.add_parser('submit', help='submit your hw code')
submit_parser.add_argument("assign_no", type=str, help="assignment number")
submit_parser.add_argument("file", type=str, help="code file")
get_parser = subcmd.add_parser('get', help='Get your assign sample code')
get_parser.add_argument("assign_no", type=str, help="assignment number")


args = parser.parse_args()
if args.subcmd == "login":
    login()
elif args.subcmd == "update":
    update()
elif args.subcmd == "submit":
    submit(args.assign_no, args.file)
elif args.subcmd == "get":
    get(args.assign_no)