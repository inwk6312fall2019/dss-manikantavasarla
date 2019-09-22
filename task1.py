def nested_sum(nestedList):
        newList = []
        #Helper function to flatten the list
        def flatlist(nestedList):
                '''
                Returns a flat list
                '''
                for i in range(len(nestedList)):
                        if type(nestedList[i]) == int:
                                newList.append(nestedList[i])
                        else:
                                flatlist(nestedList[i])
                return newList

        flatlist(nestedList)
        print(sum(newList))
        
nested_sum(nestedList)
