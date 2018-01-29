from fabric.api import env, cd, local, run

# nombre de la máquina de producción
env.hosts = ["cloud"]
# env.user
# env.password


def deploy():
    local("git push")
    with cd("~/mkdocs"):
        run("git pull")
        run("cd my-project && source /home/alu5896/.virtualenvs/mkdocs/bin/activate && mkdocs build")
