            if i in opponent.indexes:
                player.search[i] = "H"


                #check if ship is sunk
                for ship in opponent.ships:
                    sunk = True
                    for i in ship.indexes:
                        if player.search[i] == "U":
                            sunk = False
                            break
                    if sunk:
                        for i in ship.indexes:
                            player.search[i] = "S"
                
            else: 
                player.search[i] = "M"
            
            #check if game over
            #class Game: self.result = None
            game_over = True
            for i in opponent.indixes:
                if player.search[i] == "U":
                    game_over = False
            self.over = game_over
            self.result = 1 if self.player1_turn else 2

#############################GUI#################################

        if game.over:
            text ="player " + str(game.result)