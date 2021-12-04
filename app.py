from website import create_app

#run this file to start the website

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)