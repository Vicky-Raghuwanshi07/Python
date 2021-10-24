## in lives_draw dict we have 0,1,2,3,4,5 as keys and this keys contains values of a hangman stage by stage

lives_draw= {
        0: f"""
                ___________
               | /        | 
               |/        ( )
               |          |     Lives : 0
               |         / \\
               |
                      YOU DIE
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |     Lives : 1
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |	Lives : 2
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          	Lives : 3
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          	Lives : 4
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          	Lives : 5
               |          
               |
          """
    }
