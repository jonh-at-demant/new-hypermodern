import nox


@nox.session(python=["3.8", "3.6"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")