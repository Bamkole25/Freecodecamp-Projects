# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
def player(prev_play, opponent_history=[], play_record={}):
  #the record of the last five opponent plays is saved in play_record
    if not prev_play:
        prev_play = 'R' #first move is rock since we don't know our opponent play yet

    opponent_history.append(prev_play)
    prediction = 'P' #plays Paper constantly till enough data of atleast five moves is gotten 

    if len(opponent_history) > 4:
      #fill the play record with the last five moves
        last_five = "".join(opponent_history[-5:])
        play_record[last_five] = play_record.get(last_five, 0) + 1
        
        # A list of every possible play that can be played by the opponent
        #This is done by looking at the last four moves and making a guess of the next move based on what has been seen before
        possible_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

        sub_order = {
            k: play_record[k]
            for k in possible_plays if k in play_record
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]