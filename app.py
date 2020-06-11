import constants
import copy

    
teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)


y = players

user_input1 = 1

user_input2 = 2

user_input3 = 3


for char in y:
    char['height'] = char['height'].replace(' inches', '')
    char['height'] = int(char['height'])


for char in y:
    char['guardians'] = char['guardians'].replace(" and ", ', ')
    char['guardians'] = ''.join(char['guardians'])




for player in players:
    if player['experience'] == 'YES':
        player['experience'] = True

    else:
        player['experience'] = False
        

def start():

    while True:
        try:
            print('\nHere are your choices: \n1) Display Team Stats \n2) Quit')
            option1 = int(input('\nEnter an option > ')) 
            if option1 == user_input1:
                for index, i in enumerate(teams, 1):
                    print (index, i)
                    continue
    
            elif option1 == user_input2:
                print ('\nThank you and Goodbye ')
                exit()
                
            elif option1 > user_input2:
                print('\nPlease enter a number between 1 & 2 ')
                continue
                
            elif option1 < user_input2:
                print('\nPlease enter a number between 1 & 2 ')
                continue
                
            option2 = int(input('\nChoose a team > '))     
            total_players = int(len(players) / len(teams))
            
            
            pn = 0
            player_names = []
            
            hl = 0
            heights_list = []
            
            pe=0
            players_experience = []
            
            gl=0
            guardians_list = []
            
            while option2 == user_input1:
                
                player_names.append(players[pn]['name'])
                pn += 1
            
                heights_list.append(players[hl]['height'])
                hl +=1
            
                players_experience.append(players[pe]['experience'])
                pe += 1
            
                guardians_list.append(players[gl]['guardians'])
                gl += 1
                if gl==6:
                    break  
            
            if option2 == user_input1:  
                print('\nTeam: {} Stats:'.format(teams[0]))
                print('heights_list: {}'.format(heights_list))
                print('\nTotal Players: {}'.format(total_players))
                print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
                print('\nTotal inexperienced: {}'.format(len(players_experience) - players_experience.count(True)))
                print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
                print('\nPlayers on team: ',', '.join(player_names))
                print('\nGuardians: ',', '.join(guardians_list))
            
            
            
            pn = 6
            hl = 6
            pe = 6
            gl = 6
            while option2 == user_input2:
                player_names.append(players[pn]['name'])
                pn += 1
                
                heights_list.append(players[hl]['height'])
                hl +=1
            
                players_experience.append(players[pe]['experience'])
                pe += 1
            
                guardians_list.append(players[gl]['guardians'])
                gl += 1
                if gl==12:
                    break   
                
            
            if option2 == user_input2:
                print('\nTeam: {} Stats:'.format(teams[1]))
                print('heights_list: {}'.format(heights_list))
                print('\nTotal Players: {}'.format(total_players))
                print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
                print('\nTotal inexperienced: {}'.format(len(players_experience) - players_experience.count(True)))
                print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
                print('\nPlayers on team: ',', '.join(player_names))
                print('\nGuardians: ',', '.join(guardians_list))
            
            
            
            pn = 12
            hl = 12
            pe = 12
            gl = 12
            while option2 == user_input3:
                player_names.append(players[pn]['name'])
                pn += 1
            
                heights_list.append(players[hl]['height'])
                hl +=1
            
                players_experience.append(players[pe]['experience'])
                pe += 1
            
                guardians_list.append(players[gl]['guardians'])
                gl += 1
                if gl==18:
                    break  
            
            if option2 == user_input3:
                print('\nTeam: {} Stats:'.format(teams[2]))
                print('heights_list: {}'.format(heights_list))
                print('\nTotal Players: {}'.format(total_players))
                print('\nTotal experienced: {}'.format(len(players_experience) - players_experience.count(False)))
                print('\nTotal inexperienced: {}'.format(len(players_experience) - players_experience.count(True)))
                print('\nAverage height: {}'.format(sum(heights_list)/len(heights_list)))
                print('\nPlayers on team: ',', '.join(player_names))
                print('\nGuardians: ',', '.join(guardians_list))
                
            elif option2 > user_input3:
                print('\nPlease enter a number between 1 & 3 ')
                continue
                
            elif option2 < user_input1:
                print('\nPlease enter a number between 1 & 3 ')
                continue    
                
        except ValueError:
            print ('\nError!!!. Please enter a number withing provided range')
        
if __name__ == '__main__':          
    start()
