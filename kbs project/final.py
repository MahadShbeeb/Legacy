from pyknow import *

print("_______________________________________________")
print("Welcome to our legacy partition expert system".center(40, " "))
print("\nBeclouded system in legacy :\n 1-if there is male children => (father,mother,partner) cant be inherits \n 2-if there is male or female children => (brothers,sisters) cant be inherent".center(10, " "))
print("Prevent system in legacy :\n 1-if some of his inheritors change there religion they cant be inherent \n 2-if the dead killed by some of his inheritors the cant be inherent".center(10, " "))
print("\nEnter your dead status ".center(10, " "))
print("_______________________________________________")

results=Fact(mother=0,father=0,malechildrens=0,femalechildrens=0,partner=0,brothers=0,sisters=0,last=0)

class Legacy(KnowledgeEngine):    
    
 @Rule(NOT(AND(Fact(legacy=W()))),salience=7)
 def question1(self):
   l1 = input("how much the legacy is ? ")
   self.declare(Fact(legacy=l1))  

 @Rule(NOT(AND(Fact(gender=W()))),salience=6)
 def question2(self):
   ll = input("what is the dead gender ? ")
   self.declare(Fact(gender=ll))  
   
 @Rule(NOT(AND(Fact(dead_status=W()))),salience=5)
 def question3(self):
   ll = input("is the dead single ? ")
   self.declare(Fact(dead_status=ll))
    
 @Rule(AND(NOT(Fact(childrens_count=W())),Fact(dead_status='no')),salience=4)
 def question4(self):
   ll = input("how many childrens the dead has ? ")
   self.declare(Fact(childrens_count=ll)) 
    
 @Rule(AND(NOT(Fact(male_childrens=W())),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) != 0))),salience=3)
 def question5(self):
   ll = input("how many male childrens the dead has ? ")
   self.declare(Fact(male_childrens=ll)) 
        
 @Rule(AND(NOT(Fact(famale_childrens=W())),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) != 0))),salience=3)
 def question6(self):
   ll = input("how many famale childrens the dead has ? ")
   self.declare(Fact(famale_childrens=ll)) 

 @Rule(OR(AND(NOT(Fact(father_status=W())),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0))),
 AND(NOT(Fact(father_status=W())),Fact(dead_status='yes')),
 AND(NOT(Fact(father_status=W())),Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)))),salience=2)
 def question7(self):
   ll = input("is the dead's father alive ? ")
   self.declare(Fact(father_status=ll)) 

    
 @Rule(OR(AND(NOT(Fact(mother_status=W())),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0))),
 AND(NOT(Fact(mother_status=W())),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0))),
 AND(NOT(Fact(mother_status=W())),Fact(dead_status='yes'))),salience=2)
 def question8(self):
   ll = input("is the dead's mother alive ? ")
   self.declare(Fact(mother_status=ll)) 
    
 @Rule(OR(AND(NOT(Fact(partner_status=W())),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0))),
 AND(NOT(Fact(partner_status=W())),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0))),
 AND(NOT(Fact(partner_status=W())),Fact(dead_status='no'))),salience=2)
 def question9(self):
   ll = input("is the dead's partner alive ,for male dead's any of his wife's alive ? ")
   self.declare(Fact(partner_status=ll))  

 @Rule(OR(AND(NOT(Fact(brothers_count=W())),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0))),
 AND(NOT(Fact(brothers_count=W())),Fact(dead_status='yes'))),salience=1)
 def question10(self):
   ll = input("how many brothers the dead has ? ")
   self.declare(Fact(brothers_count=ll))  

 @Rule(OR(AND(NOT(Fact(sisters_count=W())),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0))),
 AND(NOT(Fact(sisters_count=W())),Fact(dead_status='yes'))),salience=1)
 def question11(self):
   ll = input("how many sisters the dead has ? ")
   self.declare(Fact(sisters_count=ll))  
    
 @Rule(Fact(legacy=P(lambda legacy: float(legacy) == 0)))
 def rule0(self):
   print('the is nothing to share ')

 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='yes'),
 Fact(mother_status='no'),Fact(father_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='no'),Fact(mother_status='no'),
 Fact(father_status='yes'),Fact(partner_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(mother_status='no'),
 Fact(father_status='yes'),Fact(partner_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)))))
 def rule1(self,legacy):
   fatherPartition=float(legacy)
   results['father']=fatherPartition
   print(results,'rule1')
  
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='yes'),
 Fact(mother_status='yes'),Fact(father_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(mother_status='yes'),Fact(father_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='no'),Fact(mother_status='yes'),Fact(father_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),Fact(partner_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(mother_status='yes'),Fact(father_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),Fact(partner_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))      
 def rule2(self,legacy):
   motherPartition=float(legacy)
   results['mother']=motherPartition
   print(results,'rule2')

 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='yes'),
 Fact(mother_status='no'),Fact(father_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(mother_status='no'),Fact(father_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='no'),Fact(mother_status='no'),Fact(father_status='no'),
 Fact(partner_status='no'),Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(mother_status='no'),Fact(father_status='no'),
 Fact(partner_status='no'),Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule3(self,legacy):
   last=float(legacy)  
   results['last']=last
   print(results,'rule3')

 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='yes'),
 Fact(mother_status='yes'),Fact(father_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(mother_status='yes'),Fact(father_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='no'),Fact(mother_status='yes'),Fact(father_status='yes'),
 Fact(partner_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(mother_status='yes'),Fact(father_status='yes'),
 Fact(partner_status='no'),Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule4(self,legacy):
   fatherPartition=2*float(legacy)/3
   motherPartition=float(legacy)/3
   results['father']=fatherPartition
   results['mother']=motherPartition
   print(results,'rule4') 

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(father_status='yes'),Fact(mother_status='yes'),Fact(partner_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule5(self,legacy):
   partnerPartition=float(legacy)/2
   motherPartition=float(legacy)/3
   fatherPartition=float(legacy)-partnerPartition-motherPartition
   results['father']=fatherPartition
   results['mother']=motherPartition
   results['partner']=partnerPartition
   print(results,'rule5') 

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
 Fact(father_status='no'),Fact(mother_status='no'),Fact(partner_status='yes')))
 def rule6(self,legacy):
   partnerPartition=float(legacy)/2
   last=float(legacy)-partnerPartition
   results['partner']=partnerPartition
   results['last']=last
   print(results,'rule6') 

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),                            
 Fact(father_status='no'),Fact(mother_status='yes'),Fact(partner_status='yes')))
 def rule7(self,legacy):
   partnerPartition=float(legacy)/2
   motherPartition=float(legacy)-partnerPartition
   results['partner']=partnerPartition
   results['mother']=motherPartition
   print(results,'rule7') 

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
 Fact(father_status='yes'),Fact(mother_status='no'),Fact(partner_status='yes')))
 def rule8(self,legacy):
   partnerPartition=float(legacy)/2
   fatherPartition=float(legacy)-partnerPartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   print(results,'rule8') 

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(father_status='yes'),Fact(mother_status='yes'),Fact(partner_status='yes')))
 def rule9(self,legacy):
   femalePartition=float(legacy)/2
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   fatherPartition=last1/6
   motherPartition=last1/6
   last=last1-partnerPartition-fatherPartition-motherPartition 
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule9') 
     
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                            
 Fact(partner_status='yes'),Fact(mother_status='no'),Fact(father_status='yes')))
 def rule10(self,legacy):
   femalePartition=float(legacy)/2
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   fatherPartition=last1/6
   last=last1-partnerPartition-fatherPartition 
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule10') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                 
 Fact(partner_status='yes'),Fact(mother_status='yes'),Fact(father_status='no')))
 def rule11(self,legacy):
   femalePartition=float(legacy)/2
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   motherPartition=last1/6
   last=last1-partnerPartition-motherPartition
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule11')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),              
 Fact(partner_status='yes'),Fact(mother_status='no'),Fact(father_status='no')))
 def rule12(self,legacy):
   femalePartition=float(legacy)/2
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   last=last1-partnerPartition
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['last']=last
   print(results,'rule12')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),  
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no')))
 def rule13(self,legacy):
   famalePartition=float(legacy)/2
   last1=float(legacy)-famalePartition
   partnerPartition=last1/8
   last=last1-partnerPartition    
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['last']=last
   print(results,'rule13')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                   
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes')))
 def rule14(self,legacy):
   famalePartition=float(legacy)/2
   last1=float(legacy)-famalePartition
   motherPartition=last1/6
   partnerPartition=last1/8
   last=last1-partnerPartition-motherPartition
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule14')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                   
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no')))
 def rule15(self,legacy):
   famalePartition=float(legacy)/2
   last1=float(legacy)-famalePartition
   fatherPartition=last1/6
   partnerPartition=last1/8
   last=last1-partnerPartition-fatherPartition
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule15')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                         
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes')))
 def rule16(self,legacy):
   famalePartition=float(legacy)/2
   last1=float(legacy)-famalePartition
   motherPartition=last1/6
   fatherPartition=last1/6
   partnerPartition=last1/8
   last=last1-partnerPartition-fatherPartition-motherPartition
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['mother']=motherPartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule16')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='no')),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='no'))))
 def rule17(self,legacy):
   femalePartition=float(legacy)/2
   last=float(legacy)-femalePartition
   results['femalechildrens']=femalePartition
   results['last']=last
   print(results,'rule17')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                      
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='yes')),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                                                                   
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='yes'))))
 def rule18(self,legacy):
   femalePartition=float(legacy)/2
   last1=float(legacy)-femalePartition
   fatherPartition=last1/6
   motherPartition=last1/6
   last=last1-fatherPartition-motherPartition
   results['femalechildrens']=femalePartition
   results['mother']=motherPartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule18')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                              
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='yes')),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),     
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='yes'))))
 def rule19(self,legacy):
   femalePartition=float(legacy)/2
   last1=float(legacy)-femalePartition
   fatherPartition=last1/6
   last=last1-fatherPartition
   results['femalechildrens']=femalePartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule19')
   
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                     
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='no')),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),    
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='no'))))
 def rule20(self,legacy):
   femalePartition=float(legacy)/2
   last1=float(legacy)-femalePartition
   motherPartition=last1/6
   last=last1-motherPartition
   results['femalechildrens']=femalePartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule20')

