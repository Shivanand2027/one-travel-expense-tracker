from app import app

def handler(request, context):
    return app

if __name__ == "__main__":
    app.run()
