#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/charmander").json()
    print(''' 
            
            
   
                                                      
   (      )                             (             
   )\  ( /(    ) (      )      )        )\ )  (  (    
 (((_) )\())( /( )(    (    ( /(  (    (()/( ))\ )(   
 )\___((_)\ )(_)|()\   )\  ')(_)) )\ )  ((_))((_|()\  
((/ __| |(_|(_)_ ((_)_((_))((_)_ _(_/(  _| (_))  ((_) 
 | (__| ' \/ _` | '_| '  \() _` | ' \)) _` / -_)| '_| 
  \___|_||_\__,_|_| |_|_|_|\__,_|_||_|\__,_\___||_|             
            
                _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
                            `" " -'
            ''')
    
    print("Games this pokemon has been in: " , len(pokeapi["game_indices"]))
    print( pokeapi["sprites"]["front_default"])
    for codex in pokeapi["moves"]:
        ans=[]
        results= codex["move"]["name"]
        ans.append(results)
        print(results)

             
      
main() 
