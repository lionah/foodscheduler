from flask import Flask


app = Flask(__name__)


def main():
    app.run()


@app.route('/')
def root():
    return "Hello World"


if __name__ == '__main__':
    main()
