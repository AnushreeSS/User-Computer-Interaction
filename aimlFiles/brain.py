from aiml import Kernel


def create_brain():
    kernel = Kernel()
    kernel.bootstrap(learnFiles="startup.xml", commands="load aiml b")
    kernel.saveBrain("brain.brn")


if __name__ == "__main__":
    create_brain()
