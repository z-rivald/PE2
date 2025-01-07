from sys import path
path.append('D:\\study\\Python\\PE2\\1-3_Section_3_Modules_and_Packages\\packages\\extrapack.zip')

    
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())