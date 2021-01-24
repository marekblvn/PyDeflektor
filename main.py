from play import Play

def main():

    i = 1

    p = Play(i)

    while True:

        p.run()
        p.update()

        if p.state == "level_fin":

            i += 1

            try:

                p = Play(i)
                p.state = "ready"

            except FileNotFoundError:
            

                p.state = "end"

                i = 1

        p.clock.tick(120)




main()