#  @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
#  Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
#  Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                     
#  Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='no')),
#  AND(Fact(gender='male'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
#  Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
#  Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),   
#  Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='no'))))
#  def rule21(self,legacy):
#    femalePartition=float(legacy)/2
#    last=float(legacy)-femalePartition
#    results['femalechildrens']=femalePartition
#    results['last']=last
#    print(results,'rule21')  
       
#  @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
#  Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
#  Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),                                        
#  Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='yes')),
#  AND(Fact(gender='male'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 1)),
#  Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 1)),
#  Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),     
#  Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='yes'))))
#  def rule22(self,legacy):
#    femalePartition=float(legacy)/2
#    last1=float(legacy)-femalePartition
#    fatherPartition=last1/6
#    last=last1-fatherPartition
#    results['femalechildrens']=femalePartition
#    results['father']=fatherPartition
#    results['last']=last
#    print(results,'rule22')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no')))
 def rule23(self,legacy):
   famalePartition=2*float(legacy)/3
   last1=float(legacy)-famalePartition
   partnerPartition=last1/8
   last=last1-partnerPartition  
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['last']=last
   print(results,'rule23')
   
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes')))
 def rule24(self,legacy):
   famalePartition=2*float(legacy)/3
   last1=float(legacy)-famalePartition
   motherPartition=last1/6
   partnerPartition=last1/8
   last=last1-partnerPartition-motherPartition 
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['last']=last
   print(results,'rule24')

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no')))
 def rule25(self,legacy):
   famalePartition=2*float(legacy)/3
   last1=float(legacy)-famalePartition
   fatherPartition=last1/6
   partnerPartition=last1/8
   last=last1-partnerPartition-fatherPartition 
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule25')

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes')))
 def rule26(self,legacy):
   famalePartition=2*float(legacy)/3
   last1=float(legacy)-famalePartition
   fatherPartition=last1/6
   motherPartition=last1/6
   partnerPartition=last1/8
   last=last1-partnerPartition-fatherPartition-motherPartition
   results['femalechildrens']=famalePartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule26')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(mother_status='yes'),Fact(father_status='yes')))
 def rule27(self,legacy):
   femalePartition=2*float(legacy)/3
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   motherPartition=last1/6
   fatherPartition=last1/6
   last=last1-partnerPartition-motherPartition-fatherPartition
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule27')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(mother_status='no'),Fact(father_status='yes')))
 def rule28(self,legacy):
   femalePartition=2*float(legacy)/3
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   fatherPartition=last1/6
   last=last1-partnerPartition-fatherPartition
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule28')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(mother_status='yes'),Fact(father_status='no')))
 def rule29(self,legacy):
   femalePartition=2*float(legacy)/3
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   motherPartition=last1/6
   last=last1-partnerPartition-motherPartition
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule29')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='yes'),Fact(mother_status='no'),Fact(father_status='no')))
 def rule30(self,legacy):
   femalePartition=2*float(legacy)/3
   last1=float(legacy)-femalePartition
   partnerPartition=last1/4
   last=last1-partnerPartition
   results['femalechildrens']=femalePartition
   results['partner']=partnerPartition
   results['last']=last
   print(results,'rule30')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='yes')),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='yes'))))
 def rule31(self,legacy):
   femalePartition=2*float(legacy)/3
   last1=float(legacy)-femalePartition
   fatherPartition=last1/6
   motherPartition=last1/6
   last=last1-fatherPartition-motherPartition
   results['femalechildrens']=femalePartition
   results['father']=fatherPartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule31')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='yes')),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='yes'))))
 def rule32(self,legacy):
   femalePartition=2*float(legacy)/3
   last1=float(legacy)-femalePartition
   fatherPartition=last1/6
   last=last1-fatherPartition
   results['femalechildrens']=femalePartition
   results['father']=fatherPartition
   results['last']=last
   print(results,'rule32') 
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='no')),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='yes'),Fact(father_status='no'))))
 def rule33(self,legacy):
   femalePartition=2*float(legacy)/3
   last1=float(legacy)-femalePartition
   motherPartition=last1/6
   last=last1-motherPartition
   results['femalechildrens']=femalePartition
   results['mother']=motherPartition
   results['last']=last
   print(results,'rule33')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='no')),
 AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) == 0)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 2)),
 Fact(partner_status='no'),Fact(mother_status='no'),Fact(father_status='no'))))
 def rule34(self,legacy):
   femalePartition=2*float(legacy)/3
   last=float(legacy)-femalePartition
   results['femalechildrens']=femalePartition
   results['last']=last
   print(results,'rule34')
    
