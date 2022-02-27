from flask import Flask


def init_app(app: Flask) -> None:
    from .categories_route import bp as bp_categories

    app.register_blueprint(bp_categories)

    from .simple_route import bp as bp_simple_route

    app.register_blueprint(bp_simple_route)

    from .tasks_route import bp as bp_tasks

    app.register_blueprint(bp_tasks)
