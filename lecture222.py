import pdb

# with open("lecture221.html","r") as webpage:
#     with open("output.txt","a") as wf:
#         for line in webpage.readlines():
#             if "<a href=" in line:
#                 pos = line.find('<a href=')
#                 FIRST_QUOTE = line.find('\"',pos)
#                 SECOND_QUOTE=line.find('\"',FIRST_QUOTE+1)
#                 url = line[ FIRST_QUOTE+1:SECOND_QUOTE]
#                 wf.write(url + '\n')



with open("lecture221.html","r") as webpage:
    with open("output2.txt","a") as wf:
        link_exist=True
        while link_exist:
            pos = line.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
              FIRST_QUOTE = line.find('\"',pos)
              SECOND_QUOTE=line.find('\"',FIRST_QUOTE+1)
              url = line[ FIRST_QUOTE+1:SECOND_QUOTE]
              wf.write(url + '\n')
              page=page[second_quote]