#  @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
#  Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
#  def rule35(self,legacy):
#    partnerPartition=float(legacy)/2
#    motherPartition=float(legacy)/3
#    fatherPartition=float(legacy)-partnerPartition-motherPartition
#    results['partner']=partnerPartition
#    results['mother']=motherPartition
#    results['father']=fatherPartition
#    print(results,'rule35')
    
#  @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
#  Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no')))
#  def rule36(self,legacy):
#    partnerPartition=float(legacy)/2
#    fatherPartition=float(legacy)-partnerPartition
#    results['partner']=partnerPartition
#    results['father']=fatherPartition
#    print(results,'rule36')
    
#  @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
#  Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes')))
#  def rule37(self,legacy):
#    partnerPartition=float(legacy)/2
#    motherPartition=float(legacy)-partnerPartition
#    results['partner']=partnerPartition
#    results['mother']=motherPartition
#    print(results,'rule37')
    
#  @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
#  Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no')))
#  def rule38(self,legacy):
#    partnerPartition=float(legacy)/2
#    last=float(legacy)-partnerPartition  
#    results['partner']=partnerPartition
#    results['last']=last
#    print(results,'rule38')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes')))
 def rule39(self,legacy):
   partnerPartition=float(legacy)/8
   motherPartition=float(legacy)/3
   fatherPartition=float(legacy)-partnerPartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   results['mother']=motherPartition
   print(results,'rule39')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no')))
 def rule40(self,legacy):
   partnerPartition=float(legacy)/8
   fatherPartition=float(legacy)-partnerPartition
   results['partner']=partnerPartition
   results['father']=fatherPartition
   print(results,'rule40')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes')))
 def rule41(self,legacy):
   partnerPartition=float(legacy)/8
   motherPartition=float(legacy)-partnerPartition
   results['partner']=partnerPartition
   results['mother']=motherPartition
   print(results,'rule41')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)),      
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no')))
 def rule42(self,legacy):
   partnerPartition=float(legacy)/8
   last=float(legacy)-partnerPartition
   results['partner']=partnerPartition
   results['last']=last
   print(results,'rule42') 
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(male_childrens=MATCH.male_childrens),Fact(famale_childrens=MATCH.famale_childrens),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) >= 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) >= 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) >= 1)))))
 def rule43(self,legacy,famale_childrens,male_childrens):
   first=2*float(male_childrens)
   second=first+float(famale_childrens)
   x=2*float(legacy)/second
   malePartition=x*float(male_childrens)
   famalePartition=x/2*float(famale_childrens)
   results['malechildrens']=malePartition
   results['femalechildrens']=famalePartition
   print(results,'rule43')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) >= 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(male_childrens=P(lambda male_childrens: int(male_childrens) >= 1)),
 Fact(famale_childrens=P(lambda famale_childrens: int(famale_childrens) == 0)))))
 def rule44(self,legacy):
    malePartition=float(legacy)
    results['malechildrens']=malePartition
    print(results,'rule44')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1)))))
 def rule45(self,legacy,brothers_count,sisters_count):
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*float(legacy)/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   print(results,'rule45')
    
 @Rule(Fact(legacy=MATCH.legacy),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1)))))
 def rule46(self,legacy):
   sistersPartition=float(legacy)/2
   last=float(legacy)-sistersPartition
   results['last']=last
   results['sisters']=sistersPartition
   print(results,'rule46')
    
 @Rule(Fact(legacy=MATCH.legacy),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count)>= 2))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2)))))
 def rule47(self,legacy):
   sistersPartition=2*float(legacy)/3
   last=float(legacy)-sistersPartition
   results['last']=last
   results['sisters']=sistersPartition
   print(results,'rule47')
    
 @Rule(Fact(legacy=MATCH.legacy),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count)== 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count)== 0)))))
 def rule48(self,legacy):
   brothersPartition=float(legacy)
   results['brothers']=brothersPartition
   print(results,'rule48')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),
 Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1)))))
 def rule49(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   motherPartiton=2*float(legacy)/3
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   print(results,'rule49')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),
 Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1)))))
 def rule50(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   fatherPartiton=2*float(legacy)/3
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   print(results,'rule50')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1)))))
 def rule51(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   fatherPartiton=float(legacy)/2
   motherPartiton=float(legacy)/6
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['mother']=motherPartiton
   print(results,'rule51')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule52(self,legacy):
   brothersPartition=float(legacy)/3
   fatherPartiton=float(legacy)/2
   motherPartiton=float(legacy)/6
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   results['mother']=motherPartiton
   print(results,'rule52')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule53(self,legacy):
   brothersPartition=float(legacy)/6
   fatherPartiton=float(legacy)/2
   motherPartiton=float(legacy)/3
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   results['mother']=motherPartiton
   print(results,'rule53')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count)>= 2))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2)))))
 def rule54(self,legacy):
   sistersPartition=float(legacy)/3
   fatherPartiton=float(legacy)/2
   motherPartiton=float(legacy)/6
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['mother']=motherPartiton
   print(results,'rule54')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1)))))
 def rule55(self,legacy):
   sistersPartition=float(legacy)/6
   fatherPartiton=float(legacy)/2
   motherPartiton=float(legacy)/3
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['mother']=motherPartiton
   print(results,'rule55')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1)))))
 def rule56(self,legacy):
   sistersPartition=float(legacy)/6
   motherPartiton=float(legacy)-sistersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   print(results,'rule56')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2)))))
 def rule57(self,legacy):
   sistersPartition=float(legacy)/3
   motherPartiton=float(legacy)-sistersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   print(results,'rule57')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule58(self,legacy):
   brothersPartition=float(legacy)/3
   motherPartiton=float(legacy)-brothersPartition
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   print(results,'rule58')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule59(self,legacy):
   brothersPartition=float(legacy)/6
   motherPartiton=float(legacy)-brothersPartition
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   print(results,'rule59')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1)))))
 def rule60(self,legacy):
   sistersPartition=float(legacy)/6
   fatherPartiton=float(legacy)-sistersPartition
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   print(results,'rule60')
    
 @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2)))))
 def rule61(self,legacy):
   sistersPartition=float(legacy)/3
   fatherPartiton=2*float(legacy)/3
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   print(results,'rule61')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule62(self,legacy):
   brothersPartition=float(legacy)/3
   fatherPartiton=float(legacy)-brothersPartition
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   print(results,'rule62')
    
 @Rule(Fact(legacy=MATCH.legacy),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='no'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
 AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))
 def rule63(self,legacy):
   brothersPartition=float(legacy)/6
   fatherPartiton=float(legacy)-brothersPartition
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   print(results,'rule63')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))))
 def rule64(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)/2-partnerPartition
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule64')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))))
 def rule65(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   fatherPartiton=0
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule65') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule66(self,legacy):
   brothersPartition=float(legacy)/6
   motherPartiton=float(legacy)/3
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)/2-partnerPartition
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule66') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule67(self,legacy):
   brothersPartition=float(legacy)/3
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)/2-partnerPartition
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule67') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule68(self,legacy):
   brothersPartition=float(legacy)/6
   motherPartiton=float(legacy)/3
   partnerPartition=float(legacy)/2
   fatherPartiton=0
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule68')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule69(self,legacy):
   brothersPartition=float(legacy)/3
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   fatherPartiton=0
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule69') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule70(self,legacy):
   sistersPartition=float(legacy)/6
   motherPartiton=float(legacy)/3
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)/2-partnerPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule70') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule71(self,legacy):
   sistersPartition=float(legacy)/3
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)/2-partnerPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule71') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule72(self,legacy):
   sistersPartition=float(legacy)/6
   motherPartiton=float(legacy)/3
   partnerPartition=float(legacy)/2
   fatherPartiton=0
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule72') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule73(self,legacy):
   sistersPartition=float(legacy)/3
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   fatherPartiton=0
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule73')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule74(self,legacy):
   brothersPartition=float(legacy)/6
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)-partnerPartition-brothersPartition
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule74') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule75(self,legacy):
   brothersPartition=float(legacy)/3
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)-partnerPartition-brothersPartition
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule75') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule76(self,legacy):
   brothersPartition=float(legacy)/3
   fatherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule76') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule77(self,legacy):
   brothersPartition=float(legacy)/3
   fatherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   results['brothers']=brothersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule77')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule78(self,legacy):
   sistersPartition=float(legacy)/6
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)-partnerPartition-sistersPartition
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule78') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule79(self,legacy):
   sistersPartition=float(legacy)/3
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)-partnerPartition-sistersPartition
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule79')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule80(self,legacy):
   sistersPartition=float(legacy)/6
   fatherPartiton=float(legacy)/3
   partnerPartition=float(legacy)/2
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule80') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule81(self,legacy):
   sistersPartition=float(legacy)/3
   fatherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule81')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule82(self,legacy):
   brothersPartition=float(legacy)/6
   partnerPartition=float(legacy)/8
   motherPartiton=float(legacy)-partnerPartition-brothersPartition
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule82')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule83(self,legacy):
   brothersPartition=float(legacy)/3
   partnerPartition=float(legacy)/8
   motherPartiton=float(legacy)-partnerPartition-brothersPartition
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule83') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule84(self,legacy):
   brothersPartition=float(legacy)/6
   motherPartiton=float(legacy)/3
   partnerPartition=float(legacy)/2
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule84') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 2)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule85(self,legacy):
   brothersPartition=float(legacy)/3
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   results['brothers']=brothersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule85')

 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule86(self,legacy):
   sistersPartition=float(legacy)/6
   partnerPartition=float(legacy)/8
   motherPartiton=float(legacy)-partnerPartition-sistersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule86')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule87(self,legacy):
   sistersPartition=float(legacy)/3
   partnerPartition=float(legacy)/8
   motherPartiton=float(legacy)-partnerPartition-sistersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule87') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule88(self,legacy):
   sistersPartition=float(legacy)/6
   motherPartiton=float(legacy)/3
   partnerPartition=float(legacy)/2
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule88') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule89(self,legacy):
   sistersPartition=float(legacy)/3
   motherPartiton=float(legacy)/6
   partnerPartition=float(legacy)/2
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule89')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule90(self,legacy):
   partnerPartition=float(legacy)/8
   brothersPartition=float(legacy)-partnerPartition
   results['brothers']=brothersPartition
   results['partner']=partnerPartition
   print(results,'rule90')     
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))))
 def rule91(self,legacy):
   brothersPartition=float(legacy)/2
   partnerPartition=float(legacy)/2
   results['brothers']=brothersPartition
   results['partner']=partnerPartition
   print(results,'rule91')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule92(self,legacy):
   sistersPartition=float(legacy)/2
   partnerPartition=float(legacy)/8
   last=float(legacy)-partnerPartition-sistersPartition
   results['sisters']=sistersPartition
   results['last']=last
   results['partner']=partnerPartition
   print(results,'rule92')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule93(self,legacy):
   sistersPartition=2*float(legacy)/3
   partnerPartition=float(legacy)/8
   last=float(legacy)-partnerPartition-sistersPartition
   results['sisters']=sistersPartition
   results['last']=last
   results['partner']=partnerPartition
   print(results,'rule93') 
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))))
 def rule94(self,legacy):
   sistersPartition=float(legacy)/2
   partnerPartition=float(legacy)/2
   results['sisters']=sistersPartition
   results['partner']=partnerPartition
   print(results,'rule94')
    
 @Rule(Fact(legacy=MATCH.legacy),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 2))))
 def rule95(self,legacy):
   sistersPartition=float(legacy)/3
   partnerPartition=float(legacy)/2
   last=float(legacy)-sistersPartition-partnerPartition
   results['sisters']=sistersPartition
   results['last']=last
   results['partner']=partnerPartition
   print(results,'rule95')
    
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),
 Fact(sisters_count=MATCH.sisters_count),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))))
 def rule96(self,legacy,brothers_count,sisters_count):
   partnerPartition=float(legacy)/2
   share=float(legacy)-partnerPartition
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   last=float(legacy)-sistersPartition-partnerPartition
   results['sisters']=sistersPartition
   results['brothers']=brothersPartition
   results['partner']=partnerPartition
   print(results,'rule96')
   
 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),
 Fact(sisters_count=MATCH.sisters_count),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))))
 def rule97(self,legacy,brothers_count,sisters_count):
   partnerPartition=float(legacy)/8
   share=float(legacy)-partnerPartition
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   results['sisters']=sistersPartition
   results['brothers']=brothersPartition
   results['partner']=partnerPartition
   print(results,'rule97')

