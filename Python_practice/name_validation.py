import re

def CodelandUsernameValidation(strParam):
  pattern = "^[A-Za-z0-9_-]*$"
  state = False
  if len(strParam) > 24 or len(strParam) < 4:
      state = False
  else:

    if bool(re.match(pattern, strParam)) == False:
      state = False

    else:
      if strParam[0].isalpha() and strParam[len(strParam)-1] != "_":
        state = True
      else:
        state = False
    return state
    

# keep this function call here 
print(CodelandUsernameValidation(input()))