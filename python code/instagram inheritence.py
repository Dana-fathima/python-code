
'''INSTAGRAM VERSION MULTI LEVEL INHERITANCE'''
# class INSTAGRAM0:
#     version="old"
#     def __init__(self,user_name):
#         self.user_name=user_name
#     def message(self):
#         print("start conversation")
#     def story(self):
#         print("upload story")
    
# class INSTAGRAM1(INSTAGRAM0):
#     version="new"
#     def __init__(self,user_name):
#         super().__init__(user_name)
#     def highlights(self):
#         print("add to highlight")
#         print("view on profile")
#     def post(self):
#         print("add song")
#         print("add location")

# class INSTAGRAM2(INSTAGRAM1):
#     def __init__(self,user_name):
#         super().__init__(user_name)
#     def game(self):
#         print("double click on emoji")

# amy=INSTAGRAM0("a_m_y")
# print(amy.version)
# amy.message()
# amy.story()

# print("-----------------------------------------------------")

# dana=INSTAGRAM1("n_.r_")
# print(dana.version)
# dana.highlights()
# dana.post()
# dana.story()
# dana.message()


# print("--------------------------------------------------------")

# diya=INSTAGRAM2("ai_dia")
# print(diya.version)
# diya.game()

'''old
start conversation
upload story
-----------------------------------------------------
new
add to highlight
view on profile
add song
add location
upload story
start conversation
--------------------------------------------------------
new
double click on emoji'''



'''ENCAPSULE INSTAGRAM FOLLOWERS AND FOLLOWING VERSION '''

class instagram:
    def __init__(self,):