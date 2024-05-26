from flask import render_template, current_app


def page_not_found(e):
    # current_app.logger.error(e)
    current_app.logger.info("===================")
    return render_template('errors/404.html', error='Error page not found'), 404