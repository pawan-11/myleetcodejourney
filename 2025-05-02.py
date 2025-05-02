class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        statechanged = True
        dots = []
        for i in dominoes:
            if i == ".":
                dots.append(i)
        
        while statechanged:
            for i,dot in enumerate(dots):
                if dot != ".":
                    continue
                forces = (dominoes[i-1]if i > 0 else ".") + (
                    dominoes[i+1]if i < len(dominoes)-1 else ".")
                statechanged = False
                if forces == "LR" or forces == "RL":
                    continue
                elif forces[1] == "L":
                    dots[i] = "L"
                    statechanged = True
                elif forces[0] == "R":
                    dots[i] = "R"
                    statechanged = True
            #statechanged = False
        final = ""
        dotidx = 0
        for i,state in enumerate(dominoes):
            if state == ".":
                final += dots[dotidx]
                dotidx += 1
            else:
                final += dominoes[i]            
        return final
