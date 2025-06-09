def register_routes(app):
    @app.get('/')
    def root():
        return {'message': 'Welcome to NOVELL v1.0'}