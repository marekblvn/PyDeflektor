from play import Play

if __name__ == "__main__":

    i = 1

    p = Play(i)

    while True:

        p.run()
        p.update()

        if p.state == "level_fin":

            if i < p.level.max_level:

                i += 1

                p = Play(i)
                p.state = "ready"


            elif i >= p.level.max_level:

                p.state = "end"

                i = 1

        p.clock.tick(120)

