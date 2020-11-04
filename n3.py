# def questionA(n , from_rod, to_rod, aux_rod): 
#     if n == 1: 
#         print "Move disk 1 from rod",from_rod,"to rod",to_rod 
#         return
#     questionA(n-1, from_rod, aux_rod, to_rod) 
#     print "Move disk",n,"from rod",from_rod,"to rod",to_rod 
#     questionA(n-1, aux_rod, to_rod, from_rod) 


def questionAB(n , debut, inter, fin): 
    if n == 1: 
        print ("Deplacer disque 1 de",debut,"----->",fin)
        return
    questionAB(n-1, debut, fin, inter) 
    print ("Deplacer disque",n,"de",debut,"----->",fin) 
    questionAB(n-1, inter, debut, fin) 

n = 4
questionAB(n, 'A', 'B', 'C')  



# def hanoi(n, source, helper, target):
#     print ("hanoi( ", n, source, helper, target, " called")
#     if n > 0:
#         # move tower of size n - 1 to helper:
#         hanoi(n - 1, source, target, helper)
#         # move disk from source peg to target peg
#         if source[0]:
#             disk = source[0].pop()
#             print ("moving " + str(disk) + " from " + source[1] + " to " + target[1])
#             target[0].append(disk)
#         # move tower of size n-1 from helper to target
#         hanoi(n - 1, helper, source, target)
        
# source = ([4,3,2,1], "source")
# target = ([], "target")
# helper = ([], "helper")
# hanoi(len(source[0]),source,helper,target)

# print (source, helper, target)