#  @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='yes'),
#  Fact(mother_status='no'),Fact(father_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
#  AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(mother_status='no'),Fact(father_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
#  AND(Fact(gender='male'),Fact(dead_status='no'),Fact(mother_status='no'),Fact(father_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),Fact(partner_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0))),
#  AND(Fact(gender='female'),Fact(dead_status='no'),Fact(mother_status='yes'),Fact(father_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),Fact(partner_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 0)))))      
#  def rule98(self,legacy):
#    brothersPartition=float(legacy)
#    results['brothers']=brothersPartition
#    print(results,'rule98')

#  @Rule(Fact(legacy=MATCH.legacy),OR(AND(Fact(gender='male'),Fact(dead_status='yes'),
#  Fact(mother_status='no'),Fact(father_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count)  == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
#  AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(mother_status='no'),Fact(father_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count) == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
#  AND(Fact(gender='male'),Fact(dead_status='yes'),Fact(mother_status='no'),Fact(father_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),Fact(partner_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count)  == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1))),
#  AND(Fact(gender='female'),Fact(dead_status='yes'),Fact(mother_status='yes'),Fact(father_status='no'),
#  Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),Fact(partner_status='no'),
#  Fact(brothers_count=P(lambda brothers_count: int(brothers_count)  == 0)),
#  Fact(sisters_count=P(lambda sisters_count: int(sisters_count) == 1)))))      
#  def rule99(self,legacy):
#    sistersPartition=float(legacy)/2
#    last=float(legacy)-sistersPartition
#    results['sisters']=sistersPartition
#    results['last']=last
#    print(results,'rule99')

 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='male'),Fact(dead_status='no'),Fact(partner_status='yes'),
 Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1)))))
 def rule100(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   partnerPartition=float(legacy)/8
   fatherPartiton=float(legacy)-partnerPartition-share
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule100')

 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),Fact(sisters_count=MATCH.sisters_count),
 OR(AND(Fact(gender='female'),Fact(dead_status='no'),Fact(partner_status='yes'),
 Fact(father_status='yes'),Fact(mother_status='no'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1)))))
 def rule101(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   partnerPartition=float(legacy)/2
   fatherPartiton=float(legacy)/6
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['father']=fatherPartiton
   results['partner']=partnerPartition
   print(results,'rule101')

 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),
 Fact(sisters_count=MATCH.sisters_count),AND(Fact(gender='male'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))))
 def rule102(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   partnerPartition=float(legacy)/8
   motherPartiton=float(legacy)-partnerPartition-share
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule102')

 @Rule(Fact(legacy=MATCH.legacy),Fact(brothers_count=MATCH.brothers_count),
 Fact(sisters_count=MATCH.sisters_count),AND(Fact(gender='female'),Fact(dead_status='no'),
 Fact(partner_status='yes'),Fact(father_status='no'),Fact(mother_status='yes'),
 Fact(childrens_count=P(lambda childrens_count: int(childrens_count) == 0)),
 Fact(brothers_count=P(lambda brothers_count: int(brothers_count) >= 1)),
 Fact(sisters_count=P(lambda sisters_count: int(sisters_count) >= 1))))
 def rule103(self,legacy,brothers_count,sisters_count):
   share=float(legacy)/3
   first=2*float(brothers_count)
   second=first+float(sisters_count)
   x=2*share/second
   brothersPartition=x*float(brothers_count)
   sistersPartition=x/2*float(sisters_count)
   partnerPartition=float(legacy)/2
   motherPartiton=float(legacy)/6
   results['brothers']=brothersPartition
   results['sisters']=sistersPartition
   results['mother']=motherPartiton
   results['partner']=partnerPartition
   print(results,'rule103')

engine = Legacy()
engine.reset()
engine.run()