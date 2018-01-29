from fabric.api import env, cd, local, run

# nombre de la máquina de producción
env.hosts = ["cloud"]
# env.user
# env.password


def deploy():
    local("git push")
    with cd("~/mkdocs"):
        run("git pull")
        run("source /home/alu5896/.virtualenvs/mkdocs/bin")
        run("cd my-project")
        run("mkbuild")
