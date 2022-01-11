from webapp import create_app

app=create_app()

if __name__ == '__main__':
    app.run(debug=True)


# make your profile public 
# if profile prvate return 404
# todo: status(completed/not)

#restapi
