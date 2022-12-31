import typer

game_cli = """██╗  ██╗███████╗ █████╗ ██████╗ ████████╗██╗  ██╗███████╗████████╗ ██████╗ ███╗   ██╗███████╗     ██████╗██╗     ██╗
██║  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝    ██╔════╝██║     ██║
███████║█████╗  ███████║██████╔╝   ██║   ███████║███████╗   ██║   ██║   ██║██╔██╗ ██║█████╗█████╗██║     ██║     ██║
██╔══██║██╔══╝  ██╔══██║██╔══██╗   ██║   ██╔══██║╚════██║   ██║   ██║   ██║██║╚██╗██║██╔══╝╚════╝██║     ██║     ██║
██║  ██║███████╗██║  ██║██║  ██║   ██║   ██║  ██║███████║   ██║   ╚██████╔╝██║ ╚████║███████╗    ╚██████╗███████╗██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝     ╚═════╝╚══════╝╚═╝ 

made by rumbarum
"""

scene_welcome = """WELCOME TO HOUSE!
1. PLAY
2. EXIT
"""

scene_choose_player = """CHOOSE YOUR CHARACTER
1. JAINA
2. ...
"""


def main() -> None:
    typer.secho(game_cli)
    while True:
        if user_cmd := int(input(scene_welcome)) == 1:
            if user_cmd := int(input(scene_choose_player)) == 1:
                print("done")
                break
        else:
            break


if __name__ == "__main__":
    typer.run(main)