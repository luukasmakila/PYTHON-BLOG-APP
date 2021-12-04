from website import create_app

#run this file to start the website

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)