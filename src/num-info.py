from phonenumbers.phonenumberutil import is_valid_number
from phonenumbers import parse
import lookups
import auxillary
import argparse

# default browser is chrome, can be set to firefox via command line args
global person_lookups
person_lookups = None

# sets parameters on the basis of command line args

# executes only if being executed via this file (not as a module)
if __name__ == "__main__":

    # create the parser
    parser = argparse.ArgumentParser(
        description="an OSINT based tool to perform phone number lookups",
    )

    # add arguments
    parser.add_argument(
        "-b",
        "--browser",
        type=str,
        choices=["chrome", "firefox"],
        default="chrome",
        help="set the browser",
    )
    parser.add_argument(
        "-e", "--serve", help="use the web-UI.", action="store_true", default=None
    )
    parser.add_argument("-s", "--scan", type=str, default=None)

    # parse the arguments
    args = parser.parse_args()

    browser = args.browser

    web_ui = args.serve
    string_no = args.scan

    person_lookups = lookups.Lookups()

    # if CLI
    if string_no and (not web_ui):
        if len(string_no) > 10:
            if (
                not (string_no.startswith("+") and string_no[1:].isdigit())
                or string_no.isdigit()
            ):
                auxillary.exit_condition()
            else:
                # methods to be called in case of CLI interface
                person_lookups.display_logo()
                person_lookups.set_browser(browser)
                person_lookups.set_number(string_no)
                person_lookups.processes()
                person_lookups.display_results()
        else:
            auxillary.exit_condition()

    # if Web-UI
    elif web_ui and (not string_no):
        person_lookups.display_logo()
        person_lookups.set_web_ui()
        from flask import (
            Flask,
            redirect,
            url_for,
            render_template,
            request,
            session,
        )

        # initiating the flask app
        app = Flask(__name__)

        # not necessary (just there)
        app.secret_key = "hello"

        # '/' indicates default domain (home page)
        @app.route("/", methods=["POST", "GET"])
        # backend for home page (index.html)
        def home():
            if request.method == "POST":
                string_number = request.form["name_input_number"]
                session["string_no"] = string_number
                checked_truecaller = request.form.getlist("name_truecaller_lookup")
                session["truecaller_flag"] = checked_truecaller
                checked_phndir = request.form.getlist("name_phndir_lookup")
                session["phndir_flag"] = checked_phndir

                # in case of truecaller lookup, since microsoft account is required and the details are to be entered in the web ui,
                # i.e. the home page, the details have to be passed to the truecaller lookup function from this page itself
                if session["truecaller_flag"] == ["checked"]:
                    person_lookups.microsoft_flag = "y"
                    microsoft_outlook_email_address = request.form["uname"]
                    session["your_email_id"] = microsoft_outlook_email_address
                    microsoft_outlook_password = request.form["pwsd"]
                    session["your_password"] = microsoft_outlook_password
                    person_lookups.set_microsoft_details(
                        session["your_email_id"], session["your_password"]
                    )
                else:
                    person_lookups.microsoft_flag = "n"

                if checked_phndir:
                    person_lookups.phndir_scan_flag = "y"
                else:
                    person_lookups.phndir_scan_flag = "n"

                # redirected to the processes page that conveys that the processes are taking place
                return redirect(url_for("ongoing"))
            else:
                return render_template("index.html")

        @app.route("/processing")
        # backend for processes page
        # NOTE: browser must be chosen only via the command-line-arguments
        def ongoing():
            string_no = session["string_no"]
            if len(string_no) <= 10:
                return redirect(url_for("incorrect_input"))
            if len(string_no) == 11 and string_no.startswith("+"):
                return redirect(url_for("incorrect_input"))

            phone_number = parse(string_no)

            # in case of invalid phone number, user gets redirected to the error page
            if not is_valid_number(phone_number):
                return redirect(url_for("incorrect_input"))

            person_lookups.set_browser(browser)
            person_lookups.set_number(session["string_no"])
            person_lookups.processes()
            person_lookups.set_results()
            return redirect(url_for("outcome"))

        # backend for error page (user gets redirected in case of erroneus user input)
        @app.route("/error")
        def incorrect_input():
            return render_template("error.html")

        # backend for results page
        # upon successful lookups, the corresponding lookup results are displayed in the results page
        @app.route("/results")
        def outcome():
            results = person_lookups.get_results()
            return render_template("results.html", results=results)

        # method to run the app
        # optional parameters:
        # debug: Default value -> False
        # port: Default value -> 5000 (not recommended to change it which is why option to change port no. isn't provided in the tool at the first place)
        app.run()